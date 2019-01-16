#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:47:43 2018

@author: shannonjin
"""

# -*- coding: utf-8 -*-

#Base case when mod returns 0
import math
import random
import sys
import pylab
from matplotlib import pyplot as plt
import matplotlib.cm as cm
# this is not needed with pylab. 
#matplotlib inline
import numpy as np

def menu():
  text=""
  
  while(text !="Q"):
      print("Please type a number in the range 1-10 to choose the function you want to play")
      print("Type Q to quit")
      print("1.Find the greatest common divisor of two numbers")
      print("2. Uses Sieve of Eratosthenes to generate primes up to a certain n ")
      print("3. Test a prime number n Trial division: For an input n, check if there is a prime number between 2 and √n that divides n")
      print("4. Test a primality or prime number n using fermat little theorem")
      print("5. Test primality of a number n using pTrialDivision")
      print("6. Test primality of number using pollard strassen")
      print("7. Call primeDistribution")
      print("8. Call twin primes to  find the number of twin primes")
      print("9. Primality test using sieve of eratosthenes")
      print("10. plot pi(x)")
      print("11. get a visualization of 1000 prime numbers")
  
      text = input("Please enter something ")  # Python 2
      
      if(text=="1"):
          a = int(input("Please enter a number "))
          b = int(input("Please enter a number "))
          print(gcd(a,b))
      elif(text=="2"):
          n=int(input("Please enter a number "))
          print(sieve(n))
      elif(text=="3"):
          n=int(input("Please enter a number "))
          print(trialDivision(n))
      elif(text=="4"):
          n=int(input("Please enter a number "))
          print(fermatLittleTheorem(n))
      elif(text=="5"):
          n=int(input("Please enter a number "))
          print(pTrialDivision(n))
      elif(text=="6"):
          n=int(input("Please enter a number "))
          print(pollardStrassen(n))
      elif(text=="7"):
          a = int(input("Please enter the last digit of the first prime "))
          b = str(input("Please enter the last digit of the second prime. Enter NA if not applicable "))
          print("The proportion "+ str(primeDistribution(a,b)))
      elif(text=="8"):
          print(twinPrimes())
      elif(text=="9"):
          n=int(input("Please enter a number "))
          print(usingSieve(n))
      elif(text=="10"):
          n=int(input("Please enter a number "))
          plotpi(n)
      elif(text=="11"):
          visualization()
      text=input("Please enter something, enter Q to quit ") 


#Problem 1. Uses Euclid's algorithim to calculate the gcd of 2 integers
def gcd(int1, int2):
    
    a=max(int1, int2)
    print("The max is"+str(a))
    b=min(int1,int2)
    print("The min is"+str(b))
    
    #print("b"+str(b))
    c=a%b
    print("Modulus of a and b is"+str(c))
    toReturn=0
    
    if b==1: #these numbers do not have a common divisor besides 1     
        print("these numbers do not have a common divisor besides 1")
        return(1)
        #print(str(b)+"a")
    elif c==0:
        #print(str(c)+"0")
        return(b)
    elif c!=0:   
        #print(str(c)+"c")
        print("perform gcd on" +str(b)+str(c))
        return(gcd(b,c))

    #print("To return"+ str(toReturn))
    #return toReturn

#Problem 2. Uses Sieve of Eratosthenes to generate primes up to a certain n
def sieve(n):

    prime=2
    nums=list(range(2,n+1))
    #print(len(nums))
    toReturn=[]
  
    
    while len(nums)>1:
        for i in nums:
            if i%prime==0:
                temp=set(nums) #python 3.6 set() should keep the order
                temp.remove(i) 
                nums=list(temp)

        prime=nums[0]
        toReturn.append(prime)
    
    return toReturn
  

#Problem 3: Primality test using
# Trial division: For an input n, check if there is a prime number between 2 and √n that divides n
def trialDivision(n):
    #For an input n, check if there is a prime number between 2 and√nthat divides n.#
    it=sieve(int(math.sqrt(n)))
    
    for i in range(2,int(math.sqrt(n))):
        if  i in it:
            if n%i==0:
                return False
    return True

#Problem 3: Primality test using Sieve of Eratosthenes.
def usingSieve(n):
    a=sieve(n)
    x=a.pop()
    if x==n:
        return True
    else:
        return False

#Problem 3: Using Fermat little theorem BONUS.
#Fermat's little theorem states that if p is a prime number
#then for any integer a, the number a^{p} − a is an integer multiple of p. 
#In the notation of modular arithmetic, this is expressed as a^p \equiv a \pmod p.
"""
// Higher value of k indicates probability of correct
// results for composite inputs become higher. For prime
// inputs, result is always correct
1)  Repeat following k times:
      a) Pick a randomly in the range [2, n - 2]
      b) If an-1 &nequiv; 1 (mod n), then return false
