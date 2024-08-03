import argparse
import os
from . import data
import sys

def main ():
    args = parse_args()
    args.func(args)
    
def parse_args():
    parser = argparse.ArgumentParser()
    
    commands = parser.add_subparsers(dest='command')
    commands.required = True
    
    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)
    
    pull_parser = commands.add_parser('pull')
    pull_parser.set_defaults(func=pull)
    
    hash_obj_parser = commands.add_parser('hash-object')
    hash_obj_parser.set_defaults(func=hash_object)
    hash_obj_parser.add_argument('file')
    
    cat_file_parser = commands.add_parser('cat-file')
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument('object')
    
    return parser.parse_args()

def init(args):
    data.init()
    print(f'Initialized empty VC repository in {os.getcwd()}/{data.GIT_DIR}')
    
def pull(args):
    print("Pulling repository!")
    
def hash_object(args):
    with open(args.file, 'rb') as f:
        print(data.hash_object(f.read()))

def cat_file(args):
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(args.object))