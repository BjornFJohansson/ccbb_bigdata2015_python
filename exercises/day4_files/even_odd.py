

import sys

number = sys.argv[1]
if type(number) != int:
    print "woah no bad!!!!"
    sys.exit()


if number % 2 == 0:
    print "that's even!"
else:
    print "that's odd"