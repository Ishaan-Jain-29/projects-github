import random
import sys

#17 lines
case_1 = "      -------\n"\
         "      |     |\n"\
         "      |     |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "-------------\n"

case_2 = "      -------\n"\
         "      |     |\n"\
         "      |     |\n"\
         "    -----   |\n"\
         "    |   |   |\n"\
         "    -----   |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "-------------\n"

case_3 = "      -------\n"\
         "      |     |\n"\
         "      |     |\n"\
         "    -----   |\n"\
         "    |   |   |\n"\
         "    -----   |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "-------------\n"

case_4 = "      -------\n"\
         "      |     |\n"\
         "      |     |\n"\
         "    -----   |\n"\
         "    |   |   |\n"\
         "    -----   |\n"\
         "      |     |\n"\
         " -----|     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "-------------\n"

case_5 = "      -------\n"\
         "      |     |\n"\
         "      |     |\n"\
         "    -----   |\n"\
         "    |   |   |\n"\
         "    -----   |\n"\
         "      |     |\n"\
         " -----|-----|\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "            |\n"\
         "-------------\n"

case_6 = "      -------\n"\
         "      |     |\n"\
         "      |     |\n"\
         "    -----   |\n"\
         "    |   |   |\n"\
         "    -----   |\n"\
         "      |     |\n"\
         " -----|-----|\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "     /      |\n"\
         "    /       |\n"\
         "            |\n"\
         "            |\n"\
         "-------------\n"

case_7 = "      -------\n"\
         "      |     |\n"\
         "      |     |\n"\
         "    -----   |\n"\
         "    |*_*|   |\n"\
         "    -----   |\n"\
         "      |     |\n"\
         " -----|-----|\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "      |     |\n"\
         "     / \    |\n"\
         "    /   \   |\n"\
         "            |\n"\
         "            |\n"\
         "-------------\n"


guessed_letters = []
tries = 6

print("Welcome to Hangman!")
words = ["ball", "box", "chair", "bed", "secret", "football", "cricket", "baseball", "cake", "door", "table", "desk",
         "electricity", "water", "insects", "books", "book", "notebooks", "notebook", "paragraph", "photoframe",
         "switch", "words", "word", "random", "pencil", "eraser", "rubber", "scale", "ruler", "pen", "black", "red",
         "blue", "printer", "pager", "ink", "awards", "award", "trophy", "pillow", "calender", "car", "cars", "blood",
         "glass", "metal", "alloy", "curtains", "head", "brain", "hangman", "english", "animals", "tiger", "lion",
         "owl", "bird", "pigeon", "bike", "motorcycle", "game", "games", "unique", "good", "nuts", "slabs", "slab",
         "python", "java", "javascript", "html", "programming", "switch", "apple", "orange", "mango", "banana",
         "pineapple", "wall", "ceiling", "floor", "colours", "truck", "heading", "atmosphere", "lithosphere",
         "biosphere", "hydrosphere", "troposphere", "mesosphere", "stratosphere", "thermosphere", "exosphere", "space",
         "air"]
word = random.choice(words)


def start():
    global tries, case_1, case_2, case_3, case_4, case_5, case_6, case_7
    for letter in word:
        print("_")

    print(case_1)

    running = True
    while running:
        if tries == 0:
            print("You Lose")
            print("You killed the HANGMAN!!!")
            print(f"The word was '{word}'")
            again()
        print(f"Tries left: {tries}")
        index = 0
        for letter in word:
            if letter in guessed_letters:
                index += 1
                if len(word) == index:
                    print("You win!")
                    again()
                    break

        player_guess = input("Your letter: ")

        index2 = 0
        for letter in word:
            if player_guess != letter:
                index2 += 1
                if len(word) == index2:
                    tries -= 1
                    break

        for letter in word:
            if letter in guessed_letters:
                print(letter)
            elif player_guess.lower() == letter:
                print(player_guess.lower())
                guessed_letters.append(player_guess.lower())
            else:
                print("_")

        if tries == 6:
            print(case_1)
        elif tries == 5:
            print(case_2)
        elif tries == 4:
            print(case_3)
        elif tries == 3:
            print(case_4)
        elif tries == 2:
            print(case_5)
        elif tries == 1:
            print(case_6)
        elif tries == 0:
            print(case_7)


def again():
    global guessed_letters, tries, word
    guessed_letters = []
    tries = 6
    word = random.choice(words)
    wanna_again = input("Do you want to play again? ")
    if wanna_again.lower() == "yes":
        start()

    elif wanna_again.lower() == "no":
        sys.exit()

    else:
        print("Only type yes or no!")
        again()


start()
