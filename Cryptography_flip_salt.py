from tkinter import *
from tkinter import messagebox

def insert_salt(message, salt_char):
    salted_message = ""
    count = 0
    for char in message:
        salted_message += char
        count += 1
        if count % 4 == 0:
            salted_message += salt_char
    return salted_message

def remove_salt(message, salt_char):
    unsalted_message = ""
    for i in range(len(message)):
        char = message[i]
        if (i + 1) % 5 != 0:
            unsalted_message += char
    return unsalted_message

def flip(message):
    flipped_message = ""
    for char in message:
        flipped_message += char[::-1]  # Reverse ihe characters in the message
    return flipped_message

def encrypt():
    password = code.get()

    if password != "":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END).rstrip('\n')  # Remove newline character
        encrypted_message = ""

        for char in message:
            for password_char in password:
                encrypted_char = chr(ord(char) + ord(password_char))
                encrypted_message += encrypted_char

        salted_message = insert_salt(encrypted_message, '*')  # Insert salt after every four characters
        flipped_message = flip(salted_message)  # Flip the salted message

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Robot 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, flipped_message)

    else:
        messagebox.showerror("Encryption", "Input Text and Password")

def decrypt():
    password = code.get()
    if password != "":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END).rstrip('\n')  # Remove newline character

        flipped_message = flip(message)  # Reverse the flipped message
        unsalted_message = remove_salt(flipped_message, '*')  # Remove salt from the message

        decrypted_message = ""

        password_index = 0
        for i in range(len(unsalted_message)):
            char = unsalted_message[i]
            decrypted_char = chr(ord(char) - ord(password[password_index]))
            decrypted_message += decrypted_char
            password_index = (password_index + 1) % len(password)

        decrypted_message = decrypted_message[::len(password)]  # Get only the first character of each iteration

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Robot 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted_message)

    else:
        messagebox.showerror("Decryption", "Input Text and Password")

# Rest of the code remains the same

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    # icon
    image_icon = PhotoImage(file="Capture.PNG")
    screen.iconphoto(False, image_icon)

    screen.title("Cryptography Machine")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter your Message", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Robot 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter the password for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()

    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)
    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()


main_screen()