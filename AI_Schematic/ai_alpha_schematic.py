import time
import os
import random

#testing program for memory files and how they interact
#The files are created in this version next versions might not have this feature
#Instead files will be prewrote as a folder
#This is just a schematic of what the main program will look like

print("Intializing Program...") #I REALLY LIKE THIS PART SO GONNA ADD
#Functions and Variables Go Here
user_files = []
if os.path.exists("greetings.txt") is False:
    memory1 = open("greetings.txt","x")
else:
    pass
if os.path.exists("greetings_responses_1.txt") is False:
    memory2 = open("greetings_responses_1.txt","x")
else:
    pass

def respond(x):
    memory1 = open("greetings.txt","r")
    memory1_contents = memory1.read()
    if x in memory1_contents:
       respond = open("greetings_responses.txt","r")
       content = respond.readlines()
       print(content[0]) #will print line 1, 0+1=1
    
#Functions and Variables Ends Here



#Check Values go here to make programming faster