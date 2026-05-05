from sympy import *

# dynamic symbols
def get_symbols(expr):
    return list(sympify(expr).free_symbols)

def solve_equation(eq):
    expr = sympify(eq)
    vars = list(expr.free_symbols)
    return solve(expr, vars)

def solve_system(equations):
    eqs = [sympify(eq) for eq in equations if eq.strip() != ""]
    vars = set()
    for eq in eqs:
        vars.update(eq.free_symbols)
    return solve(eqs, list(vars))

def derivative(expr):
    vars = get_symbols(expr)
    if vars:
        return diff(sympify(expr), vars[0])
    return "No variable found"

def integral(expr):
    vars = get_symbols(expr)
    if vars:
        return integrate(sympify(expr), vars[0])
    return "No variable found"

def simplify_expr(expr):
    return simplify(sympify(expr))