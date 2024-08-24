import random



def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'algorithm']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    while True:
        # Game setup
        word = choose_word()
        guessed_letters = set()
        incorrect_guesses = set()
        max_attempts = 6
        attempts = 0
        hints_given = 0

        print("Welcome to Hangman!")
        print("Try to guess the word. You have 6 attempts.")
        
        while attempts < max_attempts:
            # print(HANGMAN_STAGES[attempts])
            print("\nWord: ", display_word(word, guessed_letters))
            print("Incorrect guesses: ", ' '.join(incorrect_guesses))
            print("Attempts left: ", max_attempts - attempts)
            
            if hints_given == 0 and len(guessed_letters) < len(word) - 1:
                hint_request = input("Would you like a hint? (yes/no): ").lower()
                if hint_request in ['yes', 'y']:
                    hint_letter = [letter for letter in word if letter not in guessed_letters][0]
                    print(f"Hint: One of the letters is '{hint_letter}'.")
                    hints_given += 1
            
            guess = input("Enter a letter: ").lower()
            
            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter.")
                continue
            
            if guess in guessed_letters or guess in incorrect_guesses:
                print("You already guessed that letter.")
                continue
            
            if guess in word:
                guessed_letters.add(guess)
                if all(letter in guessed_letters for letter in word):
                    print("\nCongratulations! You guessed the word:", word)
                    break
            else:
                incorrect_guesses.add(guess)
                attempts += 1
                if attempts == max_attempts:
                    # print(HANGMAN_STAGES[attempts])
                    print("\nGame Over! The word was:", word)
                    break

        # Play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    hangman()
