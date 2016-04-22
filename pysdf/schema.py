import json
import os

from .exceptions import sdfError


def __load_sdf_schema():
    '''Load the schema file from the root of the package.'''

    schema_file = os.path.join(SCHEMA_DIR, 'sdf_schema.json')

    sdf_schema = None
    with open(schema_file, 'r') as fh:
        sdf_schema = json.load(fh)

    if sdf_schema is None:
        raise sdfError('Unable to load SDF Schema')

    return sdf_schema

# Populate the schema
# TODO: figure out how to grab this path from the python package, not from
#  The current file, since that will change if you install it...
SCHEMA_DIR = os.path.join(os.path.dirname(__file__), os.pardir)
SDF_SCHEMA = __load_sdf_schema()
