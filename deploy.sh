#!/bin/bash
# Xiang Wang(ramwin@qq.com)

rm -rf dist/*
python3 setup.py sdist bdist_wheel
twine upload dist/*
