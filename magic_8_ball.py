import random
import time

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')
print('')

possible_answers = ("It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes Signs point to yes", "Reply hazy", "try again", "Ask again later", "Better not tell you that", "Cannot predict now", "Concentrate and ask again", "Dont count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful")
user_name = input("Hello player... I am the magic 8 ball... And what might your name be? ")

print("Well hello there {}"
.format(user_name))

time.sleep(2)

def answer_generator():
    question = input("What is your question for me today? ")
    time.sleep(2)
    print("Interesting...")
    time.sleep(1)
    print("Very interesting...")
    time.sleep(3)
    
