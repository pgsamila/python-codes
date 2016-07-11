from __future__ import print_function
# strings = ['I', 'am', 'the', 'laziest', 'person', 'in', 'the', 'world' ]
# s = ''
# for a in strings:
#     s = s + a + ' '
# print s
#
#
# l = range(5)
# print l
# print l[2:4]
# print l[2:]
# print l[:4]
# print l[:]
#
#
# first = raw_input()
# second = raw_input()
#
# print('Hello '+first+' you just delved into python.')



# while True:
#     value = raw_input('Enter a value: ')
#     value = value.strip()
#     if value == 'quit': break

import sys

# N = int(raw_input().strip())
#
# if N % 2 == 0:
#  if ((N > 2) & (N < 5)):
#   print('Not Weird')
#  elif((N > 6) & (N < 20)):
#   print('Weird')
#  elif (N > 20):
#   print('Not Weird')
# else:
#         print('Weird')


#
# num1 = raw_input()
# num2 = raw_input()
#
# add = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
#
# print(add)
# print(sub)
# print(mul)

# num1 = int(raw_input().strip())
# num2 = int(raw_input().strip())
#
# div = num1 // num2
# div2 = num1/num2
#
# print(div)
# print(div2)
# N = int(raw_input().strip())
# l = range(1,N+1)
# l[1:N+1]
# result = list(map(int,l))
# ans = ' '.join(result)
# print(ans)

# import sys
# N = raw_input()
# L = []
# L.append(N)
#
# command = []
# command.append(raw_input())

# arr = []
# for i in range(int(raw_input())):
#     s = raw_input().split()
#     for i in range(1, len(s)):
#         s[i] = int(s[i])
#
#     if s[0] == "append":
#         arr.append(s[1])
#     elif s[0] == "extend":
#         arr.extend(s[1:])
#     elif s[0] == "insert":
#         arr.insert(s[1], s[2])
#     elif s[0] == "remove":
#         arr.remove(s[1])
#     elif s[0] == "pop":
#         arr.pop()
#     elif s[0] == "index":
#         print
#         arr.index(s[1])
#     elif s[0] == "count":
#         print
#         arr.count(s[1])
#     elif s[0] == "sort":
#         arr.sort()
#     elif s[0] == "reverse":
#         arr.reverse()
#     elif s[0] == "print":
#         print(arr)


#get inputs in seperate lines
# arr = []
# for i in range(int(raw_input())):
#  s = raw_input().split()
 #print(len(s))

for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    for i in range(1, i):
        print(i, end='')





