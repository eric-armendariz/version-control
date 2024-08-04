import os
import hashlib

GIT_DIR = '.vc'

def init():
    os.mkdir(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')
    
def hash_object(data, type_ = 'blob'):
    obj = type_.encode() + b'\x00' + data
    hash_obj = hashlib.sha1(obj).hexdigest()
    
    with open(f'{GIT_DIR}/objects/{hash_obj}', 'wb') as out:
        out.write(obj)
    return hash_obj

def get_object(obj, expected = 'blob'):
    with open(f'{GIT_DIR}/objects/{obj}', 'rb') as f:
        obj = f.read()
        
    type_, _, content = obj.partition(b'\x00')
    type_ = type_.decode()
    
    if expected is not None:
        assert expected == type_, f'Expected {expected}, got {type_}'
    return content

def update_ref(ref, oid):
    ref_path = f'{GIT_DIR}/{ref}'
    os.makedirs(os.path.dirname(ref_path), exist_ok=True)
    with open(ref_path, 'w') as f:
        f.write(oid)
        
def get_ref(ref):
    ref_path = f'{GIT_DIR}/{ref}'
    if os.path.isfile(ref_path):
        with open(ref_path) as f:
            return f.read().strip()

def iter_refs():
    refs = ['HEAD']
    for root, _, filenames in os.walk(f'{GIT_DIR}/refs/'):
        root = os.path.relpath(root, GIT_DIR)
        refs.extend(f'{root}/{name}' for name in filenames)
    
    for refname in refs:
        yield refname, get_ref(refname)