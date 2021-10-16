Number   Theory  
Submit a   Python   program called assignment1.pybased on SymPy with the following menu:

A.Primality Test using Miller-Rabin
B.Chinese Reminder Theorem
C.Symmetric Encryption
D.Exit

The behaviour of each of these menu options should be as follows:

A. Miller-Rabin [30%]. Under this option, the program takes as input from the console an integer  number  n  <  10,000,  and  uses  the  Miller-Rabin  algorithm,  as  described  in  the  course  notes,  to  determine  whether  n  is  prime  or  not.  The  program  should  output  the  result of every iteration of the loop in the Miller-Rabin algorithm, and finally whether the number  is  prime  or  not.  Of  course,  SymPy  has  the  mr  function  available  but  this  assignment is asking you to code the algorithm from scratch.
© 2021 Miguel V. Martinp. 2 of 2

B. Chinese Reminder Theorem. Under this option, the program takes as input from the  keyboard  positive  integers  a, b,  and  c,  and  also  pairwise  relatively  prime  positive  integers r, s,  and  t (i.e., gcd(r, s) = gcd(s, t)  =  gcd(r, t) = 1). The program should find the value of x that satisfies a system of congruencies of the form: x ≡ a (mod r) x ≡ b (mod s) x ≡ c (mod t) You may use SymPy functions such as crtand others.

C. Symmetric Encryption in Python. Under this option, the program takes as input from  the  keyboard  a  plaintext  message  and  encrypts  the  message  using  either  AES  or  3DES  encryption.  The  program  automatically  generates  the  necessary  key,  and outputs the corresponding ciphertext on the screen along with its decryption back to the original plaintext  and  the  key  used  for  encryption. Feel  free  to  use  example  code  from: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/.
