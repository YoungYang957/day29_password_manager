from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
    new_data ={
        entry_webiste.get(): {
            "email" : entry_user.get(),
            "password": entry_pass.get()
        }
    }




    if len(entry_webiste.get()) == 0 or len(entry_pass.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json","r") as file:
                data = json.load(file)
                data.update(new_data)

        except:

            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

                entry_webiste.delete(0,END)
                entry_pass.delete(0,END)

        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

                entry_webiste.delete(0, END)
                entry_pass.delete(0, END)

# ---------------------------- search function ------------------------------- #
def find_password():

    website=entry_webiste.get()
    try:
        with open("data.json") as file:
            data=json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")


    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}, Password:{password}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the webiste exist.")


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

entry_webiste = Entry(width=17)
entry_webiste.grid(row=1,column=1)
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


button_gen =Button(text="Generate Password",command=generate_password,width=13)
button_gen.grid(column=2,row=3)

button_add =Button(text="Add",width=33,command=save)
button_add.grid(column=1,row=4,columnspan=2)

button_search =Button(text="Search",command=find_password,width=10)
button_search.grid(column=2,row=1)

window.mainloop()