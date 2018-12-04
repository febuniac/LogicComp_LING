import slcl
import sys

if len(sys.argv) == 1:
    print("Usage: %s filename" % __file__)
else:
    with open(sys.argv[1]) as fil:
        slcl.execute(fil.read())
