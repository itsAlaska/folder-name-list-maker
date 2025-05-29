import os
import csv
import argparse

def get_folders(directory):
    return [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

def ask_overwrite(filename):
    while True:
        answer = input(f"File '{filename}' already exists. Overwrite? (y/n): ").strip().lower()
        if answer == 'y':
            return filename
        elif answer == 'n':
            new_name = input("Enter a new filename (with .csv extension): ").strip()
            if not new_name.endswith('.csv'):
                print("Please include a '.csv' extension.")
                continue
            if os.path.exists(new_name):
                print(f"File '{new_name}' also exists. Please choose a different name.")
                continue
            return new_name
        
def generate_csv(directory, output_csv):
    folders = get_folders(directory)
    folders.sort()

    if os.path.exists(output_csv):
        output_csv = ask_overwrite(output_csv)

    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['original', 'new'])
        for folder in folders:
            writer.writerow([folder, ''])
            
    print(f"CSV file saved as: {output_csv}")

def main():
    parser = argparse.ArgumentParser(description="Generate a CSV of folder names in a directory.")
    parser.add_argument("directory", help="Path to the directory containing folders.")
    parser.add_argument("output_csv", help="Filename for the output CSV file.")
    args = parser.parse_args()

    generate_csv(args.directory, args.output_csv)

if __name__ == "__main__":
    main()