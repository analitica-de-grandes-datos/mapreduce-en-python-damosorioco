#
# >>> Escriba el codigo del mapper a partir de este punto <<<

import sys 

if __name__ == "__main__":

    for line in sys.stdin:

        campos = line.strip().split(',',5)
        purpose = campos[3]
        amount = campos[4]

    sys.stdout.write("{}\t{}\n".format(purpose, amount))