
# -*- coding: utf-8 -*-
#FIB
def fib(nop):
 a=0
 b=1
 n=2
 while n<=nop:
  temp=b
  b=a+b
  a=temp
  n=n+1

 return b
#CAESAR
def caesar(text,s):
 result = ""
 for i in range(len(text)):
      char = text[i]  
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
 return result
from pwn import *
import re
import sys
from time import sleep
import os
def intro():
 print """
 \033[1;31;31m
 ███     ▄   ▄████  ▄███▄   ▄███▄   █▄▄▄▄   ▄▄▄▄▄   ▄███▄   ▄█▄                 ▄▄▄▄▄▄ ▀▄    ▄ █ ▄▄  ▄███▄   █▄▄▄▄     ▄  
 █  █     █  █▀   ▀ █▀   ▀  █▀   ▀  █  ▄▀  █     ▀▄ █▀   ▀  █▀ ▀▄              ▀   ▄▄▀   █  █  █   █ █▀   ▀  █  ▄▀ ▀▄   █ 
 █ ▀ ▄ █   █ █▀▀    ██▄▄    ██▄▄    █▀▀▌ ▄  ▀▀▀▀▄   ██▄▄    █   ▀               ▄▀▀   ▄▀  ▀█   █▀▀▀  ██▄▄    █▀▀▌    █ ▀  
 █  ▄▀ █   █ █      █▄   ▄▀ █▄   ▄▀ █  █  ▀▄▄▄▄▀    █▄   ▄▀ █▄  ▄▀              ▀▀▀▀▀▀    █    █     █▄   ▄▀ █  █   ▄ █   
 ███   █▄ ▄█  █     ▀███▀   ▀███▀     █             ▀███▀   ▀███▀                       ▄▀      █    ▀███▀     █   █   ▀▄ 
        ▀▀▀    ▀                     ▀                                                           ▀            ▀     ▀     
 \033[1;34;41m
      @coded by ZyperX | Armstrong CTF 2020 | Shifter (misc) | Fully Automated.. | BufferSEC pvt.LTD
 """
 print("________________________________________________________________________________________________________________")
 sleep(2)
intro()
p=remote("misc.2020.chall.actf.co",20300)
l=p.recv()
op=re.findall("S.*?\n",l)
print(op[1])
k=op[1].split()
k[3]=re.sub("n=",'',k[3])
print(k[1]+":"+k[3])
ciphertext=k[1]
fibs=int(k[3])
key=fib(fibs)
payload=caesar(ciphertext,key)
p.send(payload+"\n")
while True:
 try:
  l=p.recv()
  op=re.findall("S.*?\n",l)
  k=op[0].split()
  print(op[0])
  if len(k)==4:
   k[3]=re.sub("n=",'',k[3])
   print(k[1]+":"+k[3])
   ciphertext=k[1]
   if int(k[3])==0:
    fibs=0
    key=0
   elif int(k[3])==1:
    fibs=1
    key=1
   else:
    fibs=int(k[3])
    key=fib(fibs)
   payload=caesar(ciphertext,key)
   p.send(payload+"\n")
  else:
   p.send("\n")
 except:
   print(l)
   sys.exit()
