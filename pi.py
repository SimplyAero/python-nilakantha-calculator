import decimal


def main():
    # Asking for the number of digits the user wants to find
    # WARNING: this algorithm's complexity is O(n!)
    digits = input('Write the number of decimal digits you want to find: ')
    # Testing if the input is an actual number and asking for a new one if
    # necessary
    correct = False
    while not correct:
        try:
            digits = int(digits)
            correct = True
        except ValueError:
            digits = input("invalid value, write a number: ")
    # Setting the decimal precision to twice the needed one, in order to avoid
    # rounding issues
    context = decimal.getcontext()
    context.prec = digits * 2
    #starting to calculate pi
    pi = decimal.Decimal(3)
    latest_digit_index = 0
    latest_digit = -1
    iteration = 1
    print('3.', end='')
    while latest_digit_index < digits:
        # Applying Nilakantha's Series
        sign = (-1) ** (iteration + 1)
        first = iteration * 2
        divisor = decimal.Decimal(first * (first + 1) * (first + 2))
        pi += (sign * (4 / divisor))
        pi_string = str(pi)[2:]
        # Checking if the new digit has stabilized, going to the next one if it
        # has, reiterating the same position if it hasn't
        if int(pi_string[latest_digit_index]) == latest_digit:
            print(pi_string[latest_digit_index], end='')
            latest_digit_index += 1
            latest_digit = -1
        else:
            latest_digit = int(pi_string[latest_digit_index])
        iteration += 1
    print()


if __name__ == '__main__':
    main()