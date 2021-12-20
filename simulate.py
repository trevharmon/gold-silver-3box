#!/usr/bin/env python

import random
import time

tests = 1000000
boxes = [[ 'G', 'G' ],
         [ 'G', 'S' ],
         [ 'S', 'S' ]]
draws = [[[ 0, 0 ], [ 0, 0 ], [ 0, 0 ]],
         [[ 0, 0 ], [ 0, 0 ], [ 0, 0 ]]]
total_gold_1 = 0
total_gold_2 = 0

print('Running %d tests.'%(tests))
random.seed(int(time.time()))
for i in range(tests):
    box = random.randint(0,2)
    ball = random.randint(0,1)
    draws[0][box][ball] = draws[0][box][ball] + 1
    if boxes[box][ball] is 'G':
        total_gold_1 = total_gold_1 + 1
        ball = (ball + 1) % 2
        draws[1][box][ball] = draws[1][box][ball] + 1
        if boxes[box][ball] is 'G':
          total_gold_2 = total_gold_2 + 1

print('Draws:')
print('- Box 1 [G, G]:')
print('    Gold1 -> Gold2: %d'%(draws[0][0][0]))
print('    Gold2 -> Gold1: %d'%(draws[0][0][1]))
print('- Box 2 [G, S]:')
print('    Gold -> Silver: %d'%(draws[0][1][0]))
print('    Silver:         %d'%(draws[0][1][1]))
print('- Box 3 [S, S]:')
print('    Silver1:        %d'%(draws[0][2][0]))
print('    Silver2:        %d'%(draws[0][2][1]))
print('')
print('Gold on 1st draw:  %d'%(total_gold_1))
print('Gold on 2nd draw:  %d'%(total_gold_2))
print('Percent two golds: %.2f%%'%(float(total_gold_2) / float(total_gold_1)))
