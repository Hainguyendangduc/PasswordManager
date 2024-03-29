from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    entry3.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    web = entry1.get()
    e = entry2.get()
    pw = entry3.get()
    new_data = {web: {
        "email": e,
        "password": pw,
    }}
    if len(web) == 0 or len(e) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving
                json.dump(new_data, data_file, indent=4)
        else:
            # updating
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)

# ---------------------------- Search ----------------------------------#
def search():
    web_name = entry1.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data = data[web_name]
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No value can be stored.")
    except KeyError:
        messagebox.showinfo(title="Oops", message=f"Can not find {web_name} website ")
    else:
        messagebox.showinfo(title=f"{web_name}", message=f"Email: {data['email']}\n"
                                                         f"Password: {data['password']}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

#Labels
website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

#Entries
entry1 = Entry(width=33)
entry1.grid(column=1, row=1)
entry1.focus()

entry2 = Entry(width=51)
entry2.grid(column=1, row=2, columnspan=2)


entry3 = Entry(width=33)
entry3.grid(column=1, row=3)

#button
button = Button(text="Generate Password", command=generate_password)
button.grid(column=2, row=3)

button = Button(text="Search", command=search)
button.grid(column=2, row=1)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

mainloop()