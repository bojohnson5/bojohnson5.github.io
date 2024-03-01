Title: Bytes, Reloaded
Date: 2024-03-01
Category: Code 
Author: Bo Johnson
Tags: python

I might have been a overzealous in my [previous post]({filename}bytes.md) 
about using [Julia](www.julialang.org) as the best way
for parsing binary files in the most efficient, pleasant-to-use manner. I think I was
also too eager to forgo using Python in my analysis due to slow looping. I'll save most of
my reasons in switching from Julia to Python in another post, but I wanted to revisit how
I parsed the [WaveDump](https://www.caen.it/products/caen-wavedump/) output files and 
do the same thing in Python. Mostly as a way for me to get back into writing posts
but also to provide the stepping stone for the next post on switching languages.

To recap WaveDump outputs binary files in a structure where the first six 32-bit values
constitute the header, giving information on the number of waveform samples coming next
and waveform number count. Then based on the header info we can read the next `n` 16-bit 
values as the waveform ADC values. I looked at several different ways to accomplish this
in Python, one method using [NumPy](www.numpy.org), another using the built-in module
`struct`, but the one I found easiest to do this in was with the built-in module `array`.

The code looks like

```python
import array
import numpy as np


def read_binary_file_array(file_path):
    with open(file_path, "rb") as binary_file:
        header = array.array("I")
        data = array.array("H")
        while binary_file.peek() != b'':
            header.fromfile(binary_file, 6)
            data.fromfile(binary_file, 500)

    return np.array(header).reshape(-1, 6), np.array(data).reshape(-1, 500)
```

The nice thing about the `array` module is continuing to read into an already-created
array will just append the values, whereas the other two methods I tried you need to do 
the appending yourself. I return as `numpy` arrays and can reshape them into however 
many waveforms were taken during the data run. There should be some more work done on
determining how long the waveforms are and making this function more general, but for the
current purpose I think it shows how easy it is to accompish this same task of reading
custom binary files in Python as it is in other languages.
