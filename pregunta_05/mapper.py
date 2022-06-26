#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
from calendar import month
from dataclasses import fields
import sys

if __name__ == '__main__':

    for line in sys.stdin:

        fields = line.strip().split('   ')
        dates = fields[1]
        split_dates = dates.split('-')
        month = split_dates[1]

        sys.stdout.write("{}\t\n".format(month))