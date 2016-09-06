#import clr

#def getOutputType():
  #return clr.GetClrType(list)

def process():
  with open(r'config/experiment.dat') as f:
    f=[x.strip() for x in f if x.strip()]
    data=[x.split() for x in f]
    length = len(data)
    for row in data:
        row[0:2] = map(int,row[0:2])
        row[2:8] = map(float,row[2:8])
        row[8:12] = map(int,row[8:12])
        row[12:] = map(float,row[12:])
    print(data)
  return np.asarray(data)
  
thisdata = process()
#print(thisdata[0][0])