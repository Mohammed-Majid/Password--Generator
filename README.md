# Flask Password Generator

This is a simple Flask web application that generates random passwords using a random walk algorithm. the algorithm traverses a graph data structure that is created at runtime. 
The application allows users to specify the length of the password (between 8 and 20 characters) and generates a password consisting of letters, digits, and special characters.

## Features

- Random password generation
- Customizable password length (8-20 characters)
- Mix of uppercase, lowercase, digits, and special characters

## Requirements

- Python 3.x
- Flask

## Setup and Installation

1. **Clone the repository:**

    ```
    git clone https://github.com/Mohammed-Majid/Password--Generator.git
    cd flask-password-generator
    ```

2. **Create a virtual environment:**

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```
    pip install Flask
    ```

4. **Run the application:**

    ```
    python app.py
    ```

5. **Open your browser and go to:**

    ```
    http://127.0.0.1:5000
    ```

## Usage

1. Open the application in your browser.
2. Enter the desired password length (between 8 and 20 characters).
3. Click "Generate" to create a new password.
4. The generated password will be displayed on the page.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for rendering the password generation form and displaying the result.
- `static/css/styles.css`: The CSS file for styling the HTML template.

