import mycsv


def csv2xml():
    header, data = mycsv.readcsv(mycsv.getdata())
    start = '<?xml version="1.0"?>\n<file>'
    end = "\n</file>"
    header2 = [i.replace(" ", "_") for i in header]
    header_body = "\n  <headers>%s</headers>" % (",".join([header[i] for i in range(len(header))]))

    data_body3 = []
    data_body4 = []

    for j in data:
        data_body2 = []
        for i in range(len(header2)):
            data_body = "<%s>%s</%s>" % (header2[i], j[i], header2[i])
            data_body2.append("".join(data_body))
            data_body3 = "\n    <record>\n      %s\n    </record>" % ("".join(data_body2))
        data_body4.append(data_body3)
    data_body_final = "\n  <data>%s\n  </data>" % "".join(data_body4)

    together = start + header_body + data_body_final + end
    return together

print csv2xml()
