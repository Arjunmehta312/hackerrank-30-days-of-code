#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -math.inf  # Initialize to a very low number to handle negative values

    for i in range(4):
        for j in range(4):
            # Calculate the sum of the hourglass starting at arr[i][j]
            hourglass_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )
            # Update max_sum if the current hourglass_sum is greater
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum

    print(max_sum)
