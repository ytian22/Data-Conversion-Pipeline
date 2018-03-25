import mycsv


def csv2html():
    header, data = mycsv.readcsv(mycsv.getdata())
    start = "<html>\n<body>\n<table>\n"
    end = "</table>\n</body>\n</html>"
    header_row = "".join(["<th>%s</th>" % i for i in header])
    header_row = "<tr>%s</tr>\n" % header_row
    data_row_set = []
    for i in data:
        data_row = "".join(["<td>%s</td>" % j for j in i])
        data_row_set.append("<tr>%s</tr>\n" % data_row)
    data_row_set = "".join(data_row_set)
    together = start + header_row + data_row_set + end
    return together

print csv2html()