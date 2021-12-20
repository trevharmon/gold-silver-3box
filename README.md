# gold-silver-3box

This is in response to a tweet sent out by Sean Silverman
([@BarExamTutor](https://twitter.com/BarExamTutor)).
https://twitter.com/BarExamTutor/status/1472746730017939457
> Kind of reminds me of that old “Monte Hall” problem (with the goats and car).
> But far as I can tell, the answer to this one has got to be 2/3.


The description of the problem posed is as follows:
> There are 3 boxes. Each box contains 2 balls. One box contains 2 gold balls,
> another box contains 2 silver balls, and the final box contains one gold ball
> and one silver ball.
> You pick box at random. You put your hand in and take a ball from that box at
> random. It's a gold ball. What is the probability that the next ball you take
> from the same box will also be gold?
> Note: You can't see into any of the boxes

A discussion went back and forth as to whether the answer is 2/3 or 1/2, as
well as whether or not the [Monty Hall
problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) applied. I got
curious so I wrote a simulator to test out the question.

The result: **2/3 is the correct answer**

Here are some of the outputs of the simulation script:

Run #1
```
Running 1000000 tests.
Draws:
- Box 1 [G, G]:
    Gold1 -> Gold2: 166689
    Gold2 -> Gold1: 166270
- Box 2 [G, S]:
    Gold -> Silver: 166918
    Silver:         166526
- Box 3 [S, S]:
    Silver1:        166744
    Silver2:        166853

Gold on 1st draw:  499877
Gold on 2nd draw:  332959
Percent two golds: 0.67%
```

Run #2
```
Running 1000000 tests.
Draws:
- Box 1 [G, G]:
    Gold1 -> Gold2: 166932
    Gold2 -> Gold1: 166543
- Box 2 [G, S]:
    Gold -> Silver: 166517
    Silver:         167134
- Box 3 [S, S]:
    Silver1:        166300
    Silver2:        166574

Gold on 1st draw:  499992
Gold on 2nd draw:  333475
Percent two golds: 0.67%
```

Run #3
```
Running 1000000 tests.
Draws:
- Box 1 [G, G]:
    Gold1 -> Gold2: 166530
    Gold2 -> Gold1: 166977
- Box 2 [G, S]:
    Gold -> Silver: 166325
    Silver:         167458
- Box 3 [S, S]:
    Silver1:        166683
    Silver2:        166027

Gold on 1st draw:  499832
Gold on 2nd draw:  333507
Percent two golds: 0.67%
```
