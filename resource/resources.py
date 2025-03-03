import tests
import os
from pathlib import Path


def resource_path(file_name):
    return str(Path(__file__).parent.joinpath(f'{file_name}').absolute())

# def resource_path(filename):
#     return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
