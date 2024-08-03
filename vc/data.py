import os
import hashlib

GIT_DIR = '.vc'

def init():
    os.mkdir(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')
    
def hash_object(data):
    hash_obj = hashlib.sha1(data).hexdigest()
    
    with open(f'{GIT_DIR}/objects/{hash_obj}', 'wb') as out:
        out.write(data)
    return hash_obj

def get_object(obj):
    with open(f'{GIT_DIR}/objects/{obj}', 'rb') as f:
        return f.read()