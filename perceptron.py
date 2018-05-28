import numpy as np
import matplotlib.pyplot as plt

#AND Gate
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b

    # b + x1w1 + x2w2 = tmp
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

#NAND Gate
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

#OR Gate
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

#XOR Gate
def XOR(x1, x2):
    y1 = NAND(x1, x2)
    y2 = OR(x1, x2)
    
    return AND(y1, y2)

print("== AND 구현 결과 ==")
print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))

print("== NAND 구현 결과 ==")
print(NAND(0, 0))
print(NAND(1, 0))
print(NAND(0, 1))
print(NAND(1, 1))

print("== OR 구현 결과 ==")
print(OR(0, 0))
print(OR(1, 0))
print(OR(0, 1))
print(OR(1, 1))

print("== XOR 구현 결과 ==")
print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))