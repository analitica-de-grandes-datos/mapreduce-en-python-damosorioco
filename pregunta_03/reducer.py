#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator
if _name_ == '_main_':
    dict_from_list = {}

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
        

        dict_from_list[key] = val

        sorted_= sorted(dict_from_list.items(), key=operator.itemgetter(1))
        # keys_dict = sorted_.keys()
        # sorted_list = sorted(dict_from_list.items(), key=lambda x: x[1])
        # complete = key + "," + val

    for elemento in sorted_:
        sys.stdout.write("{},{}\n".format(elemento[0], elemento[1]))
    # print(sorted_)