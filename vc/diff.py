import subprocess

from collections import defaultdict
from tempfile import NamedTemporaryFile as Temp

from . import data

def compare_trees(*trees):
    entries = defaultdict(lambda: [None] * len(trees))
    for i, tree in enumerate(trees):
        for path, oid in tree.items():
            entries[path][i] = oid
    
    for path, oids in entries.items():
        yield (path, *oids)
        
def diff_trees(t_from, t_to):
    output = ''
    for path, o_from, o_to in compare_trees(t_from, t_to):
        if o_from != o_to:
            output += f'changed: {path}\n'
    
    return output

"""
def diff_blobs (o_from, o_to, path='blob'):
    with Temp () as f_from, Temp () as f_to:
        for oid, f in ((o_from, f_from), (o_to, f_to)):
            if oid:
                f.write (data.get_object (oid))
                f.flush ()
        print(f_from.name)
        with subprocess.Popen (
            ['fc', f'{path}', f_from.name, f'{path}', f_to.name],
            stdout=subprocess.PIPE, shell=True) as proc:
            output, _ = proc.communicate ()

        return output
"""