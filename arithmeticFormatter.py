def arithmetic_arranger(problems, show_answer=False):

    # Check if the number of equations is greater than five
    number_of_equations = 0

    for _ in problems:
        number_of_equations += 1

        if number_of_equations > 5:
            arranged_problems = 'Error: Too many problems.'
            return arranged_problems

    first_line = ""
    second_line = ""
    dashes = ""
    result = ""

    for problem in problems:

        first_addend = ""
        second_addend = ""
        operator = ""
        sum = 0
        switch = False

        for digit in problem:

            # Check if there are non-digits in the number
            if not digit.isdigit() and digit not in ['+','-',' ','*','/']:
                arranged_problems = 'Error: Numbers must only contain digits.'
                return arranged_problems
            
            # Check if there are forviden operators
            if digit in ['*','/']:
                arranged_problems = "Error: Operator must be '+' or '-'."
                return arranged_problems
            
            # Assing the operator
            if digit in ['+','-']:
                operator = digit
                switch = True
                continue

            # Switching between lines
            if not switch:
                first_addend += digit
            if switch:
                second_addend += digit
        
        # Cleaning the addends so they only contein numbers (no spaces)
        first_addend = first_addend.strip()
        second_addend = second_addend.strip()

        # Checking the length of the numbers
        if len(first_addend) > 4 or len(second_addend) > 4:
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
            return arranged_problems

        # Computing the sum and converting it to a string
        if operator == "+":
            sum = str(int(first_addend) + int(second_addend))
        if operator == "-":
            sum = str(int(first_addend) - int(second_addend))
        
        # Creating the lines
        first_line += " " * (2 + max(len(first_addend), len(second_addend)) - len(first_addend)) + first_addend + " " * 4
        second_line += operator + " " * (1 + max(len(first_addend), len(second_addend)) - len(second_addend)) + second_addend + " " * 4
        dashes += "-" * (2 + max(len(first_addend), len(second_addend))) + " " * 4
        result += " " * (2 + max(len(first_addend), len(second_addend)) - len(sum)) + sum + " " * 4

    # Removing the extra spaces at the end of the lines
    first_line = first_line[0:-4]
    second_line = second_line[0:-4]
    dashes = dashes[0:-4]
    result = result[0:-4]

    # Creating the output
    if show_answer:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes + "\n" + result
    if not show_answer:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes

    return arranged_problems

        

def main():
    print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"], True)}')
    print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"], True)}')
    print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True)}')
    print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], True)}')
    print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], True)}')
    print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"], True)}')
    print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"], True)}')
    print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"], True)}')
    print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
    print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')

main()