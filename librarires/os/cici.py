import os
import argparse

def walk_tree(path, ignores=None, prefix=""):
    ignores = ignores or []
    entries = [
        e for e in os.scandir(path) 
        if not any(
            (ig in e.path) 
            for ig in ignores
            )
        ]
    entries.sort(key=lambda e: e.name.lower())  # optional: sort by name

    for index, entry in enumerate(entries):
        connector = "└── " if index == len(entries) - 1 else "├── "
        print(prefix + connector + entry.name)

        if entry.is_dir():
            extension = "    " if index == len(entries) - 1 else "│   "
            walk_tree(entry.path, ignores, prefix + extension)

# root = r"C:\Users\victo\codes_real\making\python"
# walk_tree(root, ignores=[".git", "__pycache__"])

parseManger = argparse.ArgumentParser(description="tree walker")

# first argument is compulsory so:
parseManger.add_argument("--file", "-f", help="Enter a valid file absolute path")

# we for ignore:
parseManger.add_argument("--ignore", "-i", help="Enter strings you want to avoid in paths of any directory here. Example: '.git' ignores the ./.git directory and it's subdirectories entirely", default=None)

args = parseManger.parse_args()

walk_tree(args.file, ignores = args.ignore)