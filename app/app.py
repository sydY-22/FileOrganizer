import os, shutil


class FileOrganizer:

    def __init__(self):
        self.folder_mapping = {
            "Text Files": "*.txt",
            "PDFs": "*.pdfs",
            "CSV": "*.csv",
            "Python": "*.py",
            "Notebooks": "*.ipynb",
            "GIFs": "*.gif",
            "PNG Images": "*.png",
            "JPEG Images": "*.jpeg",
            "JPG Images": "*.jpg",
            "Video MP4": "*.mp4",
            "Excel": "*.xlsx",
            "Word Docs": "*.docx",
            "Archives": "*.zip",
            "Audio": "*.wav"
        }
    

    def get_folder_path(self):
        """Gets the user folder path."""
        folder_path = input("Please enter your folder path: ")

        return folder_path
    
    def organize_files(self):
        """Map the files to their specified directory."""
        pass

    
    def menu(self):
        """Display Menu Welcome."""
        pass


def main():
    test = FileOrganizer()
    test.menu()

    while True:
        prompt = input("Please select between options 1-2: ")

        if prompt == '1':
            test.organize_files()
        else:
            return False


