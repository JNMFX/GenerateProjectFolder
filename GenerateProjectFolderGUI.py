import os
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

class FolderCreatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Creator")

        # Main frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Project location selection
        self.location_label = tk.Label(self.frame, text="Project Location:")
        self.location_label.grid(row=0, column=0, sticky=tk.W)
        self.location_entry = tk.Entry(self.frame, width=50)
        self.location_entry.grid(row=0, column=1)
        self.browse_button = tk.Button(self.frame, text="Browse", command=self.browse_location)
        self.browse_button.grid(row=0, column=2)

        # Project name input
        self.name_label = tk.Label(self.frame, text="Project Name:")
        self.name_label.grid(row=1, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.frame, width=50)
        self.name_entry.grid(row=1, column=1, columnspan=2, sticky=tk.W)

        # Number of sequences input
        self.sequence_label = tk.Label(self.frame, text="Number of Sequences:")
        self.sequence_label.grid(row=2, column=0, sticky=tk.W)
        self.sequence_entry = tk.Entry(self.frame, width=5)
        self.sequence_entry.grid(row=2, column=1, sticky=tk.W)

        # Start button
        self.start_button = tk.Button(self.frame, text="Start", command=self.start_creation)
        self.start_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Log output
        self.log_text = tk.Text(self.frame, height=20, width=80, state=tk.DISABLED)
        self.log_text.grid(row=4, column=0, columnspan=3)

    def browse_location(self):
        location = filedialog.askdirectory(title="Select the location for the main project folder")
        if location:
            self.location_entry.delete(0, tk.END)
            self.location_entry.insert(0, location)

    def log(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.config(state=tk.DISABLED)
        self.log_text.see(tk.END)

    def create_project_folders(self, project_location, project_name, sequence_count, shot_counts):
        # Create the main project folder
        main_folder = os.path.join(project_location, project_name)
        if not os.path.exists(main_folder):
            os.makedirs(main_folder)
            self.log(f"Created main project folder: {main_folder}")
        else:
            self.log(f"Main project folder '{main_folder}' already exists.")
        
        # Create the sequence folders and their respective shot folders
        for seq in range(1, sequence_count + 1):
            padded_sequence = f"{seq:03}"
            sequence_folder = os.path.join(main_folder, f"SEQ-{padded_sequence}")
            
            if not os.path.exists(sequence_folder):
                os.makedirs(sequence_folder)
                self.log(f"Created sequence folder: {sequence_folder}")
            else:
                self.log(f"Sequence folder '{sequence_folder}' already exists.")
            
            shot_count = shot_counts[seq - 1]
            for shot in range(1, shot_count + 1):
                padded_shot = f"{shot:04}"
                shot_folder = os.path.join(sequence_folder, f"sh{padded_shot}")
                
                if not os.path.exists(shot_folder):
                    os.makedirs(shot_folder)
                    self.log(f"Created shot folder: {shot_folder}")
                else:
                    self.log(f"Shot folder '{shot_folder}' already exists.")
        
        messagebox.showinfo("Success", "All requested folders have been created (if they didn't already exist).")

    def start_creation(self):
        project_location = self.location_entry.get()
        project_name = self.name_entry.get()
        sequence_count = self.sequence_entry.get()

        if not project_location:
            messagebox.showerror("Error", "Project location is required.")
            return
        if not project_name:
            messagebox.showerror("Error", "Project name is required.")
            return
        if not sequence_count.isdigit() or int(sequence_count) <= 0:
            messagebox.showerror("Error", "A valid number of sequences is required.")
            return
        
        sequence_count = int(sequence_count)
        shot_counts = []
        for seq in range(1, sequence_count + 1):
            shot_count = simpledialog.askinteger("Input", f"Enter the number of shots for sequence SEQ-{seq:03}:")
            if not shot_count or shot_count <= 0:
                messagebox.showerror("Error", "A valid number of shots is required.")
                return
            shot_counts.append(shot_count)

        self.create_project_folders(project_location, project_name, sequence_count, shot_counts)

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderCreatorApp(root)
    root.mainloop()
