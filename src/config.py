import toml


def get_config():
    with open('config.toml', 'r') as config_file:
        return toml.load(config_file)
