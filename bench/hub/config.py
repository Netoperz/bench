from __future__ import absolute_import

from collections import MutableMapping
import os.path as osp
import json

from bench.hub.setup  import setup_config
from bench.hub.util   import makedirs

class Config(dict):
    pass
    
def set_config(key, value):
    pconf  = osp.join(path, 'config.json')
    config = Config()

    if not osp.exists(pconf):
        with open(pconf, 'w') as f:
            json.dump(config, f)

    with open(pconf, 'r') as f:
        config = json.load(f)

    with open(pconf, 'w') as f:
        json.dump(config, f)