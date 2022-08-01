from pathlib import Path


def get_resource_path(resources_filename):
    return str(
        Path(__file__)
        .parent
        .joinpath(f'resources/{resources_filename}')
    )
