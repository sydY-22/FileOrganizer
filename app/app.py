import os, shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

BLACK_COLOR = "#2C2C2C"

class FileOrganizer(tk.Tk):

    def __init__(self):
        super().__init__()
        self.folder_mapping = {
            "Text Files": ".txt",
            "PDFs": ".pdfs",
            "CSV": ".csv",
            "Python": ".py",
            "Notebooks": ".ipynb",
            "GIFs": ".gif",
            "PNG Images": ".png",
            "JPEG Images": ".jpeg",
            "JPG Images": ".jpg",
            "Video MP4": ".mp4",
            "Excel": ".xlsx",
            "Word Docs": ".docx",
            "Archives": ".zip",
            "Audio": ".wav",
            "SQL": ".sql",
            "Dashboards": ".pbix"
        }

        self.folder_path = ""

        self.title("File Organizer App!")
        self.geometry("500x450")
        self.config(bg=BLACK_COLOR)

        # title label:
        self.label_title = tk.Label(self, text="File Organizer App!", font=("bold", 20))
        self.label_title.pack(pady=20)

        # select file path button:
        self.select_folder_path_button = tk.Button(self, text="Select Folder Path", command=self.select_folder_path)
        self.select_folder_path_button.pack(pady=5)

    def select_folder_path(self):
        """Select file path to organize."""
        self.folder_path = filedialog.askdirectory(title="Select Folder Path")

        if self.folder_path:
            self.organize_files()
    
    def get_folder_path(self):
        """Gets the user folder path."""
        self.folder_path = input("Please enter your folder path: ")
        return self.folder_path
    
    def organize_files(self):
        """Map the files to their specified directory."""
        # self.folder_path = self.get_folder_path()

        if not os.path.exists(self.folder_path):
            print(f"Error: The directory {self.folder_path} does NOT exist!")

        for file in os.listdir(self.folder_path):
            item_path = os.path.join(self.folder_path, file)

            # skip if item is folder itself:
            if os.path.isdir(item_path):
                continue

            for folder, extension in self.folder_mapping.items():
                if os.path.splitext(file)[1].lower() == extension:
                    # create the destination:
                    destination_folder = os.path.join(self.folder_path, folder)

                    # create the folder 
                    os.makedirs(destination_folder, exist_ok=True)
                    # move file into folder
                    shutil.move(item_path, os.path.join(destination_folder, file))
                    print(f"Successfully moved: {file} to {folder}")
                    break
        messagebox.showinfo("Success!", "Files Successfully Organized!")

    
    def menu(self):
        """Display Menu Welcome."""
        print("1. Organize Files")
        print("2. Exit")


def main():
    test = FileOrganizer()
    test.mainloop()

    # while True:
    #     test.menu()
    #     prompt = input("Please select between options 1-2: ")

    #     if prompt == '1':
    #         test.organize_files()
    #     else:
    #         return False


