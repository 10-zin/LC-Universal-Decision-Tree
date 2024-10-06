## Tool Types
1. pattern
2. Data Structure
3. Algorithm

## Tool Quantity
1. Number of patterns
2. Number of Data Structures
3. Number of Algorithms

Given $N_{p}$ patterns $N_{DS}$ Data Structures, and $N_{A}$ algorithms.

We have $(N_{P})$ * $(N_{DS})$ * $(N_{A})$ pool of candidate tool combinations from which one or more combinations could solve the problem.

However, this assumes all problems can be solved with only one pattern, and one data structure, and one algorithm. That is seldom true.

Many hard questions need 2-3 patterns + 2-3 data structures + 2-3 algorithms to solve the question.

Hypothtically,
The least complex problem could need 0 pattern, 0 data structure, 0 algorithm to solve it, consider -> "print hello world".

Hypothetically,
The most complex problem could need all possible patterns, all possible data structures, and all possible algorithms to solve it. 

And there could be infinite problems that require one of the tool combinations interpolated between them.

So let's calculate, the total possible candidate combinations of tools to solve any arbitrary problem.

If $N_{P} = 3$, we can then have the following candidate combinations to solve a problem.
[], [1], [2], [3], [1,2], [2,3], [1,2,3]. These are 7 possible combinations.
However, it is also possible that [2,1] is the order of patterns that help solve the problem.
Order of patterns applied can be crucial in solving problems, imagine sorting before binary search, vs sorting after binary search. Former is correct, latter has invalid condition to use binary search. Thus, we need to consider all combinations, and for each combination all permuations (all arrangements). 

Thus, the permutation and combinations for that example would have following candidates:

[], [1], [2], [3], [1,2], [2,1], [2,3], [3,2], [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]. These are 16 candidates in total!



A mathematical way to generalize this using permutation and combinatorics formulas we learn in high school math is as follows:

Given  $N_{P}$ patterns:
1. If 1 pattern can solve the problem, there are $C^{N_{P}}_{1}$ ways to select one pattern, and $1!$ ways to order them.
2. If 2 patterns can solve the problem, there are $C^{N_{P}}_{2}$ ways to select two patterns, and $2!$ ways to order them.
3. If 3 patterns can solve the problem, there are $C^{N_{P}}_{3}$ ways to select three patterns, and $3!$ ways to order them.... AND SO ON .. UNTIL..
4. If ${N_{P}-1}$ patterns can solve the problem, there are $C^{N_{P}}_{N_{P}-1}$ ways to select ${N_{P}-1}$ patterns, and $({N_{P}-1})!$ ways to order them.
5. If ${N_{P}}$ pattern can solve the problem, there are $C^{N_{P}}_{N_{P}}$ ways to select ${N_{P}}$ patterns, and $({N_{P}})!$ ways to order them.

Put compositaly, there are $\sum_{k=0}^{N_{P}} C_{k}^{N_{P}}*k!$ candidate pattern permuations out of which one or more candidate could help solve the problem.

Similarly, there are $\sum_{k=0}^{N_{DS}} C_{k}^{N_{DS}}*k!$ data structure candidate permutations and $\sum_{k=0}^{N_{A}} C_{k}^{N_{A}}*k!$ algorithm candidate permutations out of which one ore more could help solve the problem.

Now, to fully solve a problem we need arbitrary permutaions of patterns, data structure, and algorithms altogether. Thus, total possible candidate permutations/solutions are:

$ \left( \sum_{k_{P}=0}^{N_{P}} C_{k_{P}}^{N_{P}}*k_{P}! \right) * \left( \sum_{k_{DS}=0}^{N_{DS}} C_{k_{DS}}^{N_{DS}}*k_{DS}! \right) * \left( \sum_{k_{A}=0}^{N_{A}} C_{k_{A}}^{N_{A}}*k_{A}! \right)$


So, even if we consider, 10 patterns, 10 Data Structures, and 20 algorithms. This would amount to 6.$6*10^{18}$ possible candidate solutions!!! That's a lot, how do we have elite LeetCoders then?

Well.. thankfully, even the most difficult questions don't require you to use more than 2-3 patterns, 3-4 data structures, and 2-3 algorithms. Thus, a more accurate and realistic candidate solution space would around 13,920 total candidate solutions.

However, majority of the "hard" questions usually require about 2 paterns, 2 Data Structures, 2 algorithm at max.. So that would be 600 possible possible candidate solutions.

Great ! that seems small enough to handle. With enough grind, a human can easily navigate through these decision tree to highly probable leaf node solutions.
