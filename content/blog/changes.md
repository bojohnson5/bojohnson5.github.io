+++
title = "Ch-ch-ch changes"
description = "Where I talk about new things"
date = "2024-03-02"

[taxonomies]
blog-tags = ["Test", "Personal"]
+++

# The early days

I have to make a confession at the start here. I'm like a squirrel in the middle
of a field full of nuts when it comes to technology: I run around trying all
the latest things and never stick around on one piece of tech for long. This
not only include gadgets like phones or computers, but also operating systems
and programming languages. I think this stems from my earliest days learning to
program and doing research in undergrad. When you're first introduced to Linux,
which a lot of physicists tend to use because it's free, you're immediately
immersed in a world that offers tons of possibilities and choices. One day you can be on
Linux Mint and then the next Ubuntu, followed by Fedora or Arch. Not to mention
all the flavors and desktops you can try as well. Then there are the programming
language options. I learned C++ because of the intro computer science courses but
was also asked to learn Fortran with the first professor I worked with. Then
it's easy to see how much easier some tasks can be done in Matlab or Python or 
Java or, or, or… And my personality is to want to learn all the things. So while
I spent time learning multiples of these I never got that great in any. I'd say
I was the most exposed and experienced with C++ because I took so many courses that taught it, but
for research and personal stuff I would hop around and try different things.

So when I started grad school I thought I would try to stick to whatever people
around me were using. In particle physics this tends to be C++ because ROOT. 
I've certainly learned how to use that and feel comfortable in manipulating
ROOT files and creating ROOT scripts and plotting in ROOT. But honestly it feels
like you need to have mild psychosis to want to do serious analysis in ROOT, and 
by extension, C++. It's just that it takes so much coding in order to accomplish
any small take such as plotting data. What would take two or three lines in Python
script requires multiples of that in C++. It's really painful. It's not elegant,
either. You really have to contort your thinking to the mold of C++ for the analysis
rather than the language you're using being molded to your analysis. Which is why
for a while I also tried to do things in Python. It's really nice to program in 
Python because it's higher-level constructs like list comprehensions, generators,
and functional programming tools make it possible to shape the code to how you
envision the analysis unfolding.

# The matchup

The issue with Python though is it's speed. Now any programming language is fast
by any means and for really any normal task I come across. (Admittedly, I'm not 
a programmer by trade and so normal tasks for me are analyzing data, plotting,
fitting data, etc.). But when it comes to analyzing gigabytes of data that contain
hundreds of thousands of simulated physics interactions, for example, Python tends
to grind to a halt. So it seemed, when I started grad school and doing research,
the only options were Python for the simple things like plotting, but having to
use C++ for serious lifting. 

Enter Julia. I learned a bit about Julia over a summer intership during undergrad.
I spent a lot of time learning it's ins and outs and think it's got some really
neat features. I was drawn to its mantra "Walks like Python, runs like C" because
that was the problem I had hoped to solve with Python and ROOT. When I was
running up against the wall with analysis, not wanting to use ROOT and waiting for
Python to finish running, I started accomplishing my work with Julia. I've even
contributed to a Julia package I used quite often. Once I started using Julia for
more things, I started to get hung up on little things here and there. The one 
issue you have to deal with whenever you run code is waiting for it to compile. So 
if you're wanting to do some plots, you have to wait for tens of seconds for it to
compile first. I know that issue has been one of the most pressing for the Julia
community and a lot of work has gone into bringing the so-called time to first plot
down, but it still isn't as nice as using Python for simple things there. Another
thing I'd run up against was the lack of mature packages. Julia is a lot less
established than Python and so looking for packages to do something like curve
fitting isn't as straight forward as using SciPy. The package universe in Julia
is more disparate and less well maintained, for the things I was hoping to get done.
It's really nice that the usual libraries in Python for scientific research have
been around a long time and are really well maintainted and tested, like NumPy,
SciPy, Matplotlib, etc. In Julia there's no standard for curve fitting or integration
or even plotting. So it's easy to look at any package askanse in Julia because you
don't know how battle-tested it is. 

# The result

With all these little things starting to add up, I decided to once again give Python
a try. That's because I (re)learned the benefits of using [Numba](numba.pydata.org)
in conjunction with Python. It's kind of like Julia in that you can compile Python
code, but it's unlike Julia in that you only compile what you really need to speed up.
So I can code and do analysis with nice-looking, easy to understand code wherever I 
want, but when I need that extra speed boost, I put on my C++-style coding hat and 
write some Python code that Numba is able to compile. Now things run as fast as I need
and there's no more bottleneck in Python. I get to use the nice Python packages that
have been around for a long time and know there's more helpful information out there
on the internet with any question I might have, too.

So right now, I'm trying to do the responsible thing and stick to a single programming
language for physics analysis. Python's actually been quite easy to pick up again and 
I'm hoping my squirrel brain won't be too perturbed by all the shiny-looking languages
out there (looking at you [Rust](www.rust-lang.org)).
