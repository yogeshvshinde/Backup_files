Performing regular backups of important files :

●       Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.

●       The script should copy all files from the source directory to the destination directory.

●       Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.

●       Handle errors gracefully, such as when the source directory or destination directory does not exist.

==============================================================

How It Works:

✔ Uses command-line arguments
python backup.py /path/source /path/destination

✔ Copies all files

Uses shutil.copy2() which preserves metadata like file timestamps.

✔ Avoids overwriting

If a file already exists, it creates a name like:

report.txt → report_20250214_153045.txt

✔ Error Handling Included

Source directory missing

Destination directory missing

Problems copying a file

Incorrect number of arguments

================================================================

Output screenshot:

<img width="575" height="243" alt="image" src="https://github.com/user-attachments/assets/bb070dd7-616c-4e4e-92d9-4502ca9e2f50" />

