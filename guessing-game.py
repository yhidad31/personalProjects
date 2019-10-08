secret_word = str('apple')
incorrect_guesses_left = int(10)
 
print('Length of secret word is ', len(secret_word), 'characters')


while incorrect_guesses_left > 0:

    print('You have', incorrect_guesses_left, 'incorrect guesses left')
    
    guess = str(input('Guess: '))
    
    if len(guess) == 1: # letter
        num_letters = 0
        for letter in secret_word:
            if letter == guess:
                num_letters = num_letters + 1
                
        if num_letters > 0:
            print('That letter is in the word! Count:', num_letters)
        else:
            print('That letter is not in the word.')
            incorrect_guesses_left = incorrect_guesses_left - 1
            
    elif len(guess) == len(secret_word): # word
        if guess == secret_word:
            print('That is the correct word!')
            break
        incorrect_guesses_left = incorrect_guesses_left - 1
    else: # invalid
        print('That is not a valid guess.')