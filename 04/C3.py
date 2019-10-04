def getFileLines(fname):
      fhandle=open(fname)
      lines=[]
      for line in fhandle:
            line=line.rstrip()
            if line:
                  lines.append(line)
      return lines
      
filename='https://gist.githubusercontent.com/bazzilic/ebea5d4bcfd786530f43c255f2b1b14b/raw/ad0392386cf52a61932972e26e22d7a28f4091a6/MH8811-04-Data.csv'

getFileLines(filename)

from C2 import average,min,max,median,range

average(lines)
min(lines)
max(lines)
median(lines)
range(lines)
