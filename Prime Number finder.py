#Mitchell Young, with bugfixing help by Joseph Grassi
import math as ma
print 'Welcome to the prime number finder!  To start, input two positive numbers.  We will return any prime numbers between (and including) the range.'

x1=int(raw_input('Smallest number to check:'))
x2=int(raw_input('Largest number to check:'))

#defining final print group
primes=[]

#defining low/high values
low=x1
high=x2
#BUGFIX: print type(primes)
#loop statement
for dividend in range(low,high):
    for divisor in range(2,int(ma.ceil(ma.sqrt(dividend)+1))):
        if dividend%divisor ==0:
            break
        elif divisor==int(ma.ceil(ma.sqrt(dividend))):
            #BUGFIX: print "got to line 22"
            primes.append(int(dividend))
if x1>=x2:
    print "Max value must be larger than min value."
else:
    if len(primes)==0:
        print "No Primes Found"
    else:
        print primes
        print "There are",len(primes),"primes between", x1,"and", x2


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
 and dividend=dividend+1
"""
