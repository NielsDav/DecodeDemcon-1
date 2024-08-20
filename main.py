# Demcon decode challenge 1 - even Fibonacci numbers
# Author: NDV

# Variables
t = 100000            # Max number of iterations to fill the fibonacci sequence with
fib = [1,2]        # Create start of list to fill with fibonacci numbers
fib_even = []
fib_even_sum = 0

# Functions

def CalculateEvenFib():
    for i in range(int(t - 2)):
        s = fib[i]+fib[i+1]
        if(s < 4e6):
            fib.append(s)
            if(s % 2 == 0):
                fib_even.append(s)
        else:
            # print('breaking off, next fibonacci number is greater than ' + str(int(4e6)))
            break


def SummationFib():
    global fib_even_sum
    for i in range(len(fib_even)):
        fib_even_sum = fib_even_sum + fib_even[i]


# Calculate results
CalculateEvenFib()
SummationFib()

# Display results
print('Sum of even fibonacci numbers until 4e6 is:')
print(fib_even_sum)