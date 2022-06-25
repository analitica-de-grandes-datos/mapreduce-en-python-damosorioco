#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if _name_ == "_main_":

# itera sobre cada linea de codigo recibida
# a traves del flujo de entrada

  for line in sys.stdin:

    #Eliminar vacíos
    clean = line.strip()

    col = clean.split(',')
    col_1 = col[0]
    col_2 = col[1]

  # escribe al flujo estandar de salida

    # print ('%s, %s' %  (col_1, col_2))
    print ('%s\t%s' % (col_1, col_2))