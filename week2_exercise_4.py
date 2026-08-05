def string_frac(in_string):
    """Change user input string (including fractions) to float"""
    if "/" in in_string:
        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans = n / d
        return ans
    else:
        ans = float(in_string)
        return ans
    
# One-step multiplication
def one_step_multi():
    # Uses string_frac()
    import random
    a = random.randint(1, 11)
    b = random.randint(2, 24)
    print(a, "x = ", b)
    ans_in = (input("x = "))
    answer = b / a

    # Testing
    if string_frac(ans_in) == answer:
        print("Correct! \n")
    else:
        print("Try again")
        print(f"The correct answer is {answer}. \n")

# Simple one-step addtion
def one_step_add():
    import random
    a = random.randint(-4, 10)
    b = random.randint(2, 24)
    print(f"x + {a} = {b}")
    ans = float(input("x = "))
    answer = b - a

    # Testing
    if ans == answer:
        print("Correct! \n")
    else:
        print("Try again")
        print(f"The correct answer is {answer}. \n")

# Simple one step addition with negative number
def one_step_sub():
    import random
    a = random.randint(-19, -1)
    b = random.randint(2, 24)
    print(f"{a} + x = {b}")
    ans = float(input("x = "))
    answer = b - a

    # Testing
    if ans == answer:
        print("Correct! \n")
    else:
        print("Try again")
        print(f"The correct answer is {answer}. \n")

one_step_multi()
one_step_add()
one_step_sub()