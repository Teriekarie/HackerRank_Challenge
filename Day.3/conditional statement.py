#!/bin/python3
# python program for conditional statements

# system to input an integer
N = int(input())

#if N is odd print weird
if N % 2 != 0:
    print("Weird")
else:
    if N <= 5:
        print("Not Weird")  # If N is even and in the inclusive range of 2 to 5, print Not Weird
    elif N <= 20:
        print("Weird")      #If N is even and in the inclusive range of 6 to 20, print Weird
    else:
        print("Not Weird")  #If  is even and greater than 20, print Not Weird
