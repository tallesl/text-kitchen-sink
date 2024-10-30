#!/usr/bin/env python3

# pip install beautifulsoup4 tqdm

from sys import argv
from os import walk
from os.path import isfile, join, basename, dirname
from bs4 import BeautifulSoup
from csv import writer, QUOTE_MINIMAL
from tqdm import tqdm
from uuid import uuid4

def parse_arguments():
    if len(argv) != 3:
        print("Usage: scrap-to-csv.py 'source_directory' '<css_selector>'")
        exit(1)
    source_directory = argv[1]
    css_selector = argv[2]
    return source_directory, css_selector

def get_files_in_directory(source_directory):
    files_in_directory = []
    for dirpath, _, filenames in walk(source_directory):
        for file_name in filenames:
            file_path = join(dirpath, file_name)
            if isfile(file_path):
                files_in_directory.append(file_path)
    return files_in_directory

def process_files(files_list, css_selector):
    extracted_data = []
    for file_path in tqdm(files_list, desc="Processing files"):
        # Process each file in the list
        data_from_file = process_file(file_path, css_selector)
        extracted_data.extend(data_from_file)
    return extracted_data

def process_file(file_path, css_selector):
    # Get directory and file name
    dir_name = basename(dirname(file_path))
    file_name = basename(file_path)

    try:
        # First, try to open the file with utf-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file_handle:
            file_content = file_handle.read()
    except UnicodeDecodeError:
        # If utf-8 fails, try ISO-8859-1
        with open(file_path, 'r', encoding='ISO-8859-1') as file_handle:
            file_content = file_handle.read()

    data = extract_data(file_content, css_selector, dir_name, file_name)
    return data

def extract_data(html_content, css_selector, dir_name, file_name):
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.select(css_selector)
    data = []
    for element in elements:
        # Extract text from each selected element
        elements = element.find_all(string=True, recursive=False)
        texts = [e.strip() for e in elements if e.strip()]

        if not texts:
            continue

        text = ''.join(texts)

        uid = str(uuid4())
        data.append({
            'id': uid,
            'directory': dir_name,
            'file': file_name,
            'content': text
        })
    return data

def write_to_csv(data):
    with open('scrap.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = writer(csvfile, quoting=QUOTE_MINIMAL, escapechar='\\', lineterminator='\n')
        # Write header
        csv_writer.writerow(['id', 'directory', 'file', 'content'])
        for row in data:
            # Write each data row to the CSV file
            csv_writer.writerow([row['id'], row['directory'], row['file'], row['content']])

def main():
    source_directory, css_selector = parse_arguments()
    files_list = get_files_in_directory(source_directory)
    extracted_data = process_files(files_list, css_selector)
    write_to_csv(extracted_data)

if __name__ == '__main__':
    main()
