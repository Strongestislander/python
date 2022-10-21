
is_male = True
is_tall = True


#basic if statments
if is_male:
    print("you are a male")
else:
    print("you are not male")
if is_tall:
    print("you are tall")
else:
    print("you are not tall")

#if statements and else
is_male = True
is_tall = True
if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you are neither male nor tall")

#if and else if
print("\n")
is_male = True
is_tall = False
if is_male and is_tall:
    print("you are both a male and tall")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print("you are not a male and are not tall")