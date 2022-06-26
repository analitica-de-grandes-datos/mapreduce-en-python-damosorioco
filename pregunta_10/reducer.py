#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from ntpath import join
import sys

if __name__ == "__main__":

    letters = dict()

    for line in sys.stdin:

        value, letter = line.split("\t")
        letter = letter.strip().split(",")

        for x in letter:

            if x not in letters.keys():

                letters[x] = value

            else:

                letters[x] = letters[x] + ',' + value

        tuple = sorted(letters.items(), key = lambda y: y[0])

    for letter1, number_related in tuple:

        unord_number = number_related.split(',')
        ord_number = sorted(unord_number, key=int)
        ord_number = ','.join(ord_number)

        sys.stdout.write("{}\t{}\n".format(letter1, ord_number))