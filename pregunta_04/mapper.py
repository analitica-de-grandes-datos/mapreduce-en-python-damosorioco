#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
from dataclasses import fields
import sys

if __name__=='__main__':

    for line in sys.stdin:

        fields = line.strip().split('   ')
        letter = fields[0]

        sys.stdout.write("{}\t1\n".format(letter))

