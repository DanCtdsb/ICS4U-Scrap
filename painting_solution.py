
class solution():
    def painting_problem(A, B, X, Y):
        return  2 * min((A + X) + max(B, Y), (B + Y) + max(A, X))
def main():
    print(solution.painting_problem(1, 2, 3, 1))
main()