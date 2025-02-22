from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def random_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v'
        , 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2,4)

    password_list = []

    [password_list.append(random.choice(letters)) for let in range(nr_letters)]

    [password_list.append(random.choice(symbols)) for sym in range(nr_symbols)]

    [password_list.append(random.choice(numbers)) for num in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END,string=password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def extract_data():

    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    if len(email_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="oops",message="do not leave the field empty")

    else:

        is_ok= (messagebox.askokcancel(title="website", message=f"entered details are:\nEmail: {email_data} "
                               f"\nPassword:{password_data} want to continue?"))

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website_data} | {email_data} | {password_data}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=password_img)
canvas.grid(column=1,row=0)


#website label
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

#website entry
website_entry = Entry(width=38)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2)

#email/username laber
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

#email entry
email_entry = Entry(width=38)
email_entry.insert(END,"mohdwaheed071@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)

#password label
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#password entry
password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

#generate password button
generate_password = Button(text="Generate Password",command=random_password)
generate_password.grid(column=2,row=3)

#add button
add = Button(text="Add",width=36,command=extract_data)
add.grid(column=1,row=4,columnspan=2)

window.mainloop()