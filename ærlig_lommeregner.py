# Messages
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

# Stores previous calculations
memory = 0.0


def is_one_digit(v):
    output = False
    if v.is_integer() and (-10 < v < 10):
        output = True
    return output


def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and (v3 == '*'):
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 != '/'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg

    print(msg)


# Performs every kind of validations
def validate(x, oper, y):
    result = False

    try:
        # Tests if the numbers are valid
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
    else:
        # Tests if the operator is valid
        if oper not in ['+', '-', '*', '/']:
            print(msg_2)
        else:
            # Tests for laziness
            check(x, y, oper)

            # Tests for division by zero
            if oper == '/' and y == 0:
                print(msg_3)
            else:
                result = True

    return result


# Do the math
def calculate(x, oper, y):
    result = 0.0

    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/':
        result = x / y
    print(result)

    return result


# Calculates until the user say 'n'...
while True:
    # Asks for an equation
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()

    # Tests if any operand uses the memory
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    # Validates the equation informed
    if not validate(x, oper, y):
        continue

    # Does the calculation
    result = calculate(float(x), oper, float(y))

    # Repeat until the answer is 'y' or 'n'
    answer = ''
    while answer not in ['y', 'n']:
        # Asks if you want to store the result
        print(msg_4)
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                q1 = input(msg_10)
                if q1 == "y":
                    q2 = input(msg_11)
                    if q2 == "y":
                        q3 = input(msg_12)
                        if q3 == "y":
                            memory = result
            else:
                memory = result

    # Repeat until the answer is 'y' or 'n'
    answer = ''
    while answer not in ['y', 'n']:
        # Asks if you want to calculate again
        print(msg_5)
        answer = input()

    if answer == 'n':
        break
