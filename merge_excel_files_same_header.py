import os, re, shutil, csv
from pathlib import Path

#iterage over all files in the directory

dir = r'C:\Users\Chris\Desktop\Python Scripts\merge_excel_files_same_header\merge_excel_files_same_header\source csvs'
output_csv = r'C:\Users\Chris\Desktop\Python Scripts\merge_excel_files_same_header\merge_excel_files_same_header\output csv\merged_csv.csv'
csv_dictionary = []
keys = None

def add_csv_contents(csv_in):
    with open(csv_in, newline='') as csv_file:
        reader = csv.DictReader(csv_file)  # read in csv to DictReader
        for row in reader:  # iterate over all rows in reader (csv)
            csv_dictionary.append(row)

def iter_over_files(parent, dir):
    """iterates over all files in a directory and performs a function upon them"""
    full_path = os.path.join(parent, dir)
    for entry in os.listdir(full_path):
        f, e = os.path.splitext(entry)
        entry_full_path = os.path.join(full_path, entry)
        if os.path.isdir(entry_full_path):
            iter_over_files(full_path, entry)
        elif e == ".csv":
            add_csv_contents(entry_full_path)

def export_dictionary_to_csv():
    with open(output_csv, 'w', newline='') as csv_file_out:
        keys = dict.fromkeys(csv_dictionary[0])
        writer = csv.DictWriter(csv_file_out, fieldnames=keys)  # set the keys as headers for new csv
        writer.writeheader()  # write header row to new csv
        writer.writerows(csv_dictionary)  # write the row to new csv

def main():
    iter_over_files("", dir)
    print(csv_dictionary)
    export_dictionary_to_csv()

if __name__ == "__main__":
    main()