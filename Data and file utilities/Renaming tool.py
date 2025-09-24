import os
from customtkinter import *
from tkinter import messagebox, filedialog


class RenameTool:
    def __init__(self):
        self.root = CTk()
        self.root.geometry("800x650")  # Increased width to accommodate both textboxes
        self.root.title("File Management Tool")

        self.original_name = ""
        self.current_path = os.getcwd()

        self.setup_gui()

    def setup_gui(self):
        # Create a container frame to hold the main content
        main_frame = CTkFrame(self.root, fg_color="transparent")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        label1 = CTkLabel(main_frame, text='File Management Tool', font=('Impact', 36))
        label1.pack(pady=(0, 20))

        # --- Directory Navigation and Display ---
        self.path_frame = CTkFrame(main_frame, fg_color="transparent")
        self.path_frame.pack(pady=(10, 10))

        browse_dir_button = CTkButton(self.path_frame, text='Browse', command=self.browse_directory)
        browse_dir_button.pack(side="left", padx=(0, 10))

        self.path_entry = CTkEntry(self.path_frame, placeholder_text=f"Current Path: {self.current_path}", width=400,height=30)
        self.path_entry.insert(0, self.current_path)
        self.path_entry.pack(side="left", padx=10)

        go_button = CTkButton(self.path_frame, text="Go", command=self.go_to_path)
        go_button.pack(side="left")

        # Frame to hold both file and subdirectory textboxes
        display_frame = CTkFrame(main_frame, fg_color="transparent")
        display_frame.pack(pady=10)

        # Frame and textbox for subdirectories
        subdir_frame = CTkFrame(display_frame, fg_color="transparent")
        subdir_frame.pack(side="left", padx=(0, 10), fill="both", expand=True)
        dir_label = CTkLabel(subdir_frame, text="Subdirectories in current path:")
        dir_label.pack(pady=(10, 5))
        self.dir_textbox = CTkTextbox(subdir_frame, width=350, height=150)
        self.dir_textbox.pack(pady=10)

        # Frame and textbox for files
        files_frame = CTkFrame(display_frame, fg_color="transparent")
        files_frame.pack(side="left", padx=(10, 0), fill="both", expand=True)
        files_label = CTkLabel(files_frame, text="Files in current path:")
        files_label.pack(pady=(10, 5))
        self.files_textbox = CTkTextbox(files_frame, width=350, height=150)
        self.files_textbox.pack(pady=10)

        # Initial display of content
        self.display_subdirectories()
        self.display_files()

        # --- Existing Rename Feature ---
        self.rename_frame = CTkFrame(main_frame, fg_color="transparent")
        self.rename_frame.pack(pady=20)

        separator_label = CTkLabel(self.rename_frame, text="-- Rename a file in this directory --", font=('Impact', 16))
        separator_label.pack(pady=20)

        # Entry widget for file name
        self.entry = CTkEntry(self.rename_frame, placeholder_text="Type the name of the file to rename", width=500)
        self.entry.pack(pady=10)

        # Label to display results
        self.results = CTkLabel(self.rename_frame, text='')

        # Search button
        self.search_button = CTkButton(self.rename_frame, text='Search', command=self.search_file)
        self.search_button.pack(pady=10)

        # Rename button (hidden initially)
        self.rename_button = CTkButton(self.rename_frame, text='Rename', command=self.rename_file)

    def display_subdirectories(self):
        """Displays subdirectories of the current path."""
        self.dir_textbox.delete("1.0", END)
        try:
            subdirectories = [d for d in os.listdir(self.current_path) if
                              os.path.isdir(os.path.join(self.current_path, d))]

            if subdirectories:
                self.dir_textbox.insert(END, "\n".join(subdirectories))
            else:
                self.dir_textbox.insert(END, "No subdirectories found.")
        except Exception as e:
            self.dir_textbox.insert(END, f"Error reading directory: {e}")
            messagebox.showerror("Error", f"Could not read the directory: {e}")

    def display_files(self):
        """Displays files in the current path."""
        self.files_textbox.delete("1.0", END)
        try:
            files = [f for f in os.listdir(self.current_path) if os.path.isfile(os.path.join(self.current_path, f))]

            if files:
                self.files_textbox.insert(END, "\n".join(files))
            else:
                self.files_textbox.insert(END, "No files found.")
        except Exception as e:
            self.files_textbox.insert(END, f"Error reading files: {e}")
            messagebox.showerror("Error", f"Could not read the files: {e}")

    def go_to_path(self):
        """Changes the current working directory."""
        new_path = self.path_entry.get()
        if not os.path.isdir(new_path):
            messagebox.showerror("Error", "The specified path is not a valid directory.")
            return

        try:
            os.chdir(new_path)
            self.current_path = os.getcwd()
            self.path_entry.configure(placeholder_text=f"Current Path: {self.current_path}")
            self.path_entry.delete(0, END)
            self.path_entry.insert(0, self.current_path)
            messagebox.showinfo("Success", f"Changed directory to: {self.current_path}")
            # Update both textboxes
            self.display_subdirectories()
            self.display_files()
        except Exception as e:
            messagebox.showerror("Error", f"Could not change directory: {e}")

    def browse_directory(self):
        """Allows the user to select a directory and navigates to it."""
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.path_entry.delete(0, END)
            self.path_entry.insert(0, directory_path)
            self.go_to_path()

    def search_file(self):
        """Searches for the file and updates the GUI."""
        self.original_name = self.entry.get()
        if not self.original_name:
            messagebox.showerror("Error", "Please enter a file name.")
            return

        # Check if the file exists in the current working directory
        full_path = os.path.join(self.current_path, self.original_name)
        if os.path.exists(full_path):
            self.entry.delete(0, END)
            self.entry.configure(placeholder_text=f"Type the new name for '{self.original_name}'")
            self.results.configure(text=f"File found: '{self.original_name}'")

            self.search_button.pack_forget()
            self.results.pack(pady=10)
            self.rename_button.pack(pady=10)
        else:
            self.results.configure(text="File not found")
            self.results.pack(pady=10)
            messagebox.showerror(title='404', message='The file was not found in the current directory.')
            self.results.pack_forget()

    def rename_file(self):
        """Renames the file and updates the GUI."""
        new_name = self.entry.get()
        # Check for invalid characters
        if any(char in new_name for char in ['/', ':', '*', '?', '"', '<', '>', '|']):
            messagebox.showerror("Invalid Name", "File name contains invalid characters.")
            return

        original_full_path = os.path.join(self.current_path, self.original_name)
        new_full_path = os.path.join(self.current_path, new_name)

        try:
            os.rename(original_full_path, new_full_path)
            self.results.configure(text=f"The file has been renamed to '{new_name}'")
            messagebox.showinfo("Success", f"The file has been renamed to '{new_name}'")

            # Reset the GUI for the next operation
            self.entry.delete(0, END)
            self.entry.configure(placeholder_text="Type the name of the file to rename")
            self.results.pack_forget()
            self.rename_button.pack_forget()
            self.search_button.pack(pady=10)
            self.display_files()  # Refresh the file list

        except FileNotFoundError:
            messagebox.showerror("Error", "The original file was not found.")

        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = RenameTool()
    app.run()
