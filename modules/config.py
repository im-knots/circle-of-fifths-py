import yaml

def parse_args():
    """ Parse config.yaml """
    yaml_file = yaml.safe_load(open('config.yaml').read())
    yaml_config = yaml_file.get('config')

    # Get configs
    logLevel = yaml_config.get('logLevel')

    return yaml_config