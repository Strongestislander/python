
phrase = "Klan academy"
print(phrase + " is cool")
#prints out string  and turns every character in the variable phrase to lower case
print(phrase.lower() + " is cool")
#prints out string  and turns every character in the variable phrase to upper case
print(phrase.upper() + " is cool")

#boolean to check if the variable phrase is all lower case
print(phrase.islower())
#change every character in the variable phrase to lower case than returns a boolean if every character is lower case
print(phrase.lower().islower())
#boolean to check if the variable phrase is all upper case
print(phrase.isupper())
#change every character in the variable phrase to upper case than returns a boolean if every character is upper case
print(phrase.upper().isupper())

#gets the length of the variable phrase and turns it to a string
print("There is " + str(len(phrase)) + " characters in " + phrase )

#prints out 5th character in the variable phrase
print(phrase[5])
#prints out the index vaule of the stated Parameter in the variable phrase
print(phrase.index("a"))
#replaces parameter within variable phrase with new parameter (second string chamber)
print(phrase.replace("Klan", "Chamber"))