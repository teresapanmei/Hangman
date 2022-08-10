import random
import time

def hangman():
    name=input("enter your name:")
    time.sleep(2)
    print("Hello",name,"welcome to hangman game")
    time.sleep(2)
    print("lets start the game")
    word_list=["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                    ,"plants"]
    chosen_word=random.choice(word_list)
    word_lenght=len(chosen_word)

    display=[]
    for i in range(word_lenght):
        display=display+list("_")

    lives=7
    game_over=False
    while not game_over:
        guess=input("enter the letter : ").lower()
        for i in range(word_lenght):
            letter=chosen_word[i]
            if letter==guess: 
                display[i]=letter
                print()

        if guess not in chosen_word:
                lives-=1
                if letter!=guess and lives==6:
                    print("_____\n"
                    "|      \n"
                    "|      \n"
                    "|      \n"
                    "|      \n"
                    "|      \n"
                    "|      \n"
                    "|__\n")
                    print((f"allowed error,{lives},left next guess:"))
                if letter!=guess and lives==5:    
                    print("_____ \n"
                    "|     |\n"
                    "|     |\n"
                    "|     \n"
                    "|     \n"
                    "|      \n"
                    "|      \n"
                    "|__\n")
                    lives-=1
                    print((f"allowed error,{lives},left next guess:"))
                if letter!=guess and lives==4: 
                    print("_____ \n"
                    " |      | \n"
                    " |      |\n"
                    " |      | \n"
                    " |      \n"
                    " |      \n"
                    " |      \n"
                    " |__\n")
                    print((f"allowed error,{lives},left next guess:"))
                if letter!=guess and lives==3: 
                    print("_____\n"
                    "|     |\n"
                    "|     |\n"
                    "|     |\n"
                    "|     O\n"
                    "|      \n"
                    "|      \n"
                    "|__\n")
                if letter!=guess and lives==2: 
                    print("_____ \n"
                    "|     | \n"
                    "|     |\n"
                    "|     | \n"
                    "|     O \n"
                    "|    /|\ \n"
                    "|        \n"
                    "|__\n")
                    print((f"allowed error {lives},left next guess:"))
                if letter!=guess and lives==1: 
                    print("_____ \n"
                    "|     | \n"
                    "|     |\n"
                    "|     | \n"
                    "|     O \n"
                    "|    /|\ \n"
                    "|    / \ \n"
                    "|__\n")
                    
                    print(f"game over!the word was{letter}")
                    option=input("Do you want to play again? enter yes/no:")
                    if option=="yes":
                        hangman()
                    else:
                        break

                            
        print(display)  
        
        if "_" not in display:
            game_over=True
            print("congratulation! you have guess the chosen word")
            option=input("Do you want to play again? enter yes/no:")
            if option=="yes":
                hangman()
            else:
                break

hangman()

        
