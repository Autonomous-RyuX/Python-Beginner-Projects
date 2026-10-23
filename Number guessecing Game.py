s_number = 12
i = 0
p = 4
while i<p:
    Guess = int(input("Guess: "))
    i = i+1
    if Guess == s_number:
        print("You Won")
        break
    else:
        print("Wrong")
else:
    print('\nSorry you failed')