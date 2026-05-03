+++
title = "Blastin' off like a rocket"
description = "Where I work out the rocket equation"
date = "2025-02-13"

[taxonomies]
blog-tags = ["Physics"]
+++

When taking classical mechanics as an undergraduate I remember going through the example of the rocket equation
from Taylor's book and thinking it was going about the derivation in a more difficult way than it could have
been presented. The general equation you start with for any dynamics problem in classical mechanics (at least
starting out) is $F^{ext}=m\frac{dv}{dt}$ which assumes the mass doesn't change. But for the rocket equation we
can no longer make that assumption and have to use the more general equation $F^{ext}=\dot{p}$. I want to show
how a short circuit in thinking beginning with this equation yields the same results as Taylor does using the
approach of differentials.

To get to that point I first need to lay out the problem we're looking at. A rocket is launched vertically from
the Earth's surface with the exhaust velocity $v_{ex}$ relative to the rocket. We also assume a constant
gravitational acceleration throughout the flight. Mass is ejected at a constant rate of $m_0/\tau$. We want to
find the height of the rocket as a function of time.

For an object experiencing an external force the equation of motion is (from above) $F^{ext}=\dot{p}$. Any
internal forces, like that from the exhaust pushing on the rocket, can be ignored from Newton's Third Law. Now
for the heuristic trick to make this super easy. With $p=mv$

$$
\dot{p} = \dot{m}v + m\dot{v} = F^{ext}
$$

The first term in the middle can be read "the little bit of ejected mass times its velocity (which relative
to the rocket is always $v_{ex}$) plus the mass of the rocket times its change in velocity is due to the external
force (which is gravity)." In the end the result will look like

$$
\dot{m}v_{ex} + m\dot{v} = -mg
$$
$$
\frac{dv}{dt} = -g - \frac{(m_0/\tau) v_{ex}}{m}
$$

And the last important note is that the mass itself is a function of time with $m(t)=m_0-m_0/\tau t$. This is
then a relatively simple first-order ODE (I can never remember how to solve these things) which can be
integrated twice to find the height as a function of time.

Now this method yields the same result as what Taylor does in Chapter 3 of _Classical Mechanics_. I show the
steps here briefly. Starting with $\frac{dP}{dt}=F^{ext}$ we can determine the slight change in the rocket's
momentum by $dP = P(t + dt) - P(t) = (m + dm)(v + dv) - dm (v - v_{ex}) - m v$

$$
dP = m dv + dm v_{ex}
$$
$$
\frac{dP}{dt} = m \frac{dv}{dt} + (m_0/\tau) v_{ex} = -m g
$$

Which is the same result as above. Maybe this way of deriving the simple rocket equation is more straightforward
but the heuristic trick above has always made more sense in my head when reasoning about this equation and
related problems. Maybe it will help your thinking about the result, too.
