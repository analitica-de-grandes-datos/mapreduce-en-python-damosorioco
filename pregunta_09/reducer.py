#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    list_tuple = []

    for line in sys.stdin:

        key, date, val = line.split('\t')

        val = int(val)
        tuple = (key, date, val)
        list_tuple.append(tuple)

    list_tuple = sorted(list_tuple, key=lambda x: x[2])
    list_tuple_2 = list_tuple[0:6]

    for tuple in list_tuple_2:

        sys.stdout.write("{}   {}   {}\n".format(tuple[0], tuple[1], tuple[2]))
