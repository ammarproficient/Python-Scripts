import os
import shutil
import schedule
import time

# Set up the folder paths
folder_path = os.getcwd()

# backup_folder => add your own backup path where you want to save your files
backup_folder = os.path.join(folder_path, 'BACKUP FILES')
os.makedirs(backup_folder, exist_ok=True)

# Create subfolders
python_folder = os.path.join(backup_folder, 'Python')
os.makedirs(python_folder, exist_ok=True)

images_folder = os.path.join(backup_folder, 'Images')
os.makedirs(images_folder, exist_ok=True)

videos_folder = os.path.join(backup_folder, 'Videos')
os.makedirs(videos_folder, exist_ok=True)

document_folder = os.path.join(backup_folder, 'Documents')
os.makedirs(document_folder, exist_ok=True)

audio_folder = os.path.join(backup_folder, 'Audio')
os.makedirs(audio_folder, exist_ok=True)

archives_folder = os.path.join(backup_folder, 'Archives')
os.makedirs(archives_folder, exist_ok=True)

# Files with their extensions
files = {
    "python": ['.py', '.ipynb'],
    "images": ['.png', '.jpeg', '.jpg', '.gif', '.bmp', '.svg'],
    "documents": ['.doc', '.docx', '.pdf', '.txt', '.xlsx', '.pptx'],
    "videos": ['.mp4', '.avi', '.mov', '.mkv'],
    "audio": ['.mp3', '.wav', '.aac'],
    "archives": ['.zip', '.rar', '.tar.gz'],
}


# Function to copy files to their respective folders
def copy_files():
    list_of_files = os.listdir(folder_path)
    for file in list_of_files:
        if file.endswith(tuple(files["python"])):
            shutil.copy(file, python_folder)
        elif file.endswith(tuple(files["documents"])):
            shutil.copy(file, document_folder)
        elif file.endswith(tuple(files["images"])):
            shutil.copy(file, images_folder)
        elif file.endswith(tuple(files["videos"])):
            shutil.copy(file, videos_folder)
        elif file.endswith(tuple(files["audio"])):
            shutil.copy(file, audio_folder)
        elif file.endswith(tuple(files["archives"])):
            shutil.copy(file, archives_folder)

    print("Backup has been done")


# Schedule the copy_files function to run every day
schedule.every().day.at("07:30").do(copy_files)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
