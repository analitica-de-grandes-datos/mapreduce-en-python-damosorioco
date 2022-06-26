#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
from dataclasses import field, fields
import sys

if __name__ == '__main__':

    for line in sys.stdin:

        fields = line.strip().split('   ')

        letter = fields[0]
        values = fields [2]
        dates = fields[1]

        sys.stdout.write('{}\t{}t{}\n'.format(letter, dates, values))