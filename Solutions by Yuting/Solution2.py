'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
def factorial_calculator(n: int) -> str:
    # By mathematical definition, 0! (zero factorial) is equal to 1.
    # This is a standard convention used in combinatorics and algebra.
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return str(ans)

if __name__ == '__main__':
    sample_input = 8
    sample_result = factorial_calculator(sample_input)
    print(sample_result)