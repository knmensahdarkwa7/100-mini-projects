from customtkinter import *
from time import sleep
from winsound import Beep

set_appearance_mode('dark')
set_default_color_theme('blue')


def exe():
    # Hide input widgets
    label.pack_forget()
    entry.pack_forget()
    button.pack_forget()

    # Make window fullscreen
    window.attributes('-fullscreen', True)

    time_label.pack(expand=True, fill='both')

    for x in range(int(entry.get()), 0, -1):
        seconds = x % 60
        minutes = (x // 60) % 60
        hours = (x // 3600)
        current_time = f"{hours:02}:{minutes:02}:{seconds:02}"
        time_label.configure(text=current_time, width=500)
        window.update()
        sleep(1)

    frequency = 3000
    duration = 800
    time_label.configure(text="Time's up!")

    for _ in range(5):
        Beep(frequency, duration)
        sleep(0.1)

    # Restore default window size and widgets
    window.attributes('-fullscreen', False)
    window.geometry('420x200')

    label.pack()
    entry.pack()
    button.pack(pady=10)


window = CTk()
window.geometry('420x200')
window.title("Alarm")

label = CTkLabel(window, text='Set time:')
label.pack()

entry = CTkEntry(window, width=150, placeholder_text='Enter time in seconds')
entry.pack()

time_label = CTkLabel(window, text='', font=('Consolas', 24),anchor='center')
time_label.pack(pady=10,expand=True,fill='both')

button = CTkButton(window, text='Count down', command=exe)
button.pack()

window.mainloop()