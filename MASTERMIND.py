import getpass
import sys
def is_prime(_Player_1):
  i=1
  flag=0
  while(i<=_Player_1):
      if(_Player_1%i==0):
        flag+=1
      i+=1
  if(flag==2):
    print("hint: The number entered by the Player is a prime number")
  else:
    print("hint: The number entered by the Player is not a prime number.")
def hints(P1, P2, P_guess_count):
    while True:
        
        P_guess_count+=1
        P2 = int(input("Enter your guess: "))
        if P2==P1:
            break
        else:
            P1=str(P1)
            P2=str(P2)
            P1_list=list(P1)
            P2_list=list(P2)
            
            if P1_list==P2_list:
                break
            found=False
            for i in range(len(P1)):
                if P2_list[i]==P1_list[i]:
                    
                    print(P2_list[i])
                    found=True
            if found:
                print("The above digits entered are present in the number")
            else:
                print("None of the digits are not present in the number")
            P1=int(P1)
            P2=int(P2) 
            if P2>P1 and P2<=P1+100:
                print("The number is high you are so close try hard!!")
            elif P2>P1+100:
                print("The number is higher than the number entered by the Player")
            elif P2<P1-100:
                print("The number is lower than the number entered by the Player")
            elif P2<P1 and P2>=P1-100:
                print("The number is low you are so close try hard!!")
def valid_input():
    while True:
        Player_1 = getpass.getpass("Enter the number: ")
        str_input_p1 = str(Player_1)
        if len(str_input_p1) >= 3:
            return int(str_input_p1)
        else:
            print("The number is too short! Enter a number higher than 2 digits.")
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
