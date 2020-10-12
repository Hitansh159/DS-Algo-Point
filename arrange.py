#!/bin/python

import copy

path_list = [ "./C", "./C-Plus-Plus", "./C#", "./Go", "./Java", 
						"./Javascript", "./Kotlin", "./PHP", "./Python", "./Scala"]

for path in path_list :
  path+="/readme.md"

  lines=[]
  format_line=[]

  with open(path) as f:
    for i,line in enumerate(f):
      if line == '\n' :
        continue
      if i < 2 :
        format_line.append(line)
        continue
      lines.append(line)

  test = copy.deepcopy(lines)
  test.sort()

  if test == lines :
    continue

  else:
    with open(path,"w") as f:
      f.write("".join(format_line))
      f.write("\n".join(test))
    print("ARRANGED "+path)
  print("_"*100)
