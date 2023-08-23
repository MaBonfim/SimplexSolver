# SimplexSolver
Program to solve linear programming problems using the simplex method 

# How to use
The problem must be modelled to the standard format

The program accept as parameters the standard format of the problem in the matrix form

The parameters are separated by parts of the model

example:

 C = (-3, -2, 0, 0, 0)

 A = ((0.5, 0.3, 1, 0, 0),
      (0.1, 0.2, 0, 1, 0),
      (0.4, 0.5, 0, 0, 1))

 b = ((3), (1), (3))

 B0 = [3, 4, 5]
 N = [1, 2]

 nVariables = 5
 
 nRestrictions = 3

 - C : is the vector with the coeficients of the variables of the function
 - A : is the matrix of the coeficients of the restrictions of the problem
 - b : is the vector with the result of the restrictions
 - B0: is a vector with the index of the variables that are used for the first identit matrix
 - N : is a vector with the index of the remaining variables
 - nVariables: is the lenght of the vector C
 - nRestrictions: is the number of lines of the matrix A

