from tkinter import *
import customtkinter
from customtkinter import *
from CTkMessagebox import *
import random
import pyperclip
import json


FONT_NAME = "Roboto"
MAIN_COLOR = "#0065CD"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def find_password():
    message = ""
    try:
        with open("data.json", "r") as f:
            password_data = json.load(f)
    except FileNotFoundError:
        with open("data.json", "w") as f:
            password_data = {}
            CTkMessagebox(title="Warning!", message="No data file found.", option_1="Okay", button_width=35,
                          icon="warning", button_color=MAIN_COLOR, font=(FONT_NAME, 13), option_focus=1)
    except json.decoder.JSONDecodeError:
        with open("data.json", "w") as f:
            password_data = {}
            CTkMessagebox(title="Warning!", message="No details for the website found.", option_1="Okay", button_width=35,
                          icon="warning", button_color=MAIN_COLOR, font=(FONT_NAME, 13), option_focus=1)
    else:
        website = website_entry.get()
        if website in password_data:
            for key, value in password_data[website].items():
                message += f"{key.title()}: {value}\n"
            CTkMessagebox(title=website, message=message, option_1="Okay", button_width=35,
                          button_color=MAIN_COLOR, font=(FONT_NAME, 13), option_focus=1)
        else:
            CTkMessagebox(title="Warning!", message="No details for the website found.", option_1="Okay",
                          button_width=35,
                          icon="warning", button_color=MAIN_COLOR, font=(FONT_NAME, 13), option_focus=1)


def move_focus(event):
    widget = event.widget
    if event.keysym == "Down":
        widget.tk_focusNext().focus()
    elif event.keysym == "Up":
        widget.tk_focusPrev().focus()


def save(*args):
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email/username": email,
        "password": password,
    }}
    if website != '' and email != '' and password != '':
        review_popup = CTkMessagebox(title="Review the entered info:", message=f"Website: {website}\nEmail: {email}\n"
                                                                      f"Password: {password}\nIs it okay to save?",
                            icon="question", option_1="Cancel", option_2="Okay", button_width=35,
                            button_color=MAIN_COLOR, font=(FONT_NAME, 13), option_focus=1)
        response = review_popup.get()
        if response == "Okay":
            try:
                with open("data.json", "r") as f:
                    # read old data and save it as python dict
                    json_data = json.load(f)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            except json.decoder.JSONDecodeError:
                with open("data.json", "w") as f:
                    # Save updated data to the JSON file
                    json.dump(new_data, f, indent=4)
            else:
                # update old data (dict) with new data
                json_data.update(new_data)
                with open("data.json", "w") as f:
                    # save updated data in json file
                    json.dump(json_data, f, indent=4)

            password_entry.delete(0, END)
            website_entry.delete(0, END)
            website_entry.focus()
    else:
        warning_popup = CTkMessagebox(title="Warning!", message="Please make sure not to leave any fields empty.",
                            icon="warning", option_1="Okay", button_width=35,
                            button_color=MAIN_COLOR, font=(FONT_NAME, 13), option_focus=1)


root = CTk()
root.geometry('+480+180')
root.config(padx=75, pady=75)
root.iconbitmap('icon.ico')
root.minsize(595, 485)
root.maxsize(595, 485)

customtkinter.set_appearance_mode("system")

root.title("PassKeep")

img = PhotoImage(file="logo.png")
canvas = Canvas(width=250, height=250, highlightthickness=0, background=root["bg"])

canvas.grid(row=0, column=1, pady=(0, 60))
logo = canvas.create_image(125, 125, image=img)


website_label = CTkLabel(master=root, text="Website:", font=(FONT_NAME, 13))
website_label.grid(row=1, column=0)
website_label.configure(padx=10, pady=10)

website_entry = CTkEntry(master=root, width=220)
root.update()
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = CTkButton(root, fg_color=MAIN_COLOR, text="Search", width=125, text_color='white', command=find_password)
search_button.grid(row=1, column=2, padx=2)

email_label = CTkLabel(master=root, text="Email/Username:", font=(FONT_NAME, 13))
email_label.grid(row=2, column=0)
email_label.configure(padx=10, pady=10)

email_entry = CTkEntry(master=root, width=350)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = CTkLabel(master=root, text="Password:", font=(FONT_NAME, 13))
password_label.grid(row=3, column=0)
password_label.configure(padx=10, pady=10)

password_entry = CTkEntry(master=root, width=220)
password_entry.grid(row=3, column=1)

generate_button = CTkButton(root, fg_color=MAIN_COLOR, text="Generate Password", width=125, text_color='white',
                            command=generate_password)
generate_button.grid(row=3, column=2, padx=2)

add_button = CTkButton(root, fg_color=MAIN_COLOR, text="Add", width=350, text_color='white', command=save)
add_button.grid(row=4, column=1, columnspan=2)


website_entry.bind("<Up>", move_focus)
website_entry.bind("<Down>", move_focus)
email_entry.bind("<Up>", move_focus)
email_entry.bind("<Down>", move_focus)
password_entry.bind("<Up>", move_focus)
password_entry.bind("<Down>", move_focus)
root.bind("<Return>", save)

root.mainloop()
