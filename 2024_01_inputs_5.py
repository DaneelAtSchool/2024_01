#-*-coding:utf8;-*-
#qpy:console

for row in range (0, 64):
    rowStr = "\n%-6i" % (row*31);
    for col in range(0, 31):
        ch = chr(col + row*31);
        if (not ch.isprintable()):
            ch = " ";
        rowStr = rowStr + "%-3s" % ch;
    print(rowStr);
