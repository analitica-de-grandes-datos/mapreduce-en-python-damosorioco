#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
from dataclasses import field, fields
import sys

from sqlalchemy import values

if __name__ == '__main__':

    for line in sys.stdin:

        fields = line.strip().split('   ')

        letter = fields[0]
        dates = fields[1]
        values = fields[2]

        sys.stdout.write('{}\t{}t{}\n'.format(letter, dates, values))