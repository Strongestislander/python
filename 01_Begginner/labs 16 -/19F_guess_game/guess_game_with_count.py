
print("Welcome to the Guess game please guess the secret word")
print("-----------------------------------------------------")
secret_word = "cat"
guess = ""
while guess != secret_word:
    guess = input("please enter your guess: ")

print("you win!")