import os
import heapq

def split_and_sort(input_file, chunk_size):
    """
    Splits the input file into sorted chunk files.
    Returns a list of sorted chunk filenames.
    """
    chunk_files = []
    with open(input_file, 'r') as f:
        chunk = []
        idx = 0
        for line in f:
            chunk.append(int(line.strip()))
            if len(chunk) == chunk_size:
                chunk.sort()
                chunk_filename = f"chunk_{idx}.txt"
                with open(chunk_filename, 'w') as cf:
                    for num in chunk:
                        cf.write(f"{num}\n")
                chunk_files.append(chunk_filename)
                chunk = []
                idx += 1
        # Write any remaining data
        if chunk:
            chunk.sort()
            chunk_filename = f"chunk_{idx}.txt"
            with open(chunk_filename, 'w') as cf:
                for num in chunk:
                    cf.write(f"{num}\n")
            chunk_files.append(chunk_filename)
    return chunk_files

def merge_sorted_files(chunk_files, output_file):
    """
    Merges multiple sorted chunk files into a single sorted output file.
    """
    # Open all files and initialize a heap with their first elements
    files = [open(fn, 'r') for fn in chunk_files]
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
    # Optionally delete chunk files
    for fn in chunk_files:
        os.remove(fn)

def external_merge_sort(input_file, output_file, chunk_size=1000):
    """
    Sorts a large file using external merge sort.
    Each line in the file should contain one integer.
    """
    # 1. Split and sort
    chunk_files = split_and_sort(input_file, chunk_size)
    # 2. Merge
    merge_sorted_files(chunk_files, output_file)


if __name__ == "__main__":
    # Prepare a demo input file (if you want to test)
    with open("data.txt", "w") as f:
        f.write("\n".join(str(x) for x in [5, 1, 9, 3, 7, 4, 2, 8, 6, 0]))

    external_merge_sort("data.txt", "sorted_data.txt", chunk_size=3)

    # Print sorted result
    with open("sorted_data.txt", "r") as f:
        print([int(line.strip()) for line in f])
