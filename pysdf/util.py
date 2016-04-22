"""Common useful utility functions."""
import glob
import os

EXAMPLE_DIR = os.path.join(
    os.path.dirname(__file__), os.pardir, "examples")


def list_examples(example_dir=EXAMPLE_DIR):
    """Loads all of the examples from the example_dir
    as python dicts.
    """
    files = os.path.join(example_dir, "*.json")
    return [os.path.abspath(x) for x in glob.glob(files)]
