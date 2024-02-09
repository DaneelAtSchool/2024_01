#-*-coding:utf8;-*-
#qpy:console

for row in range (0, 64):
    rowStr = "%-5i" % (row*31);
    for col in range(0, 31):
        ch = chr(col + row*31);
        if (ch.isprintable()):
            rowStr = rowStr + "%-3s" % ch;
        else:
            rowStr = rowStr + "%-3s" % " ";
    print(rowStr);

