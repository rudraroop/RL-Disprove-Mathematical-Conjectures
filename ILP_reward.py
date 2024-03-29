import cplex
from cplex import Cplex

def reward(n, edgeList):
    c = cplex.Cplex()
    c.objective.set_sense(c.objective.sense.maximize)
    c.set_problem_name("BinaryIntegerLinearProgram")
    t = c.variables.type

    var_names = ["x" + str(i) for i in range(n)]
    types = [t.binary] * n
    
    indices = c.variables.add(names = var_names, lb = [0] * n, ub = [1] * n, types = types)

    c.objective.set_linear([(name, 1.0) for name in var_names])

    for i, j in edgeList:
        c.linear_constraints.add(
            lin_expr = [cplex.SparsePair(ind = [var_names[i], var_names[j]], val = [1.0, 1.0])],
            senses = ["L"],
            rhs = [1.0]
        )

#     print("Names of variables = ", c.variables.get_names())
#     print("Number of variables = ", c.variables.get_num())

    c.solve()

    print("Solution status =", c.solution.get_status(), ":", c.solution.status[c.solution.get_status()])
    print("Solution value  =", c.solution.get_objective_value())
    for name in var_names:
        print(name, "=", c.solution.get_values(name))


n = 5 
edgeList = [(0, 1), (4, 2), (0, 3), (3, 4)]  
reward(n, edgeList)