import getpass
import sys

def is_prime(_Player_1):
    i = 1
    flag = 0
    while i <= _Player_1:
        if _Player_1 % i == 0:
            flag += 1
        i += 1
    if flag == 2:
        print("Hint: The number entered by the Player is a prime number")
    else:
        print("Hint: The number entered by the Player is not a prime number.")

def hints(P1, P_guess_count):
    while True:
        P2 = int(input("Enter your guess: "))
        P_guess_count += 1
        if P2 == P1:
            break
        else:
            P1_str = str(P1)
            P2_str = str(P2)
            P1_list = list(P1_str)
            P2_list = list(P2_str)
            
            if P1_list == P2_list:
                break
            
            common_elements = [x for x in P1_list if x in P2_list]
            if common_elements:
                for digit in common_elements:
                    print(digit)
                print("The above digits are present in the number")
            else:
                print("None of the digits are present in the number")
            
            if P2 > P1 and P2 <= P1 + 100:
                print("The number is high, you are so close, try hard!!")
            elif P2 > P1 + 100:
                print("The number is higher than the number entered by the Player")
            elif P2 < P1 - 100:
                print("The number is lower than the number entered by the Player")
            elif P2 < P1 and P2 >= P1 - 100:
                print("The number is low, you are so close, try hard!!")
            
           

    return P_guess_count

def valid_input():
    while True:
        Player_1 = getpass.getpass("Enter the number: ")
        str_input_p1 = str(Player_1)
        if len(str_input_p1) >= 3:
            return int(str_input_p1)
        else:
            print("The number is too short! Enter a number with more than 2 digits.")
            p1_foul = 0
            while len(str_input_p1) < 3:
                Player_1 = getpass.getpass("Enter the number: ")
                str_input_p1 = str(Player_1)
                p1_foul += 1
                if p1_foul == 4:
                    print("You are Disqualified!!")
                    sys.exit()
            return int(str_input_p1)

print("** Welcome to the Mastermind Game **\n\n*Instructions:\n\n1.*Objective: The goal of the game is for the second player to guess the multi-digit number chosen by the first player.\n2.*Gameplay:\n   - The first player selects a multi-digit number.\n   - The second player attempts to guess this number based on the hints provided.\n3.*Winning Condition: The second player wins the game if they successfully guess the number.\n4.*Fair Play Warning: Any attempt to observe the number entered by the opponent will result in immediate disqualification.\n\nEnjoy the game!")

print("=======Game-1========")
Player_1 = valid_input()
print("Okay!! it's time to guess the number")
p2_guess_count = 0

want_hint = input("Do you want hints? (y/n): ")
if want_hint.lower() == "y":
    is_prime(Player_1)

p2_guess_count = hints(Player_1, p2_guess_count)
print("Player-2 guessed the number correctly. Player-2 is the current MASTERMIND!!")

print("=====Game-2======")
print("Player-2 will enter the number to be guessed by Player-1.")

Player_2 = valid_input()
print("Okay!! it's time to guess the number")
p1_guess_count = 0

want_hint = input("Do you want hints? (y/n): ")
if want_hint.lower() == "y":
    is_prime(Player_2)

p1_guess_count = hints(Player_2, p1_guess_count)

print(f"Player-1 guess count: {p1_guess_count}")
print(f"Player-2 guess count: {p2_guess_count}")

if p1_guess_count < p2_guess_count:
    print("Player-1 guessed the number faster than Player-2. Player-1 has won the game!!")
    print("And the MASTERMIND is..... Player-1!!")
elif p1_guess_count == p2_guess_count:
    print("Both players guessed the number in the same number of attempts. It's a draw!!")
else:
    print("Player-2 guessed the number faster than Player-1. Player-2 has won the game!!")
    print("And the MASTERMIND is..... Player-2!!")

print("Thank you for playing the game!!")
