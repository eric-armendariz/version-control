import os
import hashlib

GIT_DIR = '.vc'

def init():
    os.mkdir(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')
    
def hash_object(data, type_ = 'blob'):
    obj = type_ + b'\x00' + data
    hash_obj = hashlib.sha1(obj).hexdigest()
    
    with open(f'{GIT_DIR}/objects/{hash_obj}', 'wb') as out:
        out.write(obj)
    return hash_obj

def get_object(obj, expected = 'blob'):
    with open(f'{GIT_DIR}/objects/{obj}', 'rb') as f:
        obj = f.read()
        
    type_, _, content = obj.partition(b'\x00')
    if expected is not None:
        assert expected == type, f'Expected {expected}, got {type_}'
    return content