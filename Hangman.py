# setup
# Take input from user and check if it's in the animal
#   if it's in the animal update the animal
#   If the letter is used before print a message
#   If it's not in the animal print part of the hanged man

import random

animals = ["cat", "dog", "elephant", "shark", "hourse", "lion", "monkey", "dolphin", "sheep"]
man = [ 
             "      O    \n",
             " *----|    \n", 
             "     \|/   \n", 
             "      |    \n",
             "      |    \n", 
             "     / \   \n", 
             " o  ------ \n", 
             "\|--- |____\n",
             " |         \n",
]

animal = random.choice(animals)
hanged_man = ""
current_answer = len(animal) * '*'
tries = 1
hanged_man += man[0]
print(hanged_man)
print(current_answer)

def check(letter):
    global current_answer, tries, hanged_man, animal
    # isRight = False
    # Right answer
    if letter not in current_answer and letter in animal:
        for i in range(len(current_answer)):
            if letter == animal[i]:
                current_answer = current_answer[:i] + letter + current_answer[i+1:]
        # isRight = True
        print(current_answer)
    # Repeated answer
    elif letter in current_answer:
        print("Repeated letter\ntry another")
        print(current_answer)

    # Wrong answer
    elif letter not in animal:
        if tries == 6:
            hanged_man += man[7] + man[8]
        else:
            hanged_man += man[tries]
        print(hanged_man)
        print(current_answer)
        tries += 1

while tries < 7:
    if animal == current_answer:
        break
    user_input = input("Enter a letter: ").strip()
    check(user_input)

if animal == current_answer:
    print("\nYou WIN :)")
else:
    print(f"\nYou lost :(")

