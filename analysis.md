
What is the algorithm I used ?
------------------------------

Constructed a minimum cost matrix in bottom up manner and found out the least
cost path.

A cost matrix (2D) is constructed in which *(i, j)* index has the least cost to
reach *(i, j)* in the hex grid from top left (considering that we can only move
bottom or right). Therefore, the bottom right *(m, n)* index will have the least
cost path to reach *(m, n)* in our hex grid.

There is only 1 possible way of traversing the 1st column and 1st row: either
move right *(in case of 1st row)* or go down *(in case of 1st column)*. Hence,
the first row and column are initialized by the cost of making these moves.
This acts as the base for building the cost matrix for rest of the elements.

Now, to build the cost matrix for rest of the elements, we check the minimum
of the cost when we approach from top or left and sum it with the current index.
Thus, building this cost matrix for all the elements.

Once we have the cost matrix, we just need to do backtrack from *(m, n)* in this
matrix and check which all elements in the hex grid contributed in the least
cost path.

Why did I decide to use it ?
----------------------------

At first glance of this problem, it seemed to be a graph traversal task
with minimum cost. But, as the movements are constrained and current state depends
on 2 directions we can look for a simpler solution using DP.

An easy way to do this was to create a top down recursive method.
The cost to reach *(m, n)* will be the minimum of the cost to reach on its
top element: *(m-1, n)* or its left: *(m, n-1)* plus the cost of current index.

This way, we can make a recursion call stack which isn't evaluated until we
reach our base case i.e. the case for which we know the result which will be the
top left element of our grid.

Once, we reach the base case all the possible moves are evaluated from the call
stack and in the end we get the cost matrix.

The problem with this approach is that there are a lot of subproblems which are
computed again and again. As we are building our cost matrix top down maintaining
a call stack, there are lot of subproblems / function calls which are repeated
which is redundant. Therefore, I went with a bottom up approach mentioned above.

Analyzing the space and time complexity
---------------------------------------

The time complexity for the solution will be O(m*n)
The most expensive computation is the building of the cost matrix which contributes
to this complexity

The space complexity for the solution will be O(m*n)
Extra space for creating a cost matrix is used (same as size of hex grid) and
thus, the space complexity

result: r, r, d, d, r, d, d, r, r, d

