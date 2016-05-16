import glob
import os

import pysdf

EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "examples")
EXAMPLE_FILES = glob.glob(os.path.join(EXAMPLE_DIR, "*.json"))


def test_load_examples():
    examples = pysdf.util.list_examples()
    assert len(examples) == len(EXAMPLE_FILES)


    assert set([os.path.basename(x) for x in examples]) == \
        set([os.path.basename(x) for x in EXAMPLE_FILES])
