### What is self.data?

self.data is the internal storage of your custom array.
It’s a Python list that acts like a fixed-size memory block — even though Python lists are dynamic by nature, we’re simulating a static array using them

`self.data = [None] * 4`

“I want to allocate a block of 4 memory slots (filled with None) where I’ll store future elements.”

Even though Python lists can resize dynamically, you won’t use that feature. Instead, you manually manage the size and simulate how arrays work in languages like C or Java.


### What is None keyword?

None is a special keyword in Python that represents the absence of a value or a null reference.

It’s like saying:

“This slot exists, but nothing is stored in it yet.”


###  Why Add _ Before resize()?

Adding a single underscore _resize() is a signal:
“This is a private/internal method, not meant to be called from outside the class.”

Unlike Java or C++, Python doesn’t have true private methods.
But developers follow naming conventions to communicate intent.

Prefix	       Meaning
resize()	    Public method — meant to be called from anywhere
_resize()	    Internal method — intended to be used only inside the class
__resize()	  Name mangling (used to avoid subclass override conflicts) — not needed here
