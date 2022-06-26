#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__=='__main__':

    for line in sys.stdin:

        campos = line.strip().split('   ')
        letter = campos[0]

        sys.stdin.write("{}\t1\n".format(letter))
        
