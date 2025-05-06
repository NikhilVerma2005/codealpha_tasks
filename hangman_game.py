import random

words = ['python','developers','google','microsoft','coding','terminal','codeaplha','internship','projects']

# f = open("word.txt","r")
# data = f.readline()
# words = data.split()

word = random.choice(words)
attempts=5
print("Guess the word ")

guess_word = '-'*len(word)
print(guess_word)

while attempts>0:
    
    letter=input("Guess letter : ").lower()
    if letter in word:
        for index in range(len(word)):
            if letter==word[index]:
                guess_word=guess_word[:index]+letter+guess_word[index+1:]
                print(guess_word)
        
        if guess_word==word:
            print("You won the Game!")
            break
    else:
        attempts-=1
        print("wrong guess! Try again")
        print(f"total {attempts} left")
        
else:
    print("You loose the game !")

print("The right word is ",word)