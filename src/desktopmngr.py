# desktopmngr.py
# Copyright Ryan Brue 2022

VERSION = "0.0.1"

import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Command-line utility to create and manage custom .desktop applications in Linux!"
)
subparsers = parser.add_subparsers(help="sub command help")
###############################
# Actions for Desktop Manager #
###############################
# INSTALL COMMAND
install_parser = subparsers.add_parser("install",help="Add an executable to Desktop Manager.")
install_parser.add_argument("path",help="The path of the executable to install.")
install_parser.add_argument("name",help="The name of the desktop shortcut.")
install_parser.add_argument("-i","--icon",required=False,help="The icon of the desktop shortcut.")
# REMOVE COMMAND
remove_parser = subparsers.add_parser("remove",help="Remove an executable from Desktop Manager.")
remove_parser.add_argument("name",help="The name of the desktop shortcut to remove.")
remove_parser.add_argument("-s","--save-path",help="The path to save the executable and icon to. If not specified, the executable and icon are deleted.")
# LIST COMMAND
list_parser = subparsers.add_parser("list", help="List app shortcuts managed by Desktop Manager.")



args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)