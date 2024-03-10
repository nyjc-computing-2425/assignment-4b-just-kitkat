stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
# Validation of rules 1 and 2
valid = True
for char in stdform:
    if char not in "0123456789Ex.-^":
        valid = False
if stdform.count(".") > 1 or stdform.count("x") > 1 or stdform.count("^") > 1:
    valid = False

if valid:
    mantissa, exponent = stdform.split("x10^")
    # Validation of rule 3
    if exponent[0] == "-":
        new_exp = exponent[1:]
    else:
        new_exp = exponent
    if not new_exp.isdigit():
        valid = False
    else:
        print("This number in E notation is {}E{}.".format(mantissa, exponent))
if not valid:
    print("Error converting to scientific E notation.")