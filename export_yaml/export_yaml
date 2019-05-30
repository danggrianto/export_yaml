#!/usr/bin/env python3
import yaml
import os
import tempfile

file_path = os.environ['YAML_FILE']

with open(file_path) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

fd, path = tempfile.mkstemp()

with os.fdopen(fd, 'w') as temp:
    for env in config['env']:
        os.environ[env] = config['env'][env]
        os.putenv(env, config['env'][env])
        temp.write('export {}="{}"\n'.format(env, config['env'][env]))

print(path)
