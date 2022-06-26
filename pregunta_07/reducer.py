#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    list_tuples = []

    for line in sys.stdin:

        key, dates, values = line.split('\t')

        values = int(values)
        tuple =  (key, dates, values)
        list_tuples.append(tuple)

    list_tuples = sorted(list_tuples, key=lambda x: (x[0], x[2]))

    for tuple in list_tuples:

        sys.stdout.write('{}  {}   {}\n'.format(tuple[0], tuple [1], tuple[2]))
