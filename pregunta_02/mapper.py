#
# >>> Escriba el codigo del mapper a partir de este punto <<<

import sys 

if __name__=='__main__':

    for row in sys.stdin:

        sys.stdout.write("{}\t{}\n".format(line.split(',')[3], line.split(',')[4]))
        