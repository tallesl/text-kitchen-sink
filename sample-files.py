#!/usr/bin/env python3

from argparse import ArgumentParser
from os import listdir, makedirs
from os.path import isfile, join
from shutil import copy
from random import sample


def get_files_only(directory):
    files_and_subdirs = [join(directory, f) for f in listdir(directory)]
    only_files = [f for f in files_and_subdirs if isfile(f)]

    return only_files


def copy_all(source_filepaths, target_directory):
    makedirs(target_directory, exist_ok=True)
    
    for f in source_filepaths:
        filename = f.split('/')[-1]
        destination_path = join(target_directory, filename)

        copy(f, destination_path)


if __name__ == '__main__':
    parser = ArgumentParser(description='Sample and copy a specified number of files from a directory.')
    parser.add_argument('source_directory', help='Directory containing files to sample')
    parser.add_argument('target_directory', help='Directory to copy sampled files to')
    parser.add_argument('number_of_samples', type=int, help='Number of files to sample')
    
    args = parser.parse_args()
    
    source_filepaths = get_files_only(args.source_directory)
    sample_filepaths = sample(source_filepaths, args.number_of_samples)

    copy_all(sample_filepaths, args.target_directory)
