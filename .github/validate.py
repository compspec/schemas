#!/usr/bin/env python3

import sys
import os
import re
import json
import jsonschema

here = os.path.abspath(__file__)
root = os.path.dirname(os.path.dirname(here))

# Validation for the compspec.json files, a compatibility group schema,
# is done with an existing standard, json graph format
schema_file = os.path.join(root, "json-graph-schema_v2.json")
example_schema_file = os.path.join(root, "schema.json")


def recursive_find(base, basename="compspec.json"):
    """
    Find all compspec.json below a root
    """
    for root, _, filenames in os.walk(base):
        for filename in filenames:
            fullpath = os.path.join(root, filename)
            if filename == basename:
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
    example_schema = read_json(example_schema_file)

    for spec_file in specs:
        print(f"⭐️ Validating spec {spec_file}")
        spec = read_json(spec_file)
        jsonschema.validate(spec, schema=schema)

    # Validate examples
    for example in os.listdir(os.path.join(root, "example")):
        fullpath = os.path.join(root, "example", example)
        print(f"⭐️ Validating example {example}")
        spec = read_json(fullpath)
        jsonschema.validate(spec, schema=example_schema)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        root = sys.argv[1]
    main(root)
