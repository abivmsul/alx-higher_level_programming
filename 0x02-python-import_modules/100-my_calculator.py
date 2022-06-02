#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import a
    if len(a.argv)-1 != 3 :
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        a.exit(1)
    operator = {'+': addition, "-": subtruction, "*": multiplication, "/": division}
    if a.argv[2] not in list(operator.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        a.exit(1)
    a = int(a.argv[1])
    b = int(a.argv[3])
    print("{} {} {} = {}".format(a, a.argv[2], b, ops[a.argv[2]](a, b)))
