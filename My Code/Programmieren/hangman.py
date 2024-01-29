import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Hangman!")
    
    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("\nAktueller Stand:", current_display)
        
        if current_display == word_to_guess:
            print("Wort erraten!", word_to_guess)
            break
        
        guess = input("Rate einen Buchstaben: ").lower()
        
        if guess in guessed_letters:
            print("Buchstabe wurde bereits verwendet. Versuche es erneut.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word_to_guess:
            attempts -= 1
            print("Nööö! Noch", attempts, "Versuche übrig.")
            
            if attempts == 0:
                print("Verloren, das Wort war:", word_to_guess)
                break

hangman()
