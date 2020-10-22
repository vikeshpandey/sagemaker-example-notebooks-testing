#!/usr/bin/env python3
import argparse
import os
import sys

#import sagemakerci.git

from github import Github

def parse_args(args):
    parser = argparse.ArgumentParser(os.path.basename(__file__))
    parser.set_defaults(func=lambda x: parser.print_usage())
    parser.add_argument("--pr", help="Pull request number", type=int, required=True)

    parsed = parser.parse_args(args)
    if not parsed.pr:
        parser.error("--pr required")

    return parsed

def is_notebook(filename):
    root, ext = os.path.splitext(filename)
    return ext == ".ipynb"

def main():
    args = parse_args(sys.argv[1:])

    #token = sagemakerci.git.Git().oauth.token
    g = Github()#token)
    repo = g.get_repo("aws/amazon-sagemaker-examples")
    pr = repo.get_pull(args.pr)
    filenames = filter(is_notebook, [file.filename for file in pr.get_files()])
    filenames_string = " ".join(filenames)
    print(filenames_string)  # This returns the string to bash scripts calling this python script


if __name__ == "__main__":
    main()
