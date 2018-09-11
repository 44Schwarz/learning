import argparse
import os
import tempfile
import json

storage = dict()

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
print(args.key, args.val)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if args.val is not None:
    with open(storage_path, 'w') as f:
        f.write(json.dumps({args.key: args.val}))
else:
    with open(storage_path, 'r') as f:
        storage = dict()
        # storage = f.read()
        print(f.read())
