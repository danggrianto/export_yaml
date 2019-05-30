# export_yaml

`export_yaml` is a python scripts to read yaml file and convert it to bash file
to be sourced later

## Installation

`pip install export-yaml`

## How to use

```
export YAML_FILE=path_to_yaml
source $(export_yaml)
```

## YAML File configuration
```
---
env:
  HELLO: "world"
```
Note: `export_yaml` is going only to read everything under `env`

