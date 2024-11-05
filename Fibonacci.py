iteraciones = 20
i = 0
previous_number = 0
current_number = 1
buffer = 0
Fibonacci_str = str(previous_number) + ' ' + str(current_number)
while i < iteraciones:
    buffer = current_number
    current_number = previous_number + current_number
    previous_number = buffer
    Fibonacci_str += ' ' + str(current_number)
    i += 1

print(Fibonacci_str)