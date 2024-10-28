#!/usr/bin/env python3

from sys import argv
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
from csv import writer
from tqdm import tqdm  # Import tqdm for the progress bar

def parse_arguments():
    if len(argv) != 3:
        print("Usage: scrap-to-csv.py 'source_directory' '<css_selector>'")
        exit(1)
    source_directory = argv[1]
    css_selector = argv[2]
    return source_directory, css_selector

def get_files_in_directory(source_directory):
    files_in_directory = []
    for file_name in listdir(source_directory):
        file_path = join(source_directory, file_name)
        if isfile(file_path):
            files_in_directory.append(file_path)
    return files_in_directory

def process_files(files_list, css_selector):
    extracted_data = []
    # Wrap the files_list with tqdm for the progress bar
    for file_path in tqdm(files_list, desc="Processing files"):
        # Process each file in the list
        data_from_file = process_file(file_path, css_selector)
        extracted_data.extend(data_from_file)
    return extracted_data

def process_file(file_path, css_selector):
    with open(file_path, 'r', encoding='utf-8') as file_handle:
        file_content = file_handle.read()
    data = extract_data(file_content, css_selector)
    return data

def extract_data(html_content, css_selector):
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.select(css_selector)
    data = []
    for element in elements:
        # Extract text from each selected element
        text = element.get_text(strip=True)
        data.append(text)
    return data

def write_to_csv(data):
    with open('scrap.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = writer(csvfile)
        for row in data:
            # Write each data row to the CSV file
            csv_writer.writerow([row])

def main():
    source_directory, css_selector = parse_arguments()
    files_list = get_files_in_directory(source_directory)
    extracted_data = process_files(files_list, css_selector)
    write_to_csv(extracted_data)

if __name__ == "__main__":
    main()
