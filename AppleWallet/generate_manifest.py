import hashlib
import json
import os

def generate_manifest():
    manifest = {}
    for root, _, files in os.walk('.'):
        for file in files:
            if file == 'manifest.json' or file == 'generate_manifest.py':
                continue
            with open(file, 'rb') as f:
                file_hash = hashlib.sha1(f.read()).hexdigest()
                manifest[file] = file_hash

    with open('manifest.json', 'w') as f:
        json.dump(manifest, f, indent=4)

generate_manifest()
