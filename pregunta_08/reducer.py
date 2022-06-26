#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from statistics import mean
import sys


if __name__ == "__main__":

    curkey = None
    list_value = []

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:

            list_value.append(val)

        else:

            if curkey is not None:

                suma = sum(list_value)
                avg = mean(list_value)
                list_value.clear()
                
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, avg))

            curkey = key
            list_value.append(val)

    suma = sum(list_value)
    avg = mean(list_value)

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, avg))