2) Return true [probably prime]. 
"""
def fermatLittleTheorem(n):
  a=random.randint(1,n-3) #because randInt has exclusive 
  return(a**(n-1)%n==1)
 
#Problem 4: A fast prime factorization algorithm using trial division
def pTrialDivision(n):
    
    it=sieve(int(math.sqrt(n)))
    toReturn=[]
    
    for i in range(2,int(math.sqrt(n))):
        if i in it:
            if n%i==0:
                toReturn.append(i)
    return toReturn

#Problem 4 BONUS: A fast prime factorization algorithim using Pollard-Strassen method
"""
Start with random x and c. Take y equal to x and f(x) = x2 + c.
While a divisor isn’t obtained
Update x to f(x) (modulo n) [Tortoise Move]
Update y to f(f(y)) (modulo n) [Hare Move]
Calculate GCD of |x-y| and n
If GCD is not unity
If GCD is n, repeat from step 2 with another set of x, y and c
Else GCD is our answer
"""
def pollardStrassen(n):
    x=2
    y=2
    d=1
    while d==1:
        x=(((x**(2))-1)%n)
        y=(((y**(2))-1)%n)
        y=(((y**(2))-1)%n)
        d=gcd(abs(x-y),n)
    if d==n:
       return "Failure"
    return d
    

#Problem 5: Prime distribution, calculates proportion of primes that end with 
#lastDigit and are followed by a prime that ends with nextLastDigit
def primeDistribution(lastDigit, nextLastDigit):
    
    
    #primes=sieve(10000)
    
    #If you're reading in primes from a file, uncomment this code
    
    primes=[]
    with open('primes1.txt') as f:
      next(f)
      
      for line in f:
        line=line.split()
        #print(len(line))
        for n in line:
            #print(n)
            primes.append(n)
    


 
    counter=0 ##represents number of primes that fits the condition
    
    
    for i in range(len(primes)-1):
        
        x=str(primes[i]) 
        y=str(primes[i+1])
  
        if x[len(x)-1] == str(lastDigit):   
            if nextLastDigit == "NA":    
                counter=counter+1
            elif y[len(y)-1] == str(nextLastDigit):
                counter=counter+1

          
    print("Out of "+ str(len(primes)) +' primes there are '+ str(counter) + ' that fit the specified condition')
    return(counter/float(len(primes)))

#Let (x) representing the number of primes less than x.
#Using the data you collected, plot (x).
def plotpi(x):
    
    primes=[]
    with open('primes1.txt') as f:
      next(f)
      
      for line in f:
        line=line.split()
        #print(len(line))
        for n in line:
            #print(n)
            primes.append(n)
            
    p=primes[0]
    y_values=[]
    counter=0
    
    for i in range(x):
        
      while int(p)<i:
        counter=counter+1
        p=primes[counter]
      
      #print(counter)
      y_values.append(counter)
        
    plt.plot(y_values)
    pylab.show()
    

#Used in problem 5 to find the number of twin primes
def twinPrimes():
    
    primes=[]
    with open('primes1.txt') as f:
      next(f)
      
      for line in f:
        line=line.split()
        #print(len(line))
        for n in line:
            #print(n)
            primes.append(n)
    
    counter=0
    
    for i in range(len(primes)-1):
        if (int(primes[i])+2)==int(primes[i+1]):
            counter=counter+1
    
    return counter


#6. Visualizing 1000 primes numbers
#if  
def visualization():
    
    arr=np.zeros((100, 100))
    counter=0
    
    
    for i in range(100):
        for j in range(100):
            if(trialDivision(i)):
                arr[i,j]=1
            counter=counter+1
    
    plt.matshow(arr, cmap=cm.binary)  
    #plt.matshow(arr)    
    pylab.show()



menu()

"""
What I used to test my code


print("Wow")
print(gcd(100,10))
print(gcd(4278,8602))
print(sieve(200))
print(trialDivision(100))
print(usingSieve(100))
print(pTrialDivision(100))
print(fermatLittleTheorem(11))
print(fermatLittleTheorem(2222))
print("Done")





firstParam=['1','3','7','9']
secondParam=["",'1','3','7','9']

for x in firstParam:
    for y in secondParam:
        print('Proportion of primes ending with '+ str(x) + ' that are followed by primes ending with ' + str(y) +' is '+ str(primeDistribution(x,y)))

print("Twin primes"+str(twinPrimes()))
"""





    
