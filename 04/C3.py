def getFileLines(fname):
      fhandle=open(fname)
      lines=[]
      for line in fhandle:
            line=line.rstrip()
            if line:
                  lines.append(line)
      return lines
      
lines=getFileLines('MH8811-04-Data.csv')

from C2 import average,min_,max_,median,range_

average(lines)
min_(lines)
max_(lines)
median(lines)
range_(lines)
