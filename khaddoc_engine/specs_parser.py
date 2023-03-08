import yaml

from dacite import from_dict

from khaddoc_engine.specs import SailorBase

def get_specs_from_file(filepath: str) -> SailorBase:
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)

    conf = from_dict(SailorBase, data)    
    return conf