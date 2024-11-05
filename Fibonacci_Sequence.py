# Creating Fibonacci Sequence Sequence

def generate_fibonacci(n):
    #creating my range to count
    fibonacci_sequence = [0,1]
    for i in range(2,n):
        #calling the sequence in a formula
        fibonacci_sequence.append(fibonacci_sequence[i-1]+fibonacci_sequence[i-2])
        #returning the values of the sequence or calculating the result
        return fibonacci_sequence


#call the function
n = 10
fibonacci_sequence