# desktop-manager.py
# Copyright Ryan Brue 2023

VERSION = "0.0.1"


import argparse, os
from pathlib import Path


LOCAL_DESKTOP_APP_PATH = Path("~/.local/share/applications/")
DESKTOP_MANAGER_BIN_PATH = Path("~/.desktop-manager/")

def valid_dir(path):
    if os.path.isdir(path):
        return Path(path)
    else:
        raise NotADirectoryError(path)

def valid_file(path):
    if os.path.isfile(path):
        return Path(path)
    else:
        raise FileNotFoundError(path)

def validate_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_file(p_from, p_to):
    os.rename(p_from, p_to)

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
install_parser.add_argument("executable",type=valid_file,help="the path of the executable to install")
install_parser.add_argument("-i","--icon",type=valid_file,required=False,help="the icon of the desktop shortcut")
# UPDATE COMMAND
update_parser = subparsers.add_parser("update",help="update the executable or icon of a managed shortcut")
update_parser.add_argument("-n","--name",help="update the name of the shortcut")
update_parser.add_argument("-e","--executable",type=valid_file,help="update the executable of the shortcut")
update_parser.add_argument("-i","--icon",type=valid_file,help="update the icon of the shortcut")
# REMOVE COMMAND
remove_parser = subparsers.add_parser("remove",help="remove an executable from Desktop Manager")
remove_parser.add_argument("name",help="the name of the desktop shortcut to remove")
remove_parser.add_argument("-s","--save-path",type=valid_dir,help="the path to save the executable and icon to If not specified, the executable and icon are deleted")
# LIST COMMAND
list_parser = subparsers.add_parser("list", help="list app shortcuts managed by Desktop Manager")

args = parser.parse_args()

def install(args):
    target_folder = LOCAL_DESKTOP_APP_PATH.joinpath(Path(f'./{args.name}'))
    print(target_folder)

def update(args):
    pass

def remove(args):
    pass

def list(args):
    pass