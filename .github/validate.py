#!/usr/bin/env python3

import sys
import os
import re
import json
import jsonschema

here = os.path.abspath(__file__)
root = os.path.dirname(os.path.dirname(here))

schema_file = os.path.join(root, "definition-schema.json")

def recursive_find(base, pattern="compspec.json"):
    """
    Find all compspec.json below a root
    """
    for root, _, filenames in os.walk(base):
        for filename in filenames:
            fullpath = os.path.join(root, filename)
            if re.search(pattern, fullpath):
                yield fullpath


def read_json(filename):
    with open(filename, "r") as fd:
        content = json.loads(fd.read())
    return content


def main(root):
    """
    Validate the format of WIP prototype specs.
    """
    root = os.path.abspath(root)
    if not os.path.exists(root):
        sys.exit(f"{root} does not exist.")
    specs = recursive_find(root)

    schema = read_json(schema_file)
    for spec_file in specs:
        print(f"⭐️ Validating spec {spec_file}")
        spec = read_json(spec_file)
        jsonschema.validate(spec, schema=schema)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        root = sys.argv[1]
    main(root)
