#!/bin/python

from pathlib import Path

# TODO: Replace with argparse
import sys
testrun_root = Path(sys.argv[1])

output_root = testrun_root / "site"
expect_root = testrun_root / "expected"

for root, dirs, files in output_root.walk(on_error=print):
    filepaths = [root / file for file in files]
    for fp in filepaths:
        str_dirpath = str(root).removeprefix(str(output_root)).removeprefix("/")
        expect_dir = expect_root / str_dirpath
        expect_fp = expect_dir / fp.name
        with fp.open("r") as output_file:
            with expect_fp.open("r") as expect_file:
                assert output_file.read() == expect_file.read()
print("Test Passed: {}".format(testrun_root))
