from tkinter import PhotoImage
import customtkinter as ctk
from logic_module import creating, cardinality, biggest

# Initialize theme
ctk.set_appearance_mode("Dark")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("green")  # Options: "blue", "green", "dark-blue"

# Create main window
window = ctk.CTk()
window.geometry("420x260")
window.title("Set Cardinality Comparator")

icon= PhotoImage(file='ChatGPT Image Jul 27, 2025, 03_08_38 PM.png')
window.iconphoto(True, icon)

# Entry fields
entry1 = ctk.CTkEntry(window, width=300, placeholder_text="Enter List 1")
entry1.place(x=80, y=20)

entry2 = ctk.CTkEntry(window, width=300, placeholder_text="Enter List 2")
entry2.place(x=80, y=60)

# Labels
label1 = ctk.CTkLabel(window, text="List1:", font=("Segoe UI", 12, "bold"))
label1.place(x=30, y=20)

label2 = ctk.CTkLabel(window, text="List2:", font=("Segoe UI", 12, "bold"))
label2.place(x=30, y=60)



result_label = ctk.CTkLabel(window, text="", wraplength=380, anchor="w", justify="left")
result_label.place(x=30, y=190)

# Button actions
def run_creating():
    creating(entry1, entry2)
    result_label.configure(text="🎲 Random sets generated.")

def run_cardinality():
    cardinality()
    result_label.configure(text="🧹 Duplicates removed.")

def run_biggest():
    result_label.configure(text=f"📊 {biggest()}")

# Buttons
ctk.CTkButton(window, text="Generate Random Sets", command=run_creating).place(x=30, y=100)
ctk.CTkButton(window, text="Remove Duplicates", command=run_cardinality).place(x=30, y=130)
ctk.CTkButton(window, text="Compare Cardinality", command=run_biggest).place(x=30, y=160)

window.mainloop()