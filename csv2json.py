import mycsv


def csv2json():
    header, data = mycsv.readcsv(mycsv.getdata())
    start = '{\n'
    end = "\n}"

    header_element = ",\n".join(['\t\t"%s"' % header[i] for i in range(len(header))])
    header_body = '\t"headers": [\n' + header_element + "\n\t],"

    data_body3 = []
    data_body4 = []

    for j in data:
        data_body2 = []
        for i in range(len(header)):
            data_body = '\n\t\t\t"%s": "%s"' % (header[i], j[i])
            data_body2.append(data_body)
            data_body3 = "\n\t\t{" + ",".join(data_body2) + "\n\t\t}"
        data_body4.append(data_body3)
    data_body_final = '\n\t"data": [' + ",".join(data_body4) + "\n\t]"

    together = start + header_body + data_body_final + end
    return together

print csv2json()
