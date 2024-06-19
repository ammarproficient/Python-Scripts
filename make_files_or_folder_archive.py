import shutil
import os

# Add your files or folder path below
source_path = "D:/"

# Add output path where you want to store
output_dir = "D:/"

# Add name to your zip folder
name = "output"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define the archive name and full path (excluding the extension)
archive_name = os.path.join(output_dir, name)

# Create the archive
archive = shutil.make_archive(archive_name, 'zip', source_path)
print(f"Your files or folder have been archived at: {archive}")
