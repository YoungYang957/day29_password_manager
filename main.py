from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters+password_numbers+password_symbols

    random.shuffle(password_list)

    password ="".join(password_list)
    entry_pass.delete(0, END)
    entry_pass.insert(END,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():




    if len(entry_webiste.get()) == 0 or len(entry_pass.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=entry_webiste.get(),
                                       message=f"These are the details entered: \nEmail: {entry_user.get()}"
                                               f"\nPassword: {entry_pass.get()} \nIs it ok to save?")

        if is_ok:

            with open("data.txt", "a") as file:
                my_tuple = (entry_webiste.get(),entry_user.get(),entry_pass.get())
                x = "|".join(my_tuple)
                file.write(f"{x}\n")

            entry_webiste.delete(0,END)
            entry_pass.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)


canvas = Canvas(width=200,height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image =photo)
canvas.grid(column=1,row=0)

label_webiste = Label(text="Webiste:")
label_webiste.grid(column=0,row=1)

entry_webiste = Entry(width=35)
entry_webiste.grid(row=1,column=1,columnspan=2)
entry_webiste.focus()

label_username = Label(text="Email/Username:")
label_username.grid(column=0,row=2)

entry_user = Entry(width=35)
entry_user.grid(row=2,column=1,columnspan=2)
entry_user.insert(END, "jinyuanyang957@gmail.com")

label_password = Label(text="Password:")
label_password.grid(column=0,row=3)


entry_pass = Entry(width=18)
entry_pass.grid(row=3,column=1)


button_gen =Button(text="Generate Password",command=generate_password)
button_gen.grid(column=2,row=3)

button_add =Button(text="Add",width=33,command=save)
button_add.grid(column=1,row=4,columnspan=2)


window.mainloop()