Title: Takin' a Byte
Date: 2024-02-28 13:48
Category: Code
Author: Bo Johnson
Tags: julia, c++, root

My first summer as a graduate student I characterized a PMT for use in our upcoming ton-scale
liquid argon neutrino detector. I'd never had hardware experience coming in from undergrad so
I had to quickly learn not only about PMTs but also digitizers and the software used to control
them and later analyze data. I've since become familiar with a couple of DAQ
packages such as [ADAQ](https://github.com/zach-hartwig/ADAQ) and [WaveDump](https://www.caen.it/products/caen-wavedump/).
The first package has built-in capabilities to save data to a ROOT file (ROOT being the
aforementioned data analysis software) whereas the second
one required another tool to do so. For that I used [TOWARD](https://github.com/jintonic/toward)
developed by a collaborator at South Dakota that converts WaveDump binaries to ROOT.
Now, using ROOT takes some getting used to and it's a great tool for physics experiments and
physics analyses. However, I find the C++ baggage to slow down analysis and data exploration
to the point where I wanted to look elsewhere for a better-suited tool.

At first I looked into PyROOT which are Python bindings to use ROOT libraries but inside
the ease of Python programming. That means using Jupyter Notebooks is an option for plotting
data and results and quickly developing some new analysis techniques or tweaking old ones. I
like the ability to read any ROOT file like I would in a ROOT macro from Python, but once
again, there are built-in limitations when you use Python. For example, I was attempting to
work with results from a GEANT4 simulation with PyROOT which required looping over 
200,000 generated events. The code I had was running for over an hour-and-a-half before I 
gave up on it. The same ROOT macro, on the other hand, took 10-20 seconds to run. So I felt
the need to look elsewhere for the ability to analyze data from a ROOT file that wasn't a 
ROOT script or required PyROOT. And that led me back to Julia.

I'd used Julia for a summer in undergrad for fun. I spent some time reading the documentation
and different tutorials but never had a real project to put my mind towards solving with
Julia. And I figured in grad school everyone used Python and ROOT (read C++) so I should
stick with and master those. But now that I'd exhausted those options for what I was trying
to do, I thought I could resurrect what I'd learned about Julia from a few years prior. One
of the first things I wanted to do was revisit my PMT analysis code and rewrite some of it
in Julia. A simple ROOT script from the TOWARD code was converting WaveDump binary files to
ROOT. Here are a few lines from that code:

```cpp
ifstream *input = new ifstream(Form("%s/%s",run,file), ios::binary);
input->seekg(0, ios::end); // move getter to the end of file
long int fsize = input->tellg();// get input file size
input->seekg(0, ios::beg); // move getter back to the beginning
short adc[99999]= {0}; float s[99999]={0}; // waveform samples
int n, len, tmp, cha, evt, ttt, tt, th, tl;
```

This reads in the binary file and gets the file size in bytes along with creating variables
to be stored in a ROOT file. After creating ROOT branches for the new file, the code 
reads the event header from the binary file. The binary file has a structure of six 
four-byte integers followed by a series of ADC values stored from the digitizer. The number 
of two-byte ADC integers is found in the header with a little algebra. The header and ADC 
values are read in as:

```cpp
while (input->good() && input->tellg()<fsize) {
  input->read(reinterpret_cast<char*>(&len),4); // size of data [bytes]
  input->read(reinterpret_cast<char*>(&tmp),4); // board id
  input->read(reinterpret_cast<char*>(&tmp),4); // VME specific
  input->read(reinterpret_cast<char*>(&cha),4); // channel id
  input->read(reinterpret_cast<char*>(&evt),4); // event id
  input->read(reinterpret_cast<char*>(&ttt),4); // trigger time tag
  n = (len-24)/ssize; // number of waveform samples
  for (int i=0; i<n; i++) {
    input->read(reinterpret_cast<char*>(&adc[i]),ssize); s[i]=(float)adc[i];
  }
}
```

With the code above being the core of the what converts the binary file, I set about doing
the same in Julia. I started with nearly a line-for-line rewrite, using something like:

```julia
open("file", "w") do io
  seekend(io)
  fsize = position(io)
  seekstart(io)
  len = Vector{UInt8}(undef, 4)
  read!(io, len)
  len = reinterpret(reshape, Int32, len)
end
```

Similar code would need to be written for the other variables and ADC values. But as you
can imagine, this was pretty long and unwieldy, reading in each byte into a vector bytes of
the correct length and then reinterpreting it as the correct-sized integer. After reading
different posts on the Julia [Discourse](https://discourse.julialang.org) and elsewhere
I quickly found much simpler solutions than my naive rewrite above. It turns out you can
directly read in the correct-sized integers with a simple `read(io, Int32)`, or better
yet, read in the whole header and ADC values as

```julia
header = read!(io, Vector{Int32}(undef, 6))
adcs = read!(io, Vector{Int16}(undef, adc_length))
```

where the `adc_length` is determined as in the TOWARD code. This greatly simplified
my first attempt at reading a binary file. And to take it one step further, I wanted
to remove any ROOT dependency at all and found [JLD2.jl](https://github.com/JuliaIO/JLD2.jl)
which is a pure Julia file format. Adding in some code to save to a `.jld2` file and
compressing it with [CodecZlib.jl](https://github.com/JuliaIO/CodecZlib.jl) I could
beat the compressed ROOT file by almost a factor of two.

So if you find yourself needing to read a binary file from scratch, I'd recommend using
Julia, as the ease and simplicity make for a great experience. And you can get back to
your physics analysis sooner.
