
import argparse
from helper import *
from categorize import categorize
from organize import organize




        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-cmd","--command", required=True, choices=["categorize", "organize"], help="Choose a command")
    parser.add_argument("-dir","--directory", required=True, help="Target directory")
    parser.add_argument("-cat","--categories",  help="Categories separated by comma")
    args = parser.parse_args()
    if args.command == "categorize":
        print(categorize(args.directory))
    elif args.command == "organize":
        organize(args.directory,categories=args.categories)

    