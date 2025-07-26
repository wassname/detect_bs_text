---
title:  Predictable Numbers
url: 
novelty: 0.5
date: 2100-01-01
---
0
2
2
4
6
10
16
26
42
68
10
78
88
66
54
20
74
94
68
62
30
92
22
14
36
50
86
36
22
58
80
38
18
56
74
30
4
34
38
72
10
82
92
74
66
40
6
46
52
98
50
48
98
46
44
90
34
24
58
82
40
22
62
84
46
30
76
6
82
88
70
58
28
86
14
0
14
14
28
42
70
12
82
94
76
70
46
16
62
78
40
18
58
76
34
10
44
54
98
52

These numbers were generated with the following code:

def fibonacci(n):
    a = 0
    b = 1

    # Check if n is less than 0
    if n < 0:
        print("Incorrect input")

    # Check if n is equal to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

print(np.array([fibonacci(i) for i in range(100)]) * 2 % 100)
