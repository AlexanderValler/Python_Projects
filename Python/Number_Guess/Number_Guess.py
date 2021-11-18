###################################
#Author: Alexander Valler
#Date: 11/8/2021
#Name: NumberGuess
#Description: Number guessing game to give 3 diffrent numbers, with 3 guesses per number, for points.
#####################################
#--Imports--#
import random   #needed to be able to generate a random number
#####################################
#--Variables--#
round_ = 1
chosen_range = "start"
points = 0
play = True
roundvalue = 0
#####################################
#--Valid Input Function--#
def valid_input(prompt, type_=None, minimum_=None, maximum_=None, range_=None):
    if (minimum_ is not None and maximum_ is not None and maximum_ < minimum_):
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        user_input = input(prompt)
        if type_ is not None:
            try:
                user_input = type_(user_input)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if maximum_ is not None and user_input > maximum_:
            print("Input must be less than or equal to {0}.".format(maximum_))
        elif minimum_ is not None and user_input < minimum_:
            print("Input must be greater than or equal to {0}.".format(minimum_))
        elif range_ is not None and user_input not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    expected = " or ".join((
                        ", ".join(str(x) for x in range_[:-1]),
                        str(range_[-1])
                    ))
                    print(template.format(expected))
        else:
            return user_input

#--LeaderBoardCheck--#
#def leaderboardcheck():
    #referance and compare score to leaderboard
   # if():
   #     break
   # else:

#####################################
#--Main Code--#
while (play == True):
    print("##################################################################################")
    print("Welcome to the number guessing game!\n")
    print("How to play:")
    print("- Enter a number to be the high end of the guessing range")
    print("- You have 3 guesses to try and guess the random number in the range")
    print("- You will be awarded points based on how close you get to the value or if you guess it")
    print("- You have 3 rounds to try and earn as many points as you can\n")
    input("Enter anything to continue: ")
    print()
    
    while (0 < round_ <= 3):
        num_guesses = 3  #reset guesses
        print("--- ROUND {}! ---".format(round_))
     
        chosen_range = valid_input("Please enter the range value: ", int, 2)  #Enter range max  
        answer = (random.randint(0,int(chosen_range)))    #Generate random number for answer
        print("The range is : 0 - {}".format(chosen_range))
        
        while (num_guesses > 0):     #Able to make guesses if there are still guesses left
            guess = valid_input("Guess a number: ", int, 0, chosen_range)   #Make a guess
            distance_off = (abs(answer - guess))
            if (guess == answer):
                print("You have guessed the correct number, Congratulations!")
                num_guesses = 0
            else:
                if(guess > answer):
                    print("Your guess was {} more than the answer, guess again.".format(distance_off))
                else:
                    print("Your guess was {} less than the answer, guess again.".format(distance_off))
                num_guesses = (num_guesses - 1)
            print()

        if (guess == answer):   #runs when the answer is correctly guessed
            print("You guessed the correct number!")
            if(round_ == 1):
                points_1 = (10)
            if(round_ == 2):
                points_2 = (20)
            if(round_ == 3):
                points_3 = (30)

        elif(num_guesses == 0):  #runs when answer is not correctly guessed and there are no guesses left
            print("You have run out of guesses")
            if(round_ == 1):
                points_1 = (0)
            if(round_ == 2):
                points_2 = (0)
            if(round_ == 3):
                points_3 = (0)

        if(round_ < 3):
            round_ = (round_ + 1)
            print()
        else:
            print()
            break

    print("--- Scoreboard Time! ---")
    score = (points_1 + points_2 + points_3)
    print("Round 1 points: {}".format(points_1))
    print("Round 2 points: {}".format(points_2))
    print("Round 3 points: {}".format(points_3))
    print("Your total points are {}!".format(score))
    
    if (input("Type 'yes to see the leaderboard or anything else to continue: ") == "yes"):
        #referenace Leaderboard.txt
        #compare
        if (leaderboardcheck == True):
            #repalce score
            place_ = ("filler")
            print("You made the Leaderboard for {} place!".format(place_))
        else:
            print("You did not make the Leaderboard.")

    print()
    if(input("Type 'yes' to play again or anything else to quit: ") == "yes"):
        round_ = 1
    else:
        play = False