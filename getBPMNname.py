filepath = "diagram_1.bpmn"
substring = "<bpmn:documentation>Feature: "
filename = ""
filenameFound = False
with open(filepath) as fp:
    line = fp.readline()
    count = 1
    while line and filenameFound is False:
        if substring in line:
            filename = line.strip()[substring.__len__():]
            filenameFound = True
        line = fp.readline()
        count += 1

print(filename)
