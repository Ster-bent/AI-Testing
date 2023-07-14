#ai learning algorithm
#will add new command/keyword
#need to create a method that can determine if a string is equal to a certain phrase like hi=greeting

greet_class = ["h","H","i","I","e","l","o"]

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
    return z

#ready for use
def learn(lesson, type):
    if type == "greeting":
        memory = open("greetings.txt", "a")
        memory.write(lesson)

print(classify("sam"))
