
# name = raw_input("Hi what is your name? ")
# print "hello ," + name
# age = raw_input("what is your age")
# print "your are old, " + age
# team = raw_input("What is your favourite team?")
# print "Hello, %s!" % name
# print "hello, {0}! so, you are {1} years old".format(name, age)
# print "hello, {0}! so, your favourite team is {1}".format(name, team)
# print "hello".capitalize()
#
# if name.endswith("luo"):
#     print"cool name"
# else:
#     print "boring name"
#
# somevalue ="hello".


name = raw_input("Hi what is your name?")
print "Hello " +name.capitalize()

game = raw_input("would you like to play a game(y/n)")
print "Hello, {0},".format(name.capitalize(), game)

if game.endswith("y"):
    print"good choice"
else:
    print"bad choice"


namebetter =raw_input("Hi, what is your name?: \n")
choice = raw_input("hello %s, would you like to play a game (y/n)\n")


goo_choice_made = False

while not goo_choice_made:
    if choice.upper().startswith('N'):
        choice = raw_input("hello %s, would you like to play a game (y/n)\n") %namebetter.capitalize()
        print "good choice"
        goo_choice_made =True
    elif choice.upper().startswith('Y'):
        print "you die"
        goo_choice_made = True
    else:
        print"its a simple question , yes or no?"





