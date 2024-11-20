#!/usr/bin/env python3

from sys import exit
from os.path import isdir, exists, join, basename, splitext, dirname
from os import makedirs, walk
from shutil import copy2
from fnmatch import fnmatch
from argparse import ArgumentParser
from tqdm import tqdm


def main():
    args = parse_arguments()

    if not isdir(args.input_directory):
        print(f'Error: Input directory "{args.input_directory}" does not exist or is not a directory.')
        exit(1)

    if exists(args.output_directory) and not isdir(args.output_directory):
        print(f'Error: Output path "{args.output_directory}" exists but is not a directory.')
        exit(1)

    if not args.file_pattern.strip():
        print('Error: File pattern cannot be empty.')
        exit(1)

    copy_matched_files(args.input_directory, args.output_directory, args.file_pattern)


def parse_arguments():
    parser = ArgumentParser(description='Copy files matching a pattern from one directory to another, flattening the structure.')
    parser.add_argument('input_directory', help='The source directory to search for files')
    parser.add_argument('output_directory', help='The destination directory to copy files into')
    parser.add_argument('file_pattern', help='The file pattern to match (e.g., *.txt)')
    return parser.parse_args()


def copy_matched_files(input_directory, output_directory, file_pattern):
    create_output_directory(output_directory)

    matched_files = []
    for root, _, files in walk(input_directory):
        for file in files:
            if fnmatch(file, file_pattern):
                source = join(root, file)
                matched_files.append(source)

    with tqdm(total=len(matched_files), desc='Copying files', unit='file') as progress_bar:
        for source in matched_files:
            destination = resolve_filename_conflict(join(output_directory, basename(source)))
            copy_file(source, destination)
            progress_bar.update(1)


def create_output_directory(output_directory):
    if not exists(output_directory):
        makedirs(output_directory)


def resolve_filename_conflict(destination):
    if not exists(destination):
        return destination

    base, ext = splitext(basename(destination))
    directory = dirname(destination)
    count = 1

    while True:
        new_name = f'{base}_{count}{ext}'
        new_path = join(directory, new_name)
        if not exists(new_path):
            return new_path
        count += 1


def copy_file(source, destination):
    try:
        copy2(source, destination)
    except UnicodeEncodeError as e:
        print(e)


if __name__ == '__main__':
    main()
