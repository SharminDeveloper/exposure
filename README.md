It's a leet code project fully written in python.

You should give it lists in this way to make a rectangle with numbers 1 or 2.
Example:
[
    [1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0],
]

It starts from around the rectangle and each 1 around the rectangle can keep every 1 that is above,below,in the left and in the right of it, and the kept 1s can do the same to other 1s and so on. At the end, all 1s that are not kept will be removed.
So we will have: 
[  
    [1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0],
]