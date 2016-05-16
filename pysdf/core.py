"""
pySDF Python API
================

This library provides an interface for reading Structured Dance Format json
files into Python, or creating them programatically.

Much of this document / repo borrowed from
https://github.com/marl/jams/blob/master/jams/core.py

Example of how to use this:
>>> import pysdf
>>> ex = pysdf.util.list_examples()
>>> an_example = pysdf.load(ex[0])
>>> an_example
StructuredDance(title='Rufty Tufty')
"""

from __future__ import print_function

import copy
import json
import jsonschema
import logging
import pprint
import six

from .version import version as __VERSION__
from . import schema
from .exceptions import sdfError, SchemaError, ParameterError

__all__ = ['load', 'StructuredDance']

logger = logging.getLogger(__name__)


def load(path_or_file, validate=True, strict=True):
    """Load a Dance (or list of dances) from a json file.

    Parameters
    ----------
    path_or_file : str or file-like
        Path to the SDF file to load
        OR
        An open file handle to load from.

    validate : bool
        Attempt to validate the SDF object

    strict : bool
        if `validate==True`, enforce strict schema validation

    Returns
    -------
    sdf : StructuredDance
        The loaded StructuredDance object.

    Raises
    ------
    SchemaError
        if `validate==True`, `strict==True` and validation fails
    """
    with open(path_or_file, mode='r') as fp:
        sdf = StructuredDance(**json.load(fp))

    if validate:
        sdf.validate(strict=strict)

    return sdf


class StructuredDance(object):
    """The Dance Container."""
    __SCHEMA__ = schema.SDF_SCHEMA

    def __init__(self, **kwargs):
        """
        Parameters
        ----------
        kwargs : dict
            The json k:v pairs
        """
        self.data = copy.deepcopy(kwargs)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def __getitem__(self, key):
        return self.data.get(key)

    def __getattr__(self, key):
        return self.data.get(key)

    def __setitem__(self, key, value):
        self.data[key] = value

    def keys(self):
        return self.data.keys()

    def __repr__(self):
        return "StructuredDance(title='{}')".format(
            self['title'])

    def pformat(self):
        return pprint.pformat(self.data)

    def validate(self, strict=True):
        """Validate this object against the schema."""
        try:
            jsonschema.validate(self.data, self.__SCHEMA__)
            return True
        except jsonschema.ValidationError as e:
            logger.error(e)
            if strict:
                raise SchemaError(e)
            else:
                return False

    def to_builtin(self):
        """Return this dance as a dict."""
        return self.data
