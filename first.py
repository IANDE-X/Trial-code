from array import *
import datetime

print("Hello welcome to the programming world \n")
phrase: str = "the world where code speaks,  codes run and bugs suck!!! \n "
my_country = input("Enter your country [----]:")
print(phrase.replace("world", my_country).upper())
print("Lets code,lets learn languages,lets play with keyboard \n")


def greetings(name, age):
    print("Good morning fuck u ", name.upper() + " " "you are ",
          str(age) + " years old  You should be fucking working by this age, this is a disgrace to ", my_country)


name = input("Enter  your name:")
Date = int(input("Enter your year of birth: \n"))
age = int(2020 - Date)
greetings(name, age)
print("But okay, tell me a word and i will tell you 10 time:\n")
i = input("Enter a word :\n")
x = int(input("Enter any number:"))
while x <= 10:

    if i == "bored":
        print("Hey ", name, "   go out to play or read a book")
        break
    elif i == "love":

        print("wow,", name + " i love you:))\n")

        break
    elif i == "fuck" and age >= 18:

        print("haha,", name + " you're stupid stop simping\n")

        break
    elif i == "sad":

        print("awww,", name + " youre making me sad also , what acn we do\n")

        break
    else:
        print(" Huh", name, " that was a ", i, "  right, whats wrong  ", name + "  is everything fine ?")
        break

print("okay hey", name, "you are  ", age, "  years old  now"  "enter the password now:")
secret = "ian"
password = " "
pass_count = 0
pass_limit = 3
out_of_guesses = False

while password != secret and not (out_of_guesses):
    if pass_count < pass_limit:
        password = input("Enter a password:")
        pass_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You cannot guess any more, try after 30 seconds")
else:
    print("Welcome  ")


class friend:
    def __init__(self, name, address, major, hobbie, partier):
        self.name = name
        self.address = address
        self.major = major
        self.hobbie = hobbie
        self.partier = partier


friend1 = friend("john", "kandia", "engineering", "fucking", "yes")
print("Name:", (friend1.name), "\n", "Adress:", (friend1.address), "\n", "Major:", (friend1.major), "\n", "Hobbie:",
      (friend1.hobbie))

x = input("Enter your new friend:\n")
y: str = input("Enter your best friend:\n")
z = input("Enter your closest friend:\n")
friends = [x, y, z]
friends2 = ["John", "Eliakim", "God", "jesus"]
friends.extend(friends2)
for friend in range(len(friends)):
    print("You're family is: ", (friends[friend]))

print("\n")


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("ENTER A WORD TO BE TRANSLATED:[-------]:")))


class student:
    def __init__(self, name, address, major, gpa, probation):
        self.name = name
        self.address = address
        self.major = major
        self.gpa = gpa
        self.probation = probation

    def honor(self):
        if self.gpa >= 3:
            print((student1.name), "is on honor role\n")
        else:
            print((student1.name), " a failure \n ")


student1 = student("john", "kandia", "engineering", 2, "yes")
print("Name:", (student1.name), "\n", "Adress:", (student1.address), "\n", "Major:", (student1.major))

# question # here i used an array to store the different question that i willa sk the user
questions_ask = [
    "What COLOR are apples??\n 1.RED \n 2.BLUE \n 3.BLACK \n\n",
    "What is your favourite FRUIT??\n 1.APPLE \n 2.GUAVA \n 3.MANGO \n\n",
    "What CITIES have you been to?\n 1.NAI \n 2.NKU \n 3.KSM\n\n",
]


# here i created a class called  Question that i will pass the argumants prompt and aansew
class Maswali:
    def __init__(self, ask, answer):
        self.ask = ask
        self.answer = answer


# here is another array tha contains answers to the asked aquestions q ojects
questions_object = [
    Maswali(questions_ask[0], "1"),
    Maswali(questions_ask[1], "2"),
    Maswali(questions_ask[2], "1"),  # qes ojcets
]


# here is a function called run that  i use to run it
def run_questions(questions_object):  # functio
    score = 0  # counter
    for question in questions_object:
        student_answer = input(question.ask)  # variable jibu
        if student_answer == question.answer:
            score += 1
    print("you got ", str(score), "/", str(len(questions_object)), " corre \n")


run_questions(questions_object)
print(student1.honor())

student_x = array('i', [1, 2, 3, 4, 5, 6, 67, ])
for x in range(4, 67):
    print(x)

command = " "
started = False
while True:
    command = input(" press  commands to start engine ----->>").lower()
    if command == "start":
        if started:
            print("car already starteed BITCH \n")
        else:
            started = True
            print("car started...\n")

    elif command == "stop":
        if not started:
            print("car already stopped\n")
        else:
            started = False
            print("car stopped.\n")
    elif command == "help":
        print("""
start- to start
stop- to stop
quit- to quit
            """)
    elif command == "quit":
        break
    else:
        print("I dont understand your command\n")
Phone = input("PHONE:\n")
digits_converter = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "for",

}
output = ""
for x in Phone:
    output += digits_converter.get(x, "!") + " "
print(output)

# emoji
message = input("Enter some text with emotions like phrases like 💌💢❤:\n")
words = message.split(' ')
emojis = {
    ":)": "🧡",
    ":(": "🤣🤣🤣🤣🤣🤣🤣🤣",
    "_": "😣",
    "++": "😎😍😍"

}
out = ""
z = 0
while z <= 10:
    for word in words:
        out += emojis.get(word, word) + " "
    z += 1
print("\n", (out))

now = datetime.datetime.now()
print("Current date and time : \n")
print("\nFinished on\n:", (now.strftime("%Y-%m-%d %H:%M:%S")))

print("\n")
print("THE END\n")