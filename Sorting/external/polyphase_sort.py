import os
import heapq

def distribute_runs(input_file, run_size, tapeA, tapeB):
    """
    Distributes sorted runs alternately to tapeA and tapeB.
    """
    with open(input_file, 'r') as f, \
         open(tapeA, 'w') as a, open(tapeB, 'w') as b:
        useA = True
        while True:
            chunk = []
            for _ in range(run_size):
                line = f.readline()
                if not line:
                    break
                chunk.append(int(line.strip()))
            if not chunk:
                break
            chunk.sort()
            out = a if useA else b
            for num in chunk:
                out.write(f"{num}\n")
            useA = not useA

def merge_files(input_files, output_file):
    """
    Merge sorted numbers from input_files into output_file.
    """
    files = [open(f, 'r') for f in input_files]
    heap = []
    for idx, f in enumerate(files):
        line = f.readline()
        if line:
            heapq.heappush(heap, (int(line.strip()), idx))
    with open(output_file, 'w') as out:
        while heap:
            val, idx = heapq.heappop(heap)
            out.write(f"{val}\n")
            next_line = files[idx].readline()
            if next_line:
                heapq.heappush(heap, (int(next_line.strip()), idx))
    for f in files:
        f.close()

def polyphase_sort(input_file, output_file, run_size=3):
    """
    Demonstration of Polyphase Merge Sort (simplified, 3 tapes as files).
    Each line in the file should contain one integer.
    """
    tapeA = 'tapeA.txt'
    tapeB = 'tapeB.txt'
    tapeC = 'tapeC.txt'
    
    # 1. Distribute initial runs to tapeA and tapeB
    distribute_runs(input_file, run_size, tapeA, tapeB)
    
    finished = False
    # Repeatedly merge from two tapes to the third until only one has data
    while not finished:
        # Check which tapes are non-empty
        nonempty = []
        for t in [tapeA, tapeB, tapeC]:
            if os.path.exists(t) and os.path.getsize(t) > 0:
                nonempty.append(t)
        if len(nonempty) == 1:
            os.rename(nonempty[0], output_file)
            finished = True
        else:
            # Pick two non-empty tapes to merge, output to the empty one
            tapes_in = nonempty[:2]
            tape_out = [t for t in [tapeA, tapeB, tapeC] if t not in tapes_in][0]
            merge_files(tapes_in, tape_out)
            # Clear input tapes for next round
            for t in tapes_in:
                os.remove(t)

if __name__ == "__main__":
    # Demo input
    with open("poly_input.txt", "w") as f:
        f.write("\n".join(str(x) for x in [7, 3, 5, 1, 9, 2, 8, 4, 6, 0]))

    polyphase_sort("poly_input.txt", "poly_output.txt", run_size=3)

    # Show sorted result
    with open("poly_output.txt", "r") as f:
        print([int(line.strip()) for line in f])
