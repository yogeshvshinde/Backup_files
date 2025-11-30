import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if source exists
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Check if destination exists
    if not os.path.isdir(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    # List all files in the source directory
    files = os.listdir(source_dir)

    if not files:
        print("No files found in the source directory.")
        return

    print("Starting backup...\n")

    for file_name in files:
        source_file = os.path.join(source_dir, file_name)

        # Skip directories; only copy files
        if os.path.isdir(source_file):
            continue

        # Check if file exists in destination
        dest_file = os.path.join(dest_dir, file_name)

        if os.path.exists(dest_file):
            # Add timestamp to avoid overwriting
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            name, extension = os.path.splitext(file_name)
            new_file_name = f"{name}_{timestamp}{extension}"
            dest_file = os.path.join(dest_dir, new_file_name)

        # Copy file
        try:
            shutil.copy2(source_file, dest_file)
            print(f"Copied: {file_name} → {dest_file}")
        except Exception as e:
            print(f"Error copying {file_name}: {e}")

    print("\nBackup completed successfully.")


if __name__ == "__main__":
    # Expect exactly 2 command-line arguments (source + destination)
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    backup_files(source_directory, destination_directory)
