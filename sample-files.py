#!/usr/bin/env python3

import argparse
from os import listdir, makedirs
from os.path import isfile, join
import shutil
import uuid

def get_all_files_in_directory(directory_path):
    # Retrieve all files in the specified directory.
    file_paths = [
        join(directory_path, file_name)
        for file_name in listdir(directory_path)
        if isfile(join(directory_path, file_name))
    ]
    return file_paths

def sample_files(file_paths, output_directory, sample_size):
    # Copy a specified number of files to the output directory with unique names.
    makedirs(output_directory, exist_ok=True)
    
    for index, file_path in enumerate(file_paths[:sample_size]):
        # Create a unique destination file name
        destination_file_name = f"{uuid.uuid4()}_{index}"
        destination_path = join(output_directory, destination_file_name)
        
        # Copy the file to the destination path
        shutil.copy(file_path, destination_path)

def main(input_directory, output_directory, sample_size):
    # Main function to handle file sampling.
    # Collect all files from the input directory
    all_files = get_all_files_in_directory(input_directory)
    
    # Copy a sample of files to the output directory
    sample_files(all_files, output_directory, sample_size)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Sample a specified number of files from a directory.")
    parser.add_argument("input_directory", help="Directory to sample files from")
    parser.add_argument("output_directory", help="Directory to save sampled files to")
    parser.add_argument("sample_size", type=int, help="Number of files to sample")
    
    args = parser.parse_args()
    
    # Call main function with parsed arguments
    main(args.input_directory, args.output_directory, args.sample_size)
