import time
import random
print("\n Welcome to hangman game\n")
name=input("Enter your name: ")
print("Hello"," "+ name + "!")
time.sleep(2)
print("The game is about to start!\n Lets play Hangman!")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game 
    words_to_guess = ["amongus","csgo","rocketleague","minecraft","fortnite","callofduty","fallguys",
     "leagueoflegends","grandtheftauto","pacman","paper" ]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    
def play_loop():
    global play_game
    play_game = input("do you wan to play again? y = yes, n = no \n")
    while play_game not in ["y","n","Y","N"]:
        play_game = input("do you wan to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
        
    elif play_game == "n":
        print("Thank you again. See you again!")
    
        
        
def hangman():
     global count
     global display
     global word
     global already_guessed
     global play_game
     limit = 5
     guess = input("This is the hangman word: " + display + "Enter your guess: \n")
     guess = guess.strip()
     
     
     if len(guess.strip()) == 0 or len(guess.strip()) >=2 or guess <= "9":
         print("Invalid input, Try a letter \n")
         hangman()
        
        
     elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word1 = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
        
     elif guess in already_guessed:
        
            print("Try another letter. \n")
     else:
            count += 1
            
            
     if count == 1:
       time.sleep(1)
       print("  -------------- \n"
             " |              | \n"
             " |                \n"
             " |                \n"
             " |                \n"
             " |                \n"
             " |                \n"
             " |                \n"
             " |                \n"
             " |                \n"
             " |                \n"
             "_|_               \n")
       print("wrong guess." + str(limit - count) + "gueses remaining \n")
    
     if  count == 2:
                time.sleep(1)
                print(" --------------- \n"
                      "|              | \n"
                      "|              | \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                     "_|_               \n")
                print("wrong guess." + str(limit - count) + "gueses remaining \n")
    
    
     if  count == 3:
                time.sleep(1)
                print(" --------------- \n"
                      "|              | \n"
                      "|              | \n"
                      "|              | \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                     "_|_               \n")
                print("wrong guess." + str(limit - count) + "gueses remaining \n")
    
     if  count == 4:
                time.sleep(1)
                print(" --------------- \n"
                      "|              | \n"
                      "|              | \n"
                      "|              | \n"
                      "|              | \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                      "|                \n"
                     "_|_               \n")
                print("wrong guess." + str(limit - count) + "gueses remaining \n")
    
     if  count == 5:
                time.sleep(1)
                print(" ---------------  \n"
                      "|              |  \n"
                      "|              |  \n"
                      "|              |  \n"
                      "|              |  \n"
                      "|              |  \n"
                      "|              O  \n"
                      "|             /|\ \n"
                      "|              |  \n"
                      "|              |  \n"
                      "|             / \  \n"
                     "_|_          /   \  \n")
                print("wrong guess. you hanged!!\n")
                print("The word was: ", word)
                play_loop()
                
     if count != limit:
        hangman()
        
main()
hangman()
                    
                    
            




    
    
    
    
    
    
    
    

    