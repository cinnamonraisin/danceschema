import os
import pytest

import pysdf

examples = pysdf.util.list_examples()


def test_parse_examples():
    def __test_example(example_path):
        assert os.path.exists(example_path)
        sdf = pysdf.load(example_path)
        assert isinstance(sdf, pysdf.StructuredDance)

    for e in examples:
        yield __test_example, e
