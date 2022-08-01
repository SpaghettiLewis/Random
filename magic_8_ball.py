from random import randint as ri
import time

print("  __  __          _____ _____ _____   ___ ")
print(" |  \/  |  /\   / ____|_   _/ ____|  / _ \ ")
print(" | \  / | /  \ | |  __  | || |      | (_) |") #<-- not mine
print(" | |\/| |/ /\ \| | |_ | | || |       > _ <")
print(" | |  | | ____ \ |__| |_| || |____  | (_) |")
print(" |_|  |_//    \_\_____|_____\_____|  \___/")
print("")

possible_answers = ("It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes Signs point to yes", "Reply hazy", "Try again", "Ask again later", "Better not tell you that", "Cannot predict now", "Concentrate and ask again", "Dont count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful")
user_name = input("Hello player... I am the magic 8 ball... And what might your name be? ")

while True:
    print("Well hello there {}".format(user_name))
    time.sleep(2)
    question = input("What is your question for me today? ")
    time.sleep(2)
    print("Interesting...")
    time.sleep(1)
    print("Very interesting...")
    time.sleep(3)
    answer_number = ri(0, 20)
    answer = possible_answers[answer_number]
    print(answer)
    time.sleep(4)
    while True:
        try:
            response = input("Would you like to play again? ")
            break
        except:
            print("Please enter either y, n, yes, no")
    if response == "Yes" or response == "yes" or response == "y" or response == "Y":
        print("Okay then...")
        time.sleep(3)
        continue
    elif response == "No" or response == "no" or response == "n" or response == "N":
        print("Well it was fun playing...")
        time.sleep(2)
        print("Goodbye {}".format(user_name))
        break
    else:
        time.sleep(1)
        print("Alright..")
        break