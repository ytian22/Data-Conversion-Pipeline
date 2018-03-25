import sys


def getdata():
    if len(sys.argv) == 1:  # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read() # a single string
        f.close()
    return data.strip()


def readcsv(data): #input is a single string
    str_split = data.splitlines()
    rows = [i.strip('"') for i in str_split]
    header = rows[0].split(',')
    data = [rows[i].split(',') for i in range(len(rows))]
    data = data[1:]
    return header,data