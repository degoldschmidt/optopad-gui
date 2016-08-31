#import clr

#def getOutputType():
  #return clr.GetClrType(list)

def process():
  with open(r'config/experiment.dat') as f:
    f=[x.strip() for x in f if x.strip()]
    data=[x.split() for x in f]
    length = len(data)
    for row in data:
        row[0:6] = map(int,row[0:6])
        row[6:8] = map(float,row[6:8])
        row[8:] = map(int,row[8:])
    print(data)
  return data
  
thisdata = process()
#print(thisdata[0][0])