
from typing import Tuple

def fac(n: int):
    """
    Alternate recursive soln (but O(N) mem space for recursive call stack)
    def fac(n):
        if n==1:
            return 1
        return n*fac(n-1)

    iterative soln is space efficient:
    """
    fac=1
    for num in range(1, n+1): fac*=num
    return fac

def permutation(n: int, k: int):
    """
    permutation = nCk*k! 
    nCk = n!/(k!*(n-k)!)
    thus, post simplification => nCk*k! = n!/(n-k)! 
    Also known as nPk = n!/(n-k)!
    """
    return fac(n)/fac(n-k)

def all_tool_permutations(max_total_tools: int, max_chosen_tools: int):
    all_permutations=0
    for chosen_tools in range(1, max_chosen_tools+1):
        all_permutations+=permutation(max_total_tools, chosen_tools)
    return all_permutations


def total_candidate_solutions(p: Tuple[int, int], ds: Tuple[int, int], a: Tuple[int, int]):
    return all_tool_permutations(p[0], p[1]) + all_tool_permutations(ds[0], ds[1]) + all_tool_permutations(a[0], a[1])

p=(10, 10)
ds=(10, 10)
a=(20, 20)

p=(10, 2)
ds=(10, 2)
a=(20, 2)
print(total_candidate_solutions(p, ds, a))