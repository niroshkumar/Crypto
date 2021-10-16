# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:35:44 2021

@author: Niroshkumar

AIM: 
   In a public-key system using RSA, you intercept the ciphertext
    C = 10 sent to a user whose public key is {e = 5, n = 35}. 
    Show all your work (either Math or Python) to answer the following two questions (not necessarily in that order):
        
    a) What is the plaintext M? Hint: with n = 35, a brute force may save you headaches.
    b) What is the secret exponent d in the private key {d = ?, n = 35}?
"""
import sys
import time
from sympy import gcd

print_Result = ''

def findSqurRoot(a,b):
    return pow(a,b)

def reset():
    global print_Result
    print_Result = ''
    
def find_Prime_Factorization(n):
    factor_base = 2
    factor_dict = {}
    div = 0
    count = 0
    while div != 1:
        div = n/factor_base
        if (div.is_integer()):
            count = count + 1
            factor_dict[factor_base] = count
            n = div
        else:
            count = 0
            factor_base = factor_base + 1
    return (factor_dict)

def find_Phi_of_N(dict_value):
    global print_Result
    phi_of_n = 1
    #print(dict_value)
    if len(dict_value) >= 1:
        for key, value in dict_value.items():
            phi_of_n = phi_of_n * (findSqurRoot(key, value) - findSqurRoot(key, value-1))
            print_Result = print_Result + "("+str(key)+"^"+str(value)+" - "+str(key)+"^"+str(value)+"-1) * "
        return phi_of_n
    else:
        print("Prime factors are empty..plz provide valid public key values")
        sys.exit(0)
    return 1
    
def eulers_Totient_Function(phi_Input,e,c):
    print("\nShould satisfy below conditions -:")
    print("\nCondition-1: Calculating the phi(n) euler totient function....") ,
    prime_fact_dict = find_Prime_Factorization(phi_Input)
    phi_Of_N = find_Phi_of_N(prime_fact_dict)
    time.sleep(2)
    print("completed")
    print("\t => phi(n) = (pi^ei - pi^ei-1) , -> here 'i = "+str(len(prime_fact_dict))+"' no.of prime factors\n\t = phi("+str(phi_Input)+") ="+print_Result[:-2]+" = "+str(phi_Of_N))
    reset()
    print("\nCondition-2: Verifying the gcd( phi(n), e) =  1 i.e => 1 < e < phi(n) .....") ,
    gcd_vlu = gcd(phi_Of_N,e)
    if( gcd_vlu == 1):
        print("verified")
        print("\t Hence, gcd("+str(phi_Of_N)+","+str(e)+") = "+str(gcd_vlu) + " i.e 1 < "+str(e)+" < phi("+str(phi_Input)+")")
    else:
        print("\t Hence, gcd("+str(phi_Of_N)+","+str(e)+") = "+str(gcd_vlu) + ", not satisfying the condition. \n\tPlease provide valide public key values PU = {e,n}")
        sys.exit(0)
    calculate_Secret_Exponent_Private_Key(e, phi_Of_N, phi_Input,c)
        
def calculate_Secret_Exponent_Private_Key(e,phi_Of_N,n,c):
    d = 1
    print("\n(i). Findig Question B : secret exponent 'd' in private key usig RSA key generation algorithm")
    print("\tWhat we have: phi("+str(n)+") = "+str(phi_Of_N)+" , e = "+str(e))
    print("\tfinding d :\n\t\ted = 1 mod (n)")
    print("\t\t"+str(e)+"d = 1 mode "+str(phi_Of_N))
    d = ((e*d) % phi_Of_N) 
    print("\t\td = "+str(d))
    find_Plain_Text(d,n,c)

def find_Plain_Text(d,n,c):
    print("\n(ii). Findig Question A: plain text 'M' usig RSA decryption algorithm")
    print("\t\twhat we have: c = "+str(c)+", n = "+str(n)+" d = "+str(d))
    print("\tfinding m :\n\t\tM = Cd mod n ")
    print("\t\tM = "+str(c)+"^"+str(d)+" mode "+str(n))
    M = (findSqurRoot(c, d) % n)
    print("\t\tM = "+str(M))   
    
def main():
    try:
        e=n=C=0
        print("Solution to Question -1:\n In a public-key system using RSA, you intercept the ciphertext"
              +"C = 10 sent to a user whose public key is {e = 5, n = 35}. \n\ta) What is the plaintext M? Hint: with n = 35, a brute force may save you headaches."
              +"\n\tb) What is the secret exponent d in the private key {d = ?, n = 35}? ")
        eulers_Totient_Function(35, 5, 10)
        #user_Option = input("Please press 'Y/y' to continue with different values (OR) press 'E/e' to exit: ").strip()
        while True:
            print("-------------------end------------------------")
            user_Option = input("Please press 'Y/y' to continue with different values (OR) press 'E/e' to exit: ").strip()
            if user_Option.upper() == 'Y':
                while True:
                    C=input("Please enter the valid ciphertext(C) value : ").strip()
                    if C.isdigit():
                        C=int(C)
                        break
                while True:
                    publicKey=(input("Please enter the valid receiver public keys in comma seperated (Ex. 1,2) represents {e,n} : ").strip()).split(',')
                    if len(publicKey) == 2:
                        if publicKey[0].isdigit and publicKey[1].isdigit():
                            e=int(publicKey[0])
                            n=int(publicKey[1])
                            break
              
                eulers_Totient_Function(n,e,C)              
            elif user_Option.upper() == 'E':
                print("Exited..!")
                sys.exit(0)
            else:
                user_Option = input("Invalid option...Please press 'Y/y' to continue with different values (OR) press 'E/e' to exit: ").strip()

    except:
        pass
    
if __name__ == "__main__":
    main()