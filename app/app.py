import os, shutil


class FileOrganizer:

    def __init__(self):
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
            "Audio": ".wav"
        }

        self.folder_path = ""
    
    def get_folder_path(self):
        """Gets the user folder path."""
        self.folder_path = input("Please enter your folder path: ")
        return self.folder_path
    
    def organize_files(self):
        """Map the files to their specified directory."""
        self.folder_path = self.get_folder_path()

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

    
    def menu(self):
        """Display Menu Welcome."""
        print("1. Organize Files")
        print("2. Exit")


def main():
    test = FileOrganizer()

    while True:
        test.menu()
        prompt = input("Please select between options 1-2: ")

        if prompt == '1':
            test.organize_files()
        else:
            return False


