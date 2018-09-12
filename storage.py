import argparse
import os
import tempfile
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.exists(storage_path):
    f = open(storage_path, 'w')
    f.close()
else:
    with open(storage_path, 'r') as f:
        try:
            storage = json.loads(f.read())
        except:
            storage = dict()

    if args.val is not None:
        if storage.get(args.key):
            storage[args.key].append(args.val)
        else:
            storage[args.key] = [args.val]

        with open(storage_path, 'w') as f:
            f.write(json.dumps(storage))
    else:
        print(', '.join(storage.get(args.key, [])))
