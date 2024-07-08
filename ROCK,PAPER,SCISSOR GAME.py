import random
import tkinter as tk

def play_game(user_choice):
    
    
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    

    paper = '''
        _______
    ---'   ____)______
              ________)
              _________)
             _________)
    ---.____________)
    '''
    
    

    scissors = '''
        ______
    ---'   ___)_____
              _______)
           ____________)
          (____)
    ---.__(___)
    '''
    

    tools = [rock, paper, scissors]
    global player_score
    global computer_score

    computer_choice = random.randint(0, 2)

    if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        player_score += 1
        result = f"You chose: {tools[user_choice]} \nThe computer chose: {tools[computer_choice]}\n You win! your score {player_score}"
    elif user_choice == computer_choice:
        result = f"You chose: {tools[user_choice]} \nThe computer chose: {tools[computer_choice]}\n It's a draw!"
    else:
        computer_score += 1
        result = f"You chose {tools[user_choice]} \nThe computer chose {tools[computer_choice]}\n You lose! computer score {computer_score}"
        
        
    if (player_score >= 10) or (computer_score >= 10):
       if player_score > computer_score:
            Result = f"Player won the game with {player_score} points\n Thank you for playing the game"
       else:
           Result = f"Computer won the game with {computer_score} points\n Thank you for playing the game"
       result_text.set(result)
       Result_text.set(Result)
       for widget in main_window.winfo_children():
           widget.pack_forget()
       tk.Label(main_window, text=Result, bg="lightpink", font="Lucida").pack(pady=10)
    else:
       result_text.set(result)

main_window = tk.Tk()
main_window.title("Rock, Paper, Scissors")
main_window.geometry("500x500")
main_window.configure(bg="lightpink")


tk.Label(main_window, text="Welcome to rock paper scissor game",bg="aqua",highlightthickness=5,font="Lucida").pack(pady=10)
tk.Label(main_window, text="Select a button below to play the game",bg="yellow",highlightthickness=5,font="Lucida").pack(pady=10)
tk.Button(main_window,text="Rock",bg="lightgreen",command=lambda:play_game(0),font="Lucida").pack(pady=5)
tk.Button(main_window,text="Paper",bg="skyblue",command=lambda:play_game(1),font="Lucida").pack(pady=5)
tk.Button(main_window,text="Scissors",bg="red",command=lambda:play_game(2),font="Lucida").pack(pady=5)


result_text = tk.StringVar()
result_label = tk.Label(main_window, textvariable=result_text, font=('Arial', 12),bg="aqua", wraplength=300)
result_label.pack(pady=10)

Result_text = tk.StringVar()
Result_label = tk.Label(main_window, textvariable=Result_text, font=('Arial', 12),bg="brown", wraplength=300)
Result_label.pack(pady=10)

player_score = 0
computer_score = 0

main_window.mainloop()
