# GuideBook-Backend-Challenge

Problem Statement: 
We have a list of ordered integers (ex: [1, 3, 7, 8, 9, 10, 11]). Suppose we slice into that list at a random index and append the "top" half of list to the "bottom" (maintaining the order of both halves while doing so).

Challenge: Write a function that returns the largest integer in the "shifted" list.

Solution:
The "search" function in Challenge.py takes a circularly rotated array as an argument and returns the maximum integer value found.
The function is a modified binary search algorithm to give a performance of O(logN).
