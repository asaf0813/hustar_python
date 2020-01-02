#python ex3.py src.txt dst.txt
import sys
if len(sys.argv) == 3:
    fr = open(sys.argv[1], "r")
    data = fr.read()
    fw = open(sys.argv[2], "w")
    fw.write(data)
    fw.close()
    fr.close()
elif len(sys.argv) == 1:
    print("원본파일명과 사본파일명이 입력되지 않았습니다")
elif len(sys.argv) == 2:
    print("사본파일명이 입력되지 않았습니다")