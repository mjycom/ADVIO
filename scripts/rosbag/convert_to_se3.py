import sys, os

from klampt.math import so3
import numpy as np

"""
in_fn = sys.argv[1]
out_fn = sys.argv[2]

in_data = []
with open(in_fn) as fptr:
    for line in fptr:
        entries = map(float, line.split(','))
        in_data.append(entries)

out_data = []
for i in range(len(in_data)):
    t = in_data[1: 4]
    A = in_data[4: 8]
    B = so3.from_quaternion(A) # [a11, a21, a31, ...]
    C = so3.matrix(B)

    T = np.eye(4)
    T[:3, :3] = C
    T[:3, 3] = t
    out_data.append(list(T[0]) + list(T[1]) + list(T[2]) + list(T[3]))

"""

TT = [0.492127,0.003738762,0.08270439,-0.02360799,0.7022632,-0.3517123,-0.5801101,-0.2158636] # from advio-04 
TT = [0.514813,-0.005759389,-0.09049783,-0.001374606,0.64807,-0.264358,0.6264483,0.343049] # a complete line from advio-23

A = TT[4: 8]

B = so3.from_quaternion(A)
print(B)

C = so3.matrix(B)
print(C)

t = TT[1: 4]

T = np.eye(4)
T[:3, :3] = C
T[:3, 3] = t

print(T)
print([list(T[0]), list(T[1]), list(T[2]), list(T[3])])
print(np.array([list(T[0]), list(T[1]), list(T[2]), list(T[3])]))
print(list(T[0]) + list(T[1]) + list(T[2]) + list(T[3]))
print(list(T[0]) + list(T[1]) + list(T[2]))
#"""
