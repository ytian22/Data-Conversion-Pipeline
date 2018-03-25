import json
import sys
import numpy as np
import pandas as pd
import mycsv
import os


def json2csv():
    data = mycsv.getdata()

    my_json = json.loads(data)
    header = my_json["headers"]
    header = [i.replace("_", " ") for i in header]

    values_set = []

    for i in header:
        values = []
        for j in range(len(my_json["data"])):
            values.append(eval('my_json["data"][%d]["%s"]' % (j,i)))
        values_set.append(values)
    table = np.array(values_set)

    a = np.transpose(table)
    b = pd.DataFrame(data=a, columns=header)
    return b.to_csv(sys.stdout, sep = ",", header = header, index = False)

json2csv()