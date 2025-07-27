# Import required modules
from customtkinter import *      # CustomTkinter for modern-looking GUI widgets
from random import *             # Random module to generate random numbers

# Set UI theme
set_appearance_mode('dark')       # Dark mode for better visual appeal
set_default_color_theme('green')  # Apply green accent color to widgets

# Function to check if input number is prime
def check():
    number = int(entry1.get())  # Get number from entry and convert to int
    if number < 2:
        label2.configure(text=f"{number} is not a prime number")
    else:
        # Check divisibility from 2 to number-1
        for n in range(2, number):
            if number % n == 0:
                label2.configure(text=f"{number} is not a prime number")
                break
        else:
            label2.configure(text=f"{number} is a prime number")  # Executed only if no divisors found

# Function to generate a random number and insert into entry field
def generate():
    entry1.delete(0, "end")                              # Clear previous input
    entry1.insert(0, str(randint(100, 1000)))            # Insert a random number between 100–1000

# Create main application window
window = CTk()
window.geometry('420x100')               # Set window size
window.title('Prime number checker')     # Set window title

# Create labels and place them
label1 = CTkLabel(window, text='Number:')
label1.place(x=10, y=10)

label2 = CTkLabel(window, text="", wraplength=380, anchor="w", justify="left")
label2.place(x=10, y=40)

# Entry field for number input
entry1 = CTkEntry(window, width=100)
entry1.place(x=65, y=10)

# Button to check prime status
button = CTkButton(window, text='check', command=check, width=60)
button.place(x=170, y=10)

# Button to generate random number
button2 = CTkButton(window, text='Generate random', command=generate)
button2.place(x=240, y=10)

# Run the GUI event loop
window.mainloop()