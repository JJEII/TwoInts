# TwoInts

This is one of the most unusual logic puzzles I've ever encountered, and I'm a life-long "puzzler" (of all sorts).

```
There are two integers, A and B, greater than 1.
Mathematician S knows their sum.
Mathematician P knows their product.
(Neither is respectively told anything more than the above.)
The following conversation takes place.

   S says to P: You don't know A and B.
   P says to S: Now I do.
   S says to P: Now I do, too.

What are the values of A and B (that result in the smallest possible sum)?
```

There's no wording trickery here, or anything like that. (E.g., "you don't know A and B" means "you don't know what the values of A and B are.")

## Context

I first encountered this puzzle decades ago, and I worked through it by hand (which is quite doable), to find a solution that meets the criteria stated. (I added the parentheticals in it, for clarification and solution uniqueness.)

But, then I started wondering if there were more solutions that fit the criteria---minus the "smallest possible sum" constraint, of course. So, I decided to write programs to help me explore this, and I managed to generate quite a few other solutions, even many years ago. These solutions exhibit some rather unusual/unexpected properties that hold almost, but not quite, always. These features have intrigued me. So, I've returned to the problem from time to time, to tinker with and generate more solutions, especially as hardware has gotten faster.

In late July, 2026, I returned to it yet again, but this time with a much more serious intent to write a highly performant program to (hopefully) generate many more solutions.

I massively succeeded in this effort.

I was able to explore number spaces orders of magnitude larger than I had done previously, thanks to a combination of new strategies, from choosing a fast programming language to implementing some fancy programming techniques to noting and leveraging mathematical properties that I hadn't used before. I have now generated more than ten thousand _solutions_ to the problem.

## Challenge

I am including here a very naïve program, written in Python, to explore this problem's solution space. But, it won't get you very far because it rapidly slows to a computational crawl. (In its current form, it only generates 3 solutions.) It would probably take years to do what my recent program does in a matter of seconds. Can you do something similar? Better?

I suggest solving the problem by hand first, to get a bit of a feel for it.
