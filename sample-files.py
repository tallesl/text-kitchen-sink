#!/usr/bin/env python3

from sys import argv, exit
from os import path, makedirs, walk
from shutil import copy2
from random import sample
from os.path import basename

def main():
    # Check if the correct number of arguments is provided
    if not validate_arguments(argv):
        exit(1)

    # Assign command-line arguments to variables
    input_directory = argv[1]
    output_directory = argv[2]
    number_of_samples = parse_number_of_samples(argv[3])

    # Collect all file paths from the input directory
    all_file_paths = collect_all_files(input_directory)

    # Check if there are enough files to sample
    if not has_enough_files(all_file_paths, number_of_samples):
        exit(1)

    # Randomly sample the specified number of file paths
    sampled_file_paths = sample_files(all_file_paths, number_of_samples)

    # Copy the sampled files to the output directory
    copy_sampled_files(sampled_file_paths, output_directory)

def validate_arguments(arguments):
    # Validate the number of command-line arguments
    if len(arguments) != 4:
        print('Usage: ./sample-files.py <input_directory> <output_directory> <number_of_samples>')
        return False
    return True

def parse_number_of_samples(samples_argument):
    # Parse the number of samples from the command-line argument
    try:
        number_of_samples = int(samples_argument)
        return number_of_samples
    except ValueError:
        print('Error: <number_of_samples> must be an integer.')
        exit(1)

def collect_all_files(input_directory):
    all_file_paths = []
    # Walk through the input directory recursively
    for root_directory, _, filenames in walk(input_directory):
        for filename in filenames:
            # Construct the full file path
            file_path = path.join(root_directory, filename)
            all_file_paths.append(file_path)
    return all_file_paths

def has_enough_files(all_file_paths, number_of_samples):
    # Check if there are enough files to sample
    if len(all_file_paths) < number_of_samples:
        print(f'Not enough files to sample. Found {len(all_file_paths)} files.')
        return False
    return True

def sample_files(all_file_paths, number_of_samples):
    # Randomly sample the specified number of file paths
    return sample(all_file_paths, number_of_samples)

def copy_sampled_files(sampled_file_paths, output_directory):
    # Create the output directory if it does not exist
    create_output_directory(output_directory)

    # Iterate over each sampled file path
    for source_file_path in sampled_file_paths:
        filename = basename(source_file_path)
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
