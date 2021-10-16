# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:18:48 2021

@author: Niroshkumar
"""


 
def startFunct():
    h = open('file1.txt')
    c = [x[:-1] for x in h.readlines()]
    number = ""
    list1 = []
    for line in c:
           line=line.replace('  ', '1') 
           line=line.replace(' ', '0')
           line=line.replace('211', '1')
           for s in line:
             if s == '1' or s == '0':
                 number = number + s
           if not number == '':
            numb = number
           list1.append(numb)
           numb = ''
           number = ''
    str_data =' '
    bin_data=list1[0]
    print("The Binary value applied on whitespace : "+bin_data)
    for i in range(0, len(bin_data), 7):
      temp_data = bin_data[i:i + 7]
      decimal_data = BinaryToDecimal(temp_data)
      str_data = str_data + chr(decimal_data) 
    print("ASCII conversion of binary (groups by 8) :",str_data)
    
def BinaryToDecimal(binary):
      
    # Using int function to convert to
    # string   
    string = int(binary, 2)
      
    return string    
 

  

if __name__ == "__main__":
    startFunct()