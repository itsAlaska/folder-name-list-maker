# Folder Name Lister

This script generates a CSV file listing all the folder names in a specified directory. The CSV is formatted to be compatible with the **folder renamer** script, allowing you to easily create a mapping between original folder names and new names.

---

## What it does

- Scans the target directory and collects the names of all folders inside.
- Outputs a CSV file with two columns:  
  - `original`: The current folder names.  
  - `new`: An empty column where you can enter desired new folder names later.
- Checks if the output CSV file already exists and prompts whether to overwrite or specify a new filename.

---

## Usage

Run the script from the command line as follows:

```bash
python folder_name_lister.py <directory_path> <output_csv_filename>
