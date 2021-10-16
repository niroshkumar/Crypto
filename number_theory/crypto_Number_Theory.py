# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Niroshkumar 
ID: 100805047
Email: niroshkumar.balasubramanian@ontariotechu.net

This program provide three main functions to user such as check primality of number using miller robin, 
find system congurences through chinese remainder theorem and AES encryption
"""
from sympy import gcd
from sympy.ntheory.modular import crt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.exceptions import UnsupportedAlgorithm
import sys
import os

match_option = '0'
input_number = '0'
limit = 10000
MR_Result = ""

def powerOfNumber(a,b):
    return pow(a, b);

def checkDigit():
    global input_number
    while not str(input_number).isdigit() or not int(input_number) < limit or not int(input_number) > 0:
            print("Input should meet the below criterias\n\t1.Input should contain only numberic\n\t2.Input Should be greater than 0 and less than 10000 ")
            input_number = int(input("Please enter the number again : ").strip())
'''       
def checkDigitSize():
    global input_number
    input_number = int(input_number)
    while not input_number < limit:
        input_number = int(input("Number should be less than "+str(limit)+" please enter valid number : "))
'''

def getMR_Result(a,j,q):
    global MR_Result    
    modOfN = 0
    #print("\nIteration - "+str(j+1)+":\n'n' value is "+str(input_number)+"\n'q' value is "+str(q)+"\n'a' value is "+str(a)+"\n'j' value is "+str(j))
    # a^((2^j)*q) mod n = n-1
    modOfN = (powerOfNumber(a,((powerOfNumber(2, j))*q))) % input_number
    #print(str(modOfN)+" ==> mod of n")
    MR_Result= "[a^(2^j*q) mod of n] = (n - 1) ==> "+str(modOfN)+" = "+str(input_number-1)
    return modOfN

#################################################
#This function using for check primality of the #
#given number using miller robin primality check #
#algorithm                                      #
#################################################
def millerRabin():
    global input_number
    global MR_Result
    
    q,k,a=0,0,3
    temp1,temp2=0,0
    print("\nWelcom to Miller-Rabin...!")
    try:
        input_number = (str(input("Please enter the number to find prime/not : "))).strip()
        checkDigit()
        #Step 1. (n-1)=2^k * q  Hence, Find the k and q 
        while True:
            power = powerOfNumber(2, k)
            #print("Power value "+str(power))
            q = (int(input_number) - 1) / power
            #print("Q value  is "+str(q))
            if q.is_integer():
                 temp1=round(q)
                 temp2=k
            else:
                #print("Now q is not whole number")
                break
            k = k+1
        q=temp1
        k=temp2
        #print("q value : "+str(q)+" K values : "+str(k))
        
        #Step 2. Check a^q mod n = 1 ..(i.e) True -> prime False  -> not prime
        power = powerOfNumber(a, q)
        #print("Power "+str(power))
        modeValue=power % int(input_number)
        
        #Step 3. Iterating till a^2iq mod n = n-1 
        flag = False
        input_number = int(input_number)
        MR_Result= ""
        modOfN = 0
        print("MR params: \n'n' value is "+str(input_number)+"\n'q' value is "+str(q)+"\n'a' value is "+str(a))
        if not modeValue == 1:
           for j in range(k):
                #print("\nIteration-(k)- "+str(j+1)+":\n'n' value is "+str(input_number)+"\n'q' value is "+str(q)+"\n'a' value is "+str(a)+"\n'j' value is "+str(j))
                print("\nIteration-(k)- "+str(j+1))
                modOfN = getMR_Result(a,j,q)            
                if modOfN == (input_number - 1):
                    flag = True
                if flag:
                    print(MR_Result+ " ? YES")
                    print("\nTotal iteration : "+str(k))
                    print("\nResult: Given number "+str(input_number)+" is PROBABLY PRIME")
                    break
                else:
                    print(MR_Result+ " ? NO")
           if not flag:
               if k == 0:
                   #print("\nIteration-(k)- "+str(0)+":\n'n' value is "+str(input_number)+"\n'q' value is "+str(q)+"\n'a' value is "+str(a)+"\n'j' value is "+str(0))
                   print("\nIteration-(k)-"+str(0))
                   modOfN = getMR_Result(a,0,q)
                   print(MR_Result+ " ? NO")
               print("\nTotal iteration : "+str(k)) 
               print ("\nResult: Given number "+str(input_number)+" is COMPOSITE")
        else:
            #print("\nIteration - 1:\n'n' value is "+str(input_number)+"\n'q' value is "+str(q)+"\n'a' value is "+str(a))
            print("\nIteration-1:")
            print ("[a^q mod n] = 1 ==> "+str(power)+" mod "+str(input_number)+" = "+str(modeValue)+" ? YES")
            print("\nTotal iteration : "+str(k)) 
            print ("\nResult: Given number "+str(input_number)+" is PROBABLY PRIME")
    except RuntimeError as rnerr:
        print("Error captured during MR input process is : {0}".format(rnerr))
    except TypeError as typerr:
        print("Error captured during MR input process is : {0}".format(typerr))
    except NameError as nmerr:
        print("Error captured during MR input process is : {0}".format(nmerr))
    except:
        pass
        #print(input_number)    
    return 1
    
def checkStringHasDigit(string_input):
    count = 0
    for char in string_input:
        if not char.isdigit():
            count = count + 1
    return count

def checkDigitIsPositive(numbers):
    count = 0
    for n in numbers:
        if not int(n) > 0:
            count = count+1
    return count

def checkPrimality(numbers):
    count = 0
    flag = False
    numbers = list(map(int,numbers))
    print("\nvalidating the relatively primes or not........") ,
    for n1 in numbers:
        for n2 in numbers:
            if not n1 == n2:
                   if not gcd(n1, n2) == 1:
                      print("gcd("+str(n1)+","+str(n2)+") = "+str(gcd(n1,n2))+" not reltively prime")
                      flag = True
                    
                    #print(temp)
                
    if flag:
        return 1
    print("inputs are relatively prime")
    return count

#############################################
#This function using for find the system    #
# of congruences through CRT                #
#############################################
def chineseReminderTheorem():
    CRT_Positive_Integers = ""
    CRT_Prime_Integers = ""

    print("\nWelcom to chinese Reminder Theorem...!")
    try:
        CRT_Positive_Integers = (input("Please enter the positive integers in comma seperated (i.e 1,2,3) : ")).strip()
        # Validate positive integers input
        while True:
            CRT_Positive_Integers = (CRT_Positive_Integers.split(','))
            if not checkStringHasDigit(CRT_Positive_Integers) == 0 or not checkDigitIsPositive(CRT_Positive_Integers) == 0:
                print("Positve Integers input should meet the below conditions:\n\t1. Integers should be numeric\n\t2. Integers should be positive")
                CRT_Positive_Integers = input("Please enter the integers again in comma seperated (i.e 1,2,3) : ")
                continue
            else:
                break
        CRT_Prime_Integers = (input("Please enter the relatively prime positive integers in comma seperated (i.e 1,2,3) : ")).strip()
        # Validate relatively prime integers input
        while True:
            CRT_Prime_Integers = (CRT_Prime_Integers.split(','))
            if not checkStringHasDigit(CRT_Prime_Integers) == 0 or not checkDigitIsPositive(CRT_Prime_Integers) == 0 or not checkPrimality(CRT_Prime_Integers) == 0 or not len(CRT_Positive_Integers) == len(CRT_Prime_Integers):
                print("\nPositve prime Integers input should meet the below conditions:\n\t1. Integers should be relative primes (i.e gcd(5,7) = 1)\n\t2. Integers should be numeric and positive\n\t3. No. of Positive and prime integers count should be equal")
                CRT_Prime_Integers = input("Please enter the integers again in comma seperated (i.e 1,2,3) : ")
                continue
            else:
                break
        #Finding the Chinese remainders
        primeInteger = list(map(int,CRT_Prime_Integers))
        positiveInteger = list(map(int,CRT_Positive_Integers))
        crt_Result = crt(primeInteger,positiveInteger)[0]
        print("\nChinese Reminder Result:\n\t=>crt("+str(primeInteger)+","+str(positiveInteger)+") = "+str(crt_Result))
        print("\nSystem of congurences [x mod ("+str(primeInteger)+") = "+str(positiveInteger)+" ]:")
        
        #System of congruences compution
        itr = 0
        for prime in primeInteger:
            itr = itr + 1
            print("\t"+str(itr)+". "+str(crt_Result)+" mod "+str(prime)+" = "+str(crt_Result % prime))    
    except RuntimeError as rnerr:
            print("Runtime error captured during CRT input process is : {0}".format(rnerr))
    except TypeError as typerr:
            print("Type error captured during CRT input process is : {0}".format(typerr))
    except NameError as nmerr:
            print("Name error captured during CRT input process is : {0}".format(nmerr))
    except:
        pass
    return 1
    
def encryptionInputValidation(algorithm):
    inputString = str(input("Please enter the message to encrypt by "+algorithm+" method (Note: even single space will be considered as a message): "))
    while True:
        if inputString.isspace() or not len(inputString) == 0:
            break
        else:
            inputString =input("You haven't entered any message. Please enter the valid message to encrypt : ")
    return inputString
    
#################################################
#This function using for encryption/decryption  #
#user message through AES encryption/decryption #
#algorithms                                     #
#################################################
def symmetricEncryption():
    print("\nWelcom to Symmetric Encryption Theorem...!")
    try:
        print("\n1. AES encryption/decryption\n2. 3DES encryption/decryption")
        encryption_Mode = ""
        while True:
            encryption_Mode = input("Please select encryption mode : ").strip()
            if encryption_Mode == '1' or encryption_Mode == '2':
               break
            else:
                print("Invalid option") ,
        if encryption_Mode == '1':
            AES_Input_String = encryptionInputValidation("AES")
            print("\nAES plain text : "+str(AES_Input_String))
            #converted_String = bytes(AES_Input_String,encoding='utf8')
            AES_Key = os.urandom(32)
            AES_Iv = os.urandom(16)
            AES_Cipher = Cipher(algorithms.AES(AES_Key), modes.GCM(AES_Iv))
            AES_Encryptor = AES_Cipher.encryptor()
            AES_Cipher_Text = AES_Encryptor.update(bytes(AES_Input_String,encoding='utf8')) + AES_Encryptor.finalize()
         
            AES_Decryptor = Cipher(algorithms.AES(AES_Key),modes.GCM(AES_Iv, AES_Encryptor.tag)).decryptor()
            decrypted_Text = AES_Decryptor.update(AES_Cipher_Text) + AES_Decryptor.finalize()
            print("\nAES generated key : "+str(AES_Key))
            print("\nAES encrypted cipher text : "+str(AES_Cipher_Text))
            print("\nAES decrypted original text : "+str(decrypted_Text))
        else:
            DES_Input_String = input("Please enter the message to encrypt by 3DES method: ").strip() 
            print("DES encrypting message "+DES_Input_String)
            print("\nCurrently 3DES not supported")
    except UnsupportedAlgorithm as unsp:
        print("Algorithm unsupported error captured: {0}".format(unsp.with_traceback()))
    except(RuntimeError, TypeError, NameError, ValueError):
        print("\nUnexpected error captured in symmetric encryption : ",sys.exc_info())
        sys.exit(0)
    return 1

def select_Algorithms():
    if match_option == 'A':
            millerRabin()
    elif match_option == 'B':
            chineseReminderTheorem()
    elif match_option == 'C':
            symmetricEncryption()
    elif match_option == 'D':
            print("Exited..!")
            sys.exit(0)
    else:
            sys.exit(0)
            
    
    
def main():
    try:
        global match_option
        option_list = ['A','B','C','D']
        while True:
            print("\n-------------------------------------------------------")
            print("Please select any option [A|B|C|D] from following menu\n")
            print("\tA. Primality Test using Miller-Rabin\n\tB. Chinese Reminder Theorem\n\tC. Symmetric Encryption\n\tD. Exit")
            print("-------------------------------------------------------")
            match_option=input("Type the option and press Enter : ")
            match_option=match_option.upper()
            while not match_option in option_list:
                match_option=(input("Invalid option. Please select again : ")).upper()
            select_Algorithms()
        sys.exit(0)
    except:
        pass
    
    
if __name__ == "__main__":
    main()