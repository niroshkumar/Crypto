# Crypto

Extracted hidden message from steganography text:
I have written  python code to find the hidden message embedded in the below steganography text.
Aim of the python code is to replace all the excess whitespace mean if two whitespaces with 1’s and singe whitespace with 0’s.

steganography text
    October 4 ‘21   This  message  is  open  for  public  release.  The Golden Gate Bridge will go through a series of renovations as of midnight, November 1st.

Steganography method used: Whitespace replace with binaries

Finally, whitespace converted binaries are grouped by 4’s and 8’s , which again transformed to ASCII value with help of ASCII table.
Python code aim:  Read the file contain subspecies message line by line, and replace singe space with 0’s and double space with 1’s. The program returns binaries which finally match with ASCII table to find out the hidden message or hidden symbol 
