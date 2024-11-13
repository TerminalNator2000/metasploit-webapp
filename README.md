# Metasploit Web Interface

This project is a **web interface for managing Metasploit exploits**, built with Flask. It enables users to select and execute exploits via a user-friendly form interface.

## Project Structure

- `app.py`: Main application file, contains Flask routes and application logic.
- `static/style.css`: Stylesheet for the web interface.
- `templates/exploits.html`: Displays a form for selecting and executing exploits.
- `templates/index.html`: Home page with navigation options.
- `requirements.txt`: Lists Python dependencies for the project.
- `settings.json` and `extensions.json`: Project configuration files for environment and extension settings.

## Features

- **View Available Exploits**: Displays a list of available Metasploit exploits.
- **Execute Exploits**: Allows users to select an exploit and input a target IP address.
- **Flash Messages**: Provides feedback on execution status or errors.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   flask run
   ```

4. Access the application by navigating to `http://127.0.0.1:5000` in your web browser.

## Requirements

- **Python**: Ensure Python 3.x is installed.
- **Flask**: Web framework for the application.
- **pymetasploit3**: Python wrapper for Metasploit.

## Usage

1. Start the application by running:

   ```bash
   flask run
   ```

2. On the home page, navigate to "View Exploits" to see the available exploits.
3. Select an exploit, provide the target IP, and execute the exploit.

## Screenshots

Include screenshots of the interface here to give users a visual overview.

## Troubleshooting

- **Missing dependencies**: Run `pip install -r requirements.txt`.
- **404 errors on static files**: Ensure the `static` folder structure matches the paths in the HTML files.

## Contributing

Feel free to open issues or submit pull requests if you’d like to improve this project.
