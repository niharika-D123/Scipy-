import os
import re
dir = os.getcwd()

for path, subdirs, files in os.walk(dir):
    for filename in files:
        #k+=1
        counter=0
        count_assert=0
        #print(filename)
        x = re.search(".*test.*",filename)
        if(not x):
            if (filename.endswith(".py")):
                # print(filename)
                path_of_file = path + "\\" + filename
                file1 = open(path_of_file, 'r+',encoding='UTF8')
                read_line = file1.readlines()
                #print(read_line)
                for line in read_line:
                   if (re.search(".*debug.*", line)):
                        counter+=1
                print(path_of_file,",",filename,",",counter)

