# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 23:52:21 2018

@author: Carte
"""

import random
from math import floor
from math import sqrt
import sys

#modes, 0=gen key, 1, encrypt data, 2, decrypt data, 4= testing all


mini = 1e5
mx = 1e8#apperently max is a parameter

def pkf(n):
    if n%2==0: #if it is devisable by two we can quickly write it off and I use an if else structure for optumisation
        return False
    else:
        if sqrt(n)-floor(sqrt(n))==0:#this is the dirtly little part, so Ill break it up
            return False
        #1 we start from 3, although 1, and 2 are prime they are not the size we want
        #2 We end at the rounded down square root of the imputed number, again for optomisation
        #3 We then move in steps of 2 becuase we started at 3 which was odd, elemiating half the nessasary computations
        else:
            for i in range(3,floor(sqrt(n)),2): 
                if n%i==0: #This is to check and already optomised y iteration of I for a possible factor
                    return False
            if n<=2:
                return False 
            #Anything less then and including 2 is technicaly a prime number... 
            #...however that is not the scale of the numbers we want
            #this can be included in the beginning however it is extra comutput power is highly unlikly that your min...
            #... value is set to 0 espesahly if used for encryption
            else: return True
                
#man I hate the Euclid Algorythem but less go

def mdin(iv1,dm):                                          #Modular inverse fuction, taking imput inverse 1 and de mod
    
    
                    # give my self some space here to relacc
                    
                    
    mOg=dm                                               #The OG or orgianal ganster mod is equil to the current value of de mod
    x=0
    y=1
    if(dm==1):
        return 0                                         #becuase the mod is 1 everything can be devided by one with no remainder, I honestly dont know about what happens to 0/1
    else :
        while(iv1>1):
            q=floor(iv1/dm)                              #this creats the quotient
            tf=dm                                        #transpher variable just used to hold data when rearaging others
            
            dm=iv1%dm                                   #making the modular the remainder of the inverse imput
            iv1= tf                                     # turns to the previous value of dm
            tf=x                                        #hold the current y value after tf is used
            #now lets update our x and y
            
            x=y-q*x                                     #The value of x gets the value of y subtract the product of the 
            y=tf                                        #y gets the previous value of x wich is transphered
            
        if(y<0):
            y=y+mOg #important to keep x positive
    return y

def gcd(x1,y1): #basicly valadate greatest common factor making sure that the varibles are exclusivly prime, else if know by an attack can be used to find the other factors of the decryption key or conpute a decreption key
    while y1!=0:
        vh =x1        #dont ask, this holds first x value
        x1=y1         #swamp x with y
        y1=vh%y1      #Check for remainder
    return x1 #Basicly it looks for possible links
def genPrime():
    n=random.randint(mini,mx)
    while not pkf(n):                                  #Pretty strait forward, while not a confirmed prime number a new one is generated, 
        n=random.randint(mini,mx)
    #pass test
    return n
def keyGen(): #math, Key:n=p*q
    
    #Getting to large primes for Euler's algorythem, man I hate this
    p=genPrime()
    q=genPrime()
    ns= p*q#whoops already used n
    #the devils Phi Function
    phi=(p-1)*(q-1)
    e = random.randrange(1,phi) #Intial value for e, will probably change
    while gcd(e,phi)!=1: #we need to make sure that phi and exclusivly prime
         e = random.randrange(1,phi)
    d= mdin(e,phi)
        #now we have what we need to make da keyzzz

    return((d,ns),(e,ns))    #the e and n will be needed for the public keys for encryption while the d and n will be needed for decreption

def encryPG(public_key,text):    #User imputs    
    e_t = []#encrypted text, now we begin
    for char in text:
        e,ns=public_key
        ntv=ord(char)         #ntv is the numeric text value, ord turns each of our chacters into their numaric unicode equivilent
        e_t.append(pow(ntv,e,ns)) #append adds to the end of the array, and pow works like pow(base, exponet, mod)
    
    return e_t #finaly
def decry (pk, e_t):
    d,ns=pk
    text=''
    
    for n in e_t:
        ch=pow(n,d,ns)      #ch or charicter
        text=text+str(chr(ch)) #str is the reverse of ord
    return text

def futureUseUgh ():
    pk,public_key=keyGen() #Makes the keys
    txta="" #Put text here 
    pbkf=0,0 #Put publick keys here the 2 values in theier givin order
    encryPG(pbkf,txta) #encrypt the data
    prk=0,0 #enter privite keys
    x=0
    decry(prk,x) #feed the list right into the data, delete the x


#if all else fails, and things bug out, use the working test functions, the varibles are the same as above and provent to work
    
pk,public_key=keyGen()
print(pk)
print(public_key)
print(encryPG(public_key,txt))
ct=encryPG(public_key,txt);
finders= decry(pk,ct)
print(finders)

system.stdout.flush()