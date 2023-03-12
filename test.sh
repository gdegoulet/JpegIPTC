#!/bin/bash

clean_up () {
rm -f 1 2 3 4 5 6 7 8 test.jpg test2.jpg test3.png test4.png
}

clean_up

./test.py
echo
echo -----------------------------------------------------------

iptc 76bde3fc961f0fa8733756922d1e2ed06311d804ec38b89dc60d6ba36d30e046.jpg 2>/dev/null | sed 1d > 1
iptc test.jpg 2>/dev/null | sed 1d > 2
diff 1 2
test $? -eq 0 && echo "TEST1 : OK"

iptc iptc-logo.png 2>/dev/null | sed 1d > 3
iptc test2.jpg 2>/dev/null | sed 1d > 4
diff 3 4
test $? -eq 0 && echo "TEST2 : OK"

md5sum iptc-logo.png |awk '{print $1}' > 5
md5sum test3.png |awk '{print $1}' > 6
diff 5 6
test $? -eq 0 && echo "TEST3 : OK"

md5sum iptc-logo.png |awk '{print $1}' > 7
md5sum test4.png |awk '{print $1}' > 8
diff 7 8
test $? -eq 0 && echo "TEST4 : OK"

clean_up

