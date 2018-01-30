#Logic to solving problem:
#input two numbers, check each interger between x1 and x2 to see if they are devisable by any numbers between 2 and sqrt(x2)
import math as ma
print 'Welcome to the prime number finder!  To start, input two positive numbers.  We will return any prime numbers between  (and including) the range.'

x1=raw_input('Smallest number to check:')
x2=raw_input('Largest number to check:')

#defining final print group
primes=[]

#defining dividend/divisor and low/high values
divisor=2
dividend=x1

low=x1
high=x2

#loop statement
for dividend in range(low,high):
    for divisor in range(2,int(ma.sqrt(max)+1)):
        if dividend%divisor ==0:
            dividend=dividend+1
        elif divisor==int(ma.sqrt(max)+1
            primes=primes+dividend and dividend=dividend+1
        else divisor=divisor+1 and dividend=dividend+1


"""    if x1%x=0
        if x1=high:
            break
        else:
            x1=x1+1
    elif x=int.ma.sqrt(high)+1:
        if x1=high:
            primes=primes+x1, break
        else:
            x=x+1
"""

print primes
