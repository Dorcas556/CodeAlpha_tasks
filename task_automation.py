import os
import shutil

# Set the directory to organize (e.g., your Downloads folder)
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".doc", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".sh", ".bat", ".apk"],
    "Others": []
}

def organize_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Skip folders
        if os.path.isdir(filepath):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Determine the folder based on file extension
        moved = False
        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                target_folder = os.path.join(directory, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(target_folder, filename))
                moved = True
                break

        # Move to 'Others' if no match
        if not moved:
            other_folder = os.path.join(directory, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(other_folder, filename))

    print("✅ Files organized successfully!")

# Run the organizer
organize_files(DOWNLOADS_DIR)
