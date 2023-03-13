#!/bin/bash
v=$(fgrep __version__ JpegIPTC.py| cut -d"'" -f2)
rm -f dist/JpegIPTC-${v}.tar.gz dist/JpegIPTC-${v}-py3-none-any.whl
python3 -m build --sdist .
python3 -m build --wheel .
twine upload dist/JpegIPTC-${v}.tar.gz dist/JpegIPTC-${v}-py3-none-any.whl
