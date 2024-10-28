#!/usr/bin/env python3

from sys import argv, exit
from os import path, makedirs, walk
from shutil import copy2
from fnmatch import fnmatch

def main():
    # Check if the correct number of arguments is provided
    if not validate_arguments(argv):
        exit(1)

    # Assign command-line arguments to variables
    input_directory = argv[1]
    output_directory = argv[2]
    file_pattern = argv[3]

    # Start the file copying process
    copy_matched_files(input_directory, output_directory, file_pattern)

def validate_arguments(arguments):
    # Validate the number of command-line arguments
    if len(arguments) != 4:
        print('Usage: ./find-and-flatten.py <input_directory> <output_directory> <pattern>')
        return False
    return True

def copy_matched_files(input_directory, output_directory, file_pattern):
    # Create the output directory if it does not exist
    create_output_directory(output_directory)

    # Walk through the input directory recursively
    for root_directory, _, filenames in walk(input_directory):
        for filename in filenames:
            # Check if the filename matches the given pattern
            if is_pattern_matched(filename, file_pattern):
                source_file_path = path.join(root_directory, filename)
                destination_file_path = path.join(output_directory, filename)

                # Resolve any filename conflicts
                destination_file_path = resolve_filename_conflict(destination_file_path)

                # Copy the file to the destination
                copy_file(source_file_path, destination_file_path)

def create_output_directory(output_directory):
    # Check if the output directory exists
    if not path.exists(output_directory):
        # Create the output directory
        makedirs(output_directory)

def is_pattern_matched(filename, file_pattern):
    # Return True if the filename matches the pattern
    return fnmatch(filename, file_pattern)

def resolve_filename_conflict(destination_file_path):
    # If the destination file does not exist, return the original path
    if not path.exists(destination_file_path):
        return destination_file_path

    # Extract the base name and extension
    base_filename = path.basename(destination_file_path)
    base_name, extension = path.splitext(base_filename)
    directory = path.dirname(destination_file_path)
    duplicate_count = 1

    # Increment the filename until a unique one is found
    while True:
        new_filename = f'{base_name}_{duplicate_count}{extension}'
        new_destination = path.join(directory, new_filename)
        # Check if the new destination file exists
        if not path.exists(new_destination):
            return new_destination
        duplicate_count += 1

def copy_file(source_file_path, destination_file_path):
    # Copy the source file to the destination
    copy2(source_file_path, destination_file_path)
    # Print the copy action
    print(f'Copied {source_file_path} to {destination_file_path}')

if __name__ == '__main__':
    main()
