# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 17:14:58 2021

@author: Niroshkumar
"""
import sys
import sympy

def find_User_A_PrivateKey(YA,q,α):
    print("Answer:")
    print("\n(a) what is A's private key X?")
    print("Computing the Diffie-Hellman formual to find private key XA of user A :")
    print("-----------------------------------------------------------------------")
    print("What we have: YA = "+str(YA)+" , common prime (q) = "+str(q)+" , and primitive root (α) = "+str(α))
    print("\n\tYA = α^(xA) mod q -> apply XA=1,2,3...n to find mod q value should match YA\n")
    result = 0
    count = 1
    while True:
        result = (pow(α,count)) % q
        if result == YA:
            break
        print("\tif XA ="+str(count)+" => "+str(α)+"^"+str(count)+" mod "+str(q)+" = "+str(result)+" ? NO")
        count = count + 1
        
    print("\tif XA ="+str(count)+" => "+str(α)+"^"+str(count)+" mod "+str(q)+" = "+str(result)+" ? YES")
    print("\n\t\t==> Private key of user A => XA = "+str(count))    
    return(count)
    
def find_Shared_Secret_Key(YB,XA,q):
    print("\n(b) what is the secret key K, shared with A")
    print("As per Diffie-Hellman to find secret key of user B below:")
    print("---------------------------------------------------------")
    print("\tKAB = a^(xA.xB) mod q\n\t = YA^(XB) mod q => Hence, user B shared secret key can be compute\n\t = YB^(XA) mod q => Hence, user A shared secret key can be compute")
    print("\n\tNow, finding User B secret key using above formula:\n")
    print("\tWhat we have: YB = "+str(YB)+" , XA = "+str(XA)+", and q = "+str(q))
    print("\t k = YB^(XA) mod q")
    print("\t k = "+str(YB)+"^("+str(XA)+") mod "+str(q))
    K = ((pow(YB,XA)) % q)
    print("\n\t\t==> Shared Secret Key => K = "+str(K))
   
         
def main():
    try:
        YA=YB=common_Prime=primitive_Root=0
        print("Solution to Question - 2:\n In a Diffie-Hellman scheme with a common prime q =11 and a primitive root α = 2:\n"
              +"a) If user A has public key YA = 9, what is A’s private key X?"
              +"b) If user B has public key YB = 3, what is the secret key K, shared with A?\n")
      
        XA = find_User_A_PrivateKey(9, 11, 2)
        find_Shared_Secret_Key(3, XA, 11)
        while True:   
            print("<<-------------------------------------end---------------------------------------->>")
            user_Option = input("Please press 'Y/y' to continue with different values (OR) press 'E/e' to exit: ").strip()
            if user_Option.upper() == 'Y':
                common_Prime = input("Please enter the valid common_Prime (q) : ").strip()
                while True:
                     if common_Prime.isdigit():
                        common_Prime=int(common_Prime)                
                        if sympy.isprime(common_Prime):
                            break
                     common_Prime = input("Entered value neither digit nor prime..please enter the valid common_Prime (q) : ").strip()
                primitive_Root = input("Please enter the valid primitive_Root (α): ").strip()
                while True:                    
                     if primitive_Root.isdigit():
                        primitive_Root=int(primitive_Root)
                        break
                     primitive_Root = input("Entered value is not digit..please enter the valid primitive_Root (α): ").strip()
                print("\nPlease enter the below vlaues to find private key and secre key's")
                while True:
                     YA = input("Please enter the valid user A public key (YA) in digit : ").strip()
                     if YA.isdigit():
                        YA=int(YA)
                        break
                while True:
                    YB=(input("Please enter the valid user B public key (YB) in digit :")).strip()
                    if YB.isdigit():
                       YB=int(YB)    
                       break   
                XA = find_User_A_PrivateKey(YA,common_Prime,primitive_Root)
                find_Shared_Secret_Key(YB, XA, common_Prime)            
            elif user_Option.upper() == 'E':
                print("Exited..!")
                sys.exit(0)
            else:
                user_Option = input("Invalid option...Please press 'Y/y' to continue with different values (OR) press 'E/e' to exit: ").strip()
     
        
       

    except:
        pass
    
if __name__ == "__main__":
    main()