# Compspec

This is a prototype repository for compatibility specifications that are being worked on by the [OCI compatibility working group](https://github.com/opencontainers/wg-image-compatibility). While that work is underway (and the structure and format of these metadata to be determined. For the time being we have defined two things:

- A **compatibility schema** is a graph (nodes and edges) that defines a space of metadata and relationships for compatibility attributes
- A **compatibility spec** is a specific extraction of these metadata attributes for a given application or container image

## JSON Schema Specifications

 - The [JGF schema](https://github.com/jsongraph/json-graph-specification) version 2.0 is used to validate the compatibility schemas (compspec.json) files, which are essentially graphs with nodes and edges. Every node is required to be present in the graph.
 - The [schema.json](schema.json) is used to validate a compatibility spec using one or more compatibility schemas

Both of the above are based on proposals [C](https://github.com/opencontainers/wg-image-compatibility/pull/8) and [D](https://github.com/opencontainers/wg-image-compatibility/pull/9) of the Image Compatibility working group, with a stronger orientation toward D to honor the graph. This, however, means that everything is subject to change. This repository is for prototyping only!

## Organization

The different subdirectories of compatibility families (sets of metadata owned by different groups).

Likely these metadata can be moved to be owned properly by the group. They are all kept here for the time being for ease of access. Also for the time being, we have represented the entire set of labels (and smaller namespaces) for one compatibiilty family (e.g., supercontainers) in one JSON file, and of course this is subject to change. 

## History

The original discussion and labels were discussed [in this Google Document](https://docs.google.com/document/d/1THOPd-QUbcFAK7JCkKAjKF7BZlsdV7Qvjxv25PyejIU/edit?usp=sharing) and many of those were derived from a talk by [Christian Kniep](https://archive.fosdem.org/2023/schedule/event/metahub/) at FOSDEM.
