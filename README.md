Hangman Game Implementation
Objective

The objective of this project is to implement a text-based Hangman game in Python. The player has to guess a randomly selected word by entering one letter at a time. The game continues until the player either guesses the complete word or runs out of attempts.

Requirements
Game Initialization
A random word is selected from a predefined list.
The player is given 15 attempts.
The selected word is displayed as underscores (_) representing hidden letters.
Player's Guessing

The program should:

Ask the player to enter one letter at a time.
Check whether the guessed letter exists in the word.
Reveal the correct letter in all matching positions.
Reduce the remaining attempts if the guessed letter is incorrect.
Keep track of guessed letters.
Inform the player if they enter the same letter again.
Game Over Conditions
Win Condition
If all letters are guessed correctly before attempts reach zero, display a congratulatory message.
Lose Condition
If all attempts are used, display a game over message and reveal the correct word.
Input Validation

The program should ensure that:

Only a single alphabet letter (A–Z or a–z) is accepted.
Numbers, symbols, spaces, or multiple characters are rejected.
Invalid input prompts the user to enter a valid letter.
