import customtkinter as ctk
from tkinter import PhotoImage
from logic_module import creating, cardinality, biggest

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

# Create main window
window = ctk.CTk()
window.geometry("420x300")
window.title("Set Cardinality Comparator")

# Icon
icon = PhotoImage(file='ChatGPT Image Jul 27, 2025, 03_08_38 PM.png')
window.iconphoto(True, icon)

# Configure root window grid
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Create a frame that centers its contents
content_frame = ctk.CTkFrame(window, corner_radius=10)
content_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

content_frame.grid_columnconfigure(0, weight=1)  # For horizontal centering

# Labels + Entry fields (organized in sub-frames)
for i, label_text in enumerate(["List1:", "List2:"]):
    row_frame = ctk.CTkFrame(content_frame)
    row_frame.grid(row=i, column=0, pady=5)
    label = ctk.CTkLabel(row_frame, text=label_text, font=("Segoe UI", 12, "bold"))
    label.pack(side="left", padx=(0, 10))
    entry = ctk.CTkEntry(row_frame, width=300, placeholder_text=f"Enter List {i+1}")
    entry.pack(side="left")
    if i == 0:
        entry1 = entry
    else:
        entry2 = entry

# Buttons
button_frame = ctk.CTkFrame(content_frame)
button_frame.grid(row=2, column=0, pady=10)
ctk.CTkButton(button_frame, text="Generate Random Sets", command=lambda: [creating(entry1, entry2), result_label.configure(text="🎲 Random sets generated.")]).pack(pady=2)
ctk.CTkButton(button_frame, text="Remove Duplicates", command=lambda: [cardinality(), result_label.configure(text="🧹 Duplicates removed.")]).pack(pady=2)
ctk.CTkButton(button_frame, text="Compare Cardinality", command=lambda: result_label.configure(text=f"📊 {biggest()}")).pack(pady=2)

# Result Label
result_label = ctk.CTkLabel(content_frame, text="", wraplength=380, anchor="w", justify="left")
result_label.grid(row=3, column=0, pady=(10, 0), sticky="w")

window.mainloop()