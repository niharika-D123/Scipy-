import os
import re
dir = os.getcwd()
k=0
for path, subdirs, files in os.walk(dir):
    for filename in files:

        counter=0
        x = re.search(".*test.*", filename)
        if(x):
            k += 1
            if (filename.endswith(".py")):
                path_of_file = path + "\\" + filename
                file1 = open(path_of_file, 'r+',encoding='UTF8')
                read_line = file1.readlines()
                #print(read_line)
                for line in read_line:
                   if (re.search(".*assert.*", line)):
                        counter+=1
                print(filename,",",counter)
print("The total number of test files:",k)
