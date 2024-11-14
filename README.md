# README - Flask Guessing Game

## Overview
This is a simple web-based guessing game built using Flask, a Python web framework. The goal of the game is for the player to guess a random number between 1 and 100.

## How to Play
1. The player enters a guess in the provided input field on the main page.
2. The game will inform the player if their guess is "Too small!", "Too big!", or if they guessed the correct number.
3. When the correct number is guessed, the player is redirected to a win page.
4. The player can reset the game at any time, which generates a new number.

## Project Structure
- **app.py**: The main application code, as provided above.
- **templates/**: A folder that contains the HTML files used in the application.
  - **game.html**: The main game page where the player makes guesses.
  - **win.html**: The page displayed when the player guesses the correct number.

## Installation Instructions
1. Make sure you have Python and Flask installed. You can install Flask using pip:
   ```
   pip install flask
   ```
2. Save the above code to a file named `app.py`.
3. Create a folder named `templates` in the same directory as `app.py`.
4. Inside the `templates` folder, create two HTML files:
   - `game.html`: This file should include an input field for guessing and a message area to display feedback.
   - `win.html`: This file should display a congratulatory message when the player guesses correctly.

## Running the Application
1. Open a terminal and navigate to the directory containing `app.py`.
2. Run the application using the command:
   ```
   python app.py
   ```
3. Open a web browser and navigate to `http://127.0.0.1:5000/` to play the game.

## Application Routes
- `/` : The main route that handles the guessing game logic.
- `/win` : The route that displays the win page.
- `/reset_game` : The route to reset the game and generate a new number.

## Notes
- The application uses a global variable (`number_to_guess`) to store the randomly generated number. This is used to maintain state between guesses.
- Input validation is performed to ensure only numerical values are accepted, with an appropriate error message for invalid inputs.

## Dependencies
- Flask

To install Flask:
```
pip install flask
```

