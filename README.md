‘Super-random’ number generator
===============================

An implementation of Donald E. Knuth’s “‘Super-random’
number generator” given as an educational example of a bad
pseudo random number generator in chapter 3.1 of his “The Art of
Computer programming” series of books.

The input value 6065038420 is a fixed point of the algorithm. For
other input values, the algorithm has a cycle length of around 3000,
making it a pretty bad random number generator.

Knuth summarized these properties by concluding “The moral of this
story is that random numbers should not be generated with a method
chosen at random. Some theory should be used.”

