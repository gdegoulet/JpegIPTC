#!/bin/bash
rm -f test.jpg
./test.py
iptc 76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg | sed 1d > 1
iptc test.jpg | sed 1d > 2
diff 1 2
test $? -eq 0 && echo "OK : same IPTC tags"
rm -f 1 2

