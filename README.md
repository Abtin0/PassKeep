# PassKeep

PassKeep is a simple and secure password manager built using the Tkinter and the CustomTkinter libraries. It allows you to generate strong passwords, save them along with associated website details, and retrieve stored passwords.

![alt text](https://github.com/Abtin0/PassKeep/blob/main/screenshot.png)

## Features

- **Password Generation**: Generate strong, random passwords with a combination of letters, symbols, and numbers.
- **Password Storage**: Save website, email/username, and password details in a JSON file.
- **Password Retrieval**: Search for saved passwords by website and view details.
- **User Interface**: A clean and user-friendly interface using CustomTkinter for modern styling.

## Requirements

- Python 3.x
- `customtkinter`
- `CTkMessagebox`
- `pyperclip`

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Abtin0/PassKeep.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd PassKeep
    ```

3. **Install requirements:**

    ```bash
    pip install -r requirements.txt
    ```
    
4. **Run the application:**

    ```bash
    python main.py
    ```
    
## Usage

- **Generate Password**: Click the "Generate Password" button to create a new password. The password will be copied to your clipboard and displayed in the password entry field.
- **Add Password**: Fill in the website, email/username, and password fields, then click "Add" to save the information. A confirmation message will appear before saving.
- **Search Password**: Enter the website name and click "Search" to retrieve and display saved details for that website.

## File Structure

- `main.py`: The main application script.
- `icon.ico`: Application icon.
- `logo.png`: Logo image displayed in the UI.
- `data.json`: JSON file where passwords and website details are stored.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. Any improvements or bug fixes are welcome!

## Contact

If you have any questions or suggestions, feel free to reach out to me at [a.fouladizadeh@gmail.com](mailto:a.fouladizadeh@gmail.com).

