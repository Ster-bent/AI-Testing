#ai learning algorithm
#will add new command/keyword
#need to create a method that can determine if a string is equal to a certain phrase like hi=greeting
greetings = []
def create_list(listtype, directory):
    f = open(directory, "r")
    contents = f.readlines
    count = 0
    while count >= contents:
        listtype.append(contents[count])
        count += 1
    f.close()

def classify(Uinput):
    if Uinput in greetings :
        Uinput = "greeting"

def learn(lesson, type):
    if type == "greeting":
        memory = open("greetings.txt", "a")
        memory.write(lesson)

create_list(greetings, "greetings.txt")
print(greetings)
