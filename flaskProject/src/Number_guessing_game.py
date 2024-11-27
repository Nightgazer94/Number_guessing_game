from flask import Flask, render_template, request, redirect, url_for
import random

# Create a Flask application
app = Flask(__name__)

# Generate a random number for the player to guess
number_to_guess = random.randint(1, 100)

# Define the main game route that handles user input from the form
@app.route("/", methods=["GET", "POST"])
def game():
    global number_to_guess
    message = ""

    try:
        if request.method == "POST":
            # Get user input and try to convert it to an integer
            user_num = int(request.form["user_guess"])

            # Check if the input is less than, greater than, or equal to the random number
            if user_num < number_to_guess:
                message = "Too small!"
            elif user_num > number_to_guess:
                message = "Too big!"
            else:
                # If the player guesses the number, redirect to the win page
                return redirect(url_for('win'))

        # Render the game template with the appropriate message
        return render_template("game.html", message=message)
    except ValueError:
        # If the user enters an invalid input (text), display an appropriate message
        return render_template("game.html", message="It's not a number!")

# Define the route for the win page
@app.route("/win")
def win():
    return render_template("win.html")

# Define the route to reset the game, generating a new number and redirecting to the main game
@app.route("/reset_game")
def reset_game():
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    return redirect(url_for('game'))

# Run the application in debug mode to display errors
if __name__ == "__main__":
    app.run(debug=True)
