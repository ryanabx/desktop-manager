# desktop-manager.py
# Copyright Ryan Brue 2022

VERSION = "0.0.1"

import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description="command-line utility to create and manage custom '.desktop' applications in Linux!"
)
subparsers = parser.add_subparsers(title="actions",description="valid actions",help="sub command help")
###############################
# Actions for Desktop Manager #
###############################
# INSTALL COMMAND
install_parser = subparsers.add_parser("install",help="add an executable to Desktop Manager")
install_parser.add_argument("name",help="the name of the desktop shortcut")
install_parser.add_argument("executable",help="the path of the executable to install")
install_parser.add_argument("-i","--icon",required=False,help="the icon of the desktop shortcut")
# UPDATE COMMAND
update_parser = subparsers.add_parser("update",help="update the executable or icon of a managed shortcut")
update_parser.add_argument("-n","--name",help="update the name of the shortcut")
update_parser.add_argument("-e","--executable",help="update the executable of the shortcut")
update_parser.add_argument("-i","--icon",help="update the icon of the shortcut")
# REMOVE COMMAND
remove_parser = subparsers.add_parser("remove",help="remove an executable from Desktop Manager")
remove_parser.add_argument("name",help="the name of the desktop shortcut to remove")
remove_parser.add_argument("-s","--save-path",help="the path to save the executable and icon to If not specified, the executable and icon are deleted")
# LIST COMMAND
list_parser = subparsers.add_parser("list", help="list app shortcuts managed by Desktop Manager")



args = parser.parse_args()

def install(args):
    pass

def update(args):
    pass

def remove(args):
    pass

def list(args):
    pass