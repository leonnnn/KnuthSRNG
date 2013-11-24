#!/usr/bin/python3

""" An implementation of Donald E. Knuth’s “‘Super-random’
    number generator” given as an educational example of a bad
    pseudo random number generator in chapter 3.1 of his “The Art of
    Computer programming” series of books.

    The input value 6065038420 is a fixed point of the algorithm. For
    other input values, the algorithm has a cycle length of around 3000,
    making it a pretty pad random number generator.

    Knuth summarized these properties by concluding “The moral of this
    story is that random numbers should not be generated with a method
    chosen at random. Some theory should be used.”
"""

import sys

class KnuthSRNG:
    def __init__(self, seed, verbose=False):
        self.steps = [self.K3, self.K4, self.K5, self.K6, self.K7, self.K8,
                self.K9, self.K10, self.K11, self.K12]

        self.X = int(seed)
        self.verbose = verbose

    def __iter__(self):
        while True:
            self.Y = int(self.X/10**9)
            self.next_step = self.K2
            while self.next_step is not None:
                self.next_step()

            yield self.X

    def K2(self):
        self.Z = int(self.X/10**8) % 10
        
        self.next_step = self.steps[self.Z]

    def K3(self):
        if self.X < 5000000000:
            self.X += 5000000000

        self.next_step = self.K4

    def K4(self):
        self.X = int(self.X**2 / 10**5) % 10**10

        self.next_step = self.K5

    def K5(self):
        self.X = (self.X * 1001001001) % 10**10

        self.next_step = self.K6

    def K6(self):
        if self.X < 100000000:
            self.X = self.X + 9814055677
        else:
            self.X = 10**10 - self.X

        self.next_step = self.K7

    def K7(self):
        self.X = 10**5 * (self.X % 10**5) + int(self.X/10**5)

        self.next_step = self.K8

    def K8(self):
        self.K5()

        self.next_step = self.K9

    def K9(self):
        str_ = ""
        for x in str(self.X):
            y = int(x)
            str_ += str(y-1) if y>0 else "0"

        self.X = int(str_)

        self.next_step = self.K10

    def K10(self):
        if self.X < 10**5:
            self.X = self.X*self.X + 99999
        else:
            self.X -= 99999

        self.next_step = self.K11

    def K11(self):
        if self.X < 10**9:
            self.X *= 10
            self.next_step = self.K11
        else:
            self.next_step = self.K12


    def K12(self):
        self.X = int(self.X*(self.X-1)/10**5) % 10**10

        self.next_step = self.K13

    def K13(self):
        if self.Y > 0:
            self.Y -= 1
            self.next_step = self.K2
        else:
            self.next_step = None


seed = sys.argv[1]

a = iter(KnuthSRNG(seed))
values = set()
prev = 0
for i in range(100000):
    val = next(a)
    if val == prev:
        print("converged after {} iterations!".format(i))
        print(val)
        break
    if val in values:
        print("cycle after {} iterations!".format(i))
        print(prev)
        break
    
    values.add(val)
    prev = val

