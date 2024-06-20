#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
  '''Creates a list of lists of integers representing
  the Pascal's triangle of a given integer.
  '''
  if n <= 0:
    return []
  ans = [[1]]
  for i in range(1, n):
    ans.append([1])
    for j in range(len(ans[-2])-1):
      ans[-1].append(ans[-2][j] + ans[-2][(j+1)%len(ans[-2])])
    ans[-1].append(1)
  return ans
print(pascal_triangle(5))
