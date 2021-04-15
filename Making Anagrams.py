Given two strings,  and , that may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

Sample Input
cde
abc
Sample Output

4
Explanation

Delete the following characters from our two strings to turn them into anagrams:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
 characters have to be deleted to make both strings anagrams.
  
  #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def number_needed(a, b):
    count = 0
    for i in range(97, 123):
        ia = a.count(chr(i))
        ib = b.count(chr(i))
        count += abs(ia-ib)
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = number_needed(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
