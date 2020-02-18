filepath = "diagram_1.bpmn"
substring = "<bpmn:documentation>Feature: "
filename = ""
with open(filepath) as fp:
    line = fp.readline()
    count = 1
    while line:
        if substring in line:
            filename = line.strip()[substring.__len__():]
        line = fp.readline()
        count += 1

print(filename)
