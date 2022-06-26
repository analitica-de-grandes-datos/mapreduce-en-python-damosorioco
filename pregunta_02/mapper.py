#
# >>> Escriba el codigo del mapper a partir de este punto <<<

import sys 

if __name__ == "__main__":

    for row in sys.stdin:

        campos = row.strip().split(',',5)
        purpose = campos[3]
        amount = campos[4]

    sys.stdout.write("{}\t{}\n".format(purpose, amount))