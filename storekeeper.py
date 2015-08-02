from module.duplicates import search_duplicates
from pprint import pprint
import argparse
import os


def r_dir(prospective_dir):
    if not os.path.isdir(prospective_dir):
        raise Exception("readable_dir:{0} is not a valid path".format(prospective_dir))
    if not os.access(prospective_dir, os.R_OK):
        raise Exception("readable_dir:{0} is not a readable dir".format(prospective_dir))

    return prospective_dir


parser = argparse.ArgumentParser(description='A set of tools to facilitate the work with the disk.')
parser.add_argument('command', help='Command to execute', choices=['duplicates'])
parser.add_argument('-t', '--target', help='Target directory', type=r_dir, metavar='DIRECTORY', default=os.getcwd())

parser.add_argument('-v', '--verbose', help='Switch to verbose mode', action='store_true')

args = parser.parse_args()

{
    'duplicates': lambda: pprint(search_duplicates(args.target, args))
}[args.command]()