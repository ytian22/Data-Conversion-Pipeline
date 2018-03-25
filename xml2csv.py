import untangle
import sys
import mycsv
import numpy as np
import pandas as pd
import os


def xml2csv():
    data = mycsv.getdata()

    xml = untangle.parse(data)
    header = xml.file.headers.cdata.split(",")
    header2 = [i.replace(" ", "_") for i in header]

    values_set = []

    for i in header2:
        content = "record.%s.cdata" % i
        values = []
        for record in xml.file.data.record:
            values.append(eval(content))
        values_set.append(values)
    table = np.array(values_set)
    table = [",".join(j) for j in table]

    new_set = []
    for i in range(len(table)):
        new = table[i].split(",")
        new_set.append(new)

    a = np.transpose(new_set)
    b = pd.DataFrame(data = a, columns= header)
    return b.to_csv(sys.stdout, sep = ",", header = header, index = False)

xml2csv()