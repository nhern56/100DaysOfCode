import hangman_art
import hangman_words
import random


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Testing code
print(f'\nPssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        
        lives -= 1
        if lives <= 5 and lives > 1:
          print(f"\nYou have {lives} tries left")
        if lives == 1:
          print(f"\nYou have {lives} try left")
        if lives == 0:
            end_of_game = True
            print("\nYou lose.")
            print(f"\nThe correct word is {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")

    print(hangman_art.stages[lives])
