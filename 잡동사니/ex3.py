#python ex3.py src.txt dst.txt
import sys

fr = open(sys.argv[1], "r")
data = fr.read()

fw = open(sys.argv[2], "w")
fw.write(data)

fw.close()
fr.close()