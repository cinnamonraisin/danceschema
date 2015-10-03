"""
pySDF Python API
================

This library provides an interface for reading Structured Dance Format json
files into Python, or creating them programatically.

Much of this document / repo borrowed from
https://github.com/marl/jams/blob/master/jams/core.py
"""

import json
import jsonschema

import six
import warnings

from .version import version as __VERSION__
from . import schema
from .exceptions import sdfError, SchemaError, ParameterError

__all__ = ['load', 'JSONObject', 'StructuredDance']


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
    with _open(path_or_file, mode='r') as fp:
        sdf = StructuredDance(**json.load(fp))

    if validate:
        sdf.validate(strict=strict)

    return sdf


class JSONObject(object):
    """Dict-like object for JSON Serialization.
    """
    pass


class StructuredDance(JSONObject):
    """The Dance Container."""
    pass
