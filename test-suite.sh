#!/bin/bash

for dir in testsuite/*/; do
	python modulr.py $dir 1>/dev/null
	python testsuite/checkresults.py $dir
done

