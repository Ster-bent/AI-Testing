#ai learning algorithm
#will add new command/keyword
#need to create a method that can determine if a string is equal to a certain phrase like hi=greeting
danger_class = ["help", "me", "9", "oh no","1"]
cmd_class = ["/", "&", "!"]
greet_class = ["h","H","i","I","e","l","o","y"]
big_list = [greet_class, cmd_class, danger_class]

#not for list testing
greetings = []
#can be used
def create_list(listtype, directory):
    f = open(directory, "r")
    contents = f.readlines()
    for i in range(len(contents)):
        listtype.append(contents[i])
    f.close()





#beta of classifcation program
def classify(z):
    listz = []
    listz[:0] = z
    classification = any(item in greet_class for item in listz)
    if classification is True:
        z = "greeting"
#NEW classify program beta0.1
def classify2(uinput):
    uinput_list = []
    uinput_list[:0] = uinput
    for i in range(len(big_list)):
        simalarity = len(set(uinput_list) and set(big_list[i])) / float(len(set(uinput) or set(big_list[i]))) *10
        if simalarity >= 15:
            print(f"Type: {big_list[i]}")
            print(f"Simalarity: {simalarity}")
        else:
            pass
#ready for use
def learn(lesson, type):
    if type == "greeting":
        memory = open("greetings.txt", "a")
        memory.write(lesson)

classify2("911")
