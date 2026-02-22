# Configuration settings

import yaml
import os

config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'settings.yaml')

with open(config_path, 'r') as f:
    SETTINGS = yaml.safe_load(f)
