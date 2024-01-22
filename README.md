# Compspec

This is a prototype repository for compatibility specifications that are being worked on by the [OCI compatibility working group](https://github.com/opencontainers/wg-image-compatibility). While that work is underway (and the structure and format of these metadata to be determined. For the time being we have defined:

## JSON Schema Specifications

 - [schema.json]schema.json) is used to validate the format of a json defining compatibiilty.
 - [definition-schema.json](definition-schema.json) is to validate the format of the keys for each namespace (in the subdirectories here) 

Both of the above are based on [Proposal C](https://github.com/opencontainers/wg-image-compatibility/pull/8) of the Image Compatibility working group, and everything is subject to change. This repository is for prototyping only.

## Organization

The different subdirectories of compatibility families (sets of metadata owned by different groups).

Likely these metadata can be moved to be owned properly by the group. They are all kept here for the time being for ease of access. Also for the time being, we have represented the entire set of labels (and smaller namespaces) for one compatibilty family (e.g., supercontainers) in one JSON file, and of course this is subject to change. I am also keeping things simple - for now each compatibility family has different groups that can define one or more key value pairs, and those pairs must be strings. This means that numbers will need to be parsed from strings by any respective tool.

## History

The original discussion and labels were discussed [in this Google Document](https://docs.google.com/document/d/1THOPd-QUbcFAK7JCkKAjKF7BZlsdV7Qvjxv25PyejIU/edit?usp=sharing) and many of those were derived from a talk by [Christian Kniep](https://archive.fosdem.org/2023/schedule/event/metahub/) at FOSDEM.
