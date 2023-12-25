'''
Run the various CSP solvers on the nQueens problem.
These calls are mostly copied/adapted from AIMA Python.

Code edited to run on python3

Acknowledgement to  main author of this script
@author: kvlinden
@version 14feb2013
'''

from csp import backtracking_search, NQueensCSP, min_conflicts, mrv, \
    forward_checking, AC3
from search import depth_first_graph_search
import logging



## 1. Set up the problem.
n_vals = [5,10,25,50,100, 200, 500, 600, 750, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 7500]
for n in n_vals:
     problem = NQueensCSP(n)
     print('n = ', n)
     solution = backtracking_search(NQueensCSP(n),select_unassigned_variable=mrv,inference=forward_checking)
## 2. Solve the problem; only keep 1 algorithm uncommented.
# solution = backtracking_search(problem, select_unassigned_variable=mrv, inference=forward_checking)
# solution = min_conflicts(problem)

## 3. Print the results.  
# print()
# # Handle AC3 solutions (boolean values) first, they behave differently.
# if type(solution) is bool:
#     if solution and problem.goal_test(problem.infer_assignment()):
#         print("AC3 Solution:")
#     else:
#         print("AC Failure:")
#     print(problem.curr_domains)

# # Handle other solutions next.
# elif problem.goal_test(solution):
#     print("Solution:")
#     print(solution)
#     # problem.display(problem.infer_assignment())
# else:
#     print("Failed - domains: " + str(problem.curr_domains))
#     problem.display(problem.infer_assignment())


