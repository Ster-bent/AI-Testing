import time
import os
import random

print("Intializing Program...")
#Functions and Variables Go Here
user_files = []
if os.path.exists("memory_1.txt") == False:
    memory1 = open("memory_1.txt","x")
else:
    continue
if os.path.exists("memory_2.txt") == False:
    memory2 = open("memory_2.txt","x")
else:
    continue
    
def respond(x):
    memory1 = open("memory_1.txt","r")
    memory1_contents = memory1.read()
    if x in memory1_contents:
        print(memory_2)
    
#Functions and Variables Ends Here



#Check Values go here to make programming faster