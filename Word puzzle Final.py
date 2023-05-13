
secret = 'laptop'
display = '_'*len(secret)
print('\nWelcome to the word guessing game!')
print('---------------------------------')
show = print(f'Your hint is: {display}') 
guess = input('What is your guess?: ').lower()
co = 1

while guess != secret:
    i = 0
    if guess in secret:
        while secret.find(guess, i) != -1:
            i = secret.find(guess, i)
            display = display[:i] + guess + display[i + 1:]
            i += 1
            
        if guess in secret:  
            print('\n---------------------------')
            print(f'Correct letter {guess.capitalize()}, guess again!')
            print('---------------------------')

    print(f'\nYour hint is: {display}')
    guess = input('What is your guess?: ').lower()
    co = co + 1
else:
    print('\nCongratulations! You guessed it!')
    print(f'It took you {co} guesses.')

       
