#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    list_value = []

    for line in sys.stdin:

        key, val = line.split('\t')
        val = float(val)

        if key == curkey:

            list_value.append(val)

        else:

            if curkey is not None:

                max_value = max(list_value)
                min_value = min(list_value)

                list_value.clear()

                sys.stdout.write("{}\t{}\t{}\n",format(curkey, max_value, min_value))

            curkey = key
            list_value.append(val)

    max_value = max(list_value)
    min_value = min(list_value)

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, max_value, min_value))

