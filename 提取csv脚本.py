import pandas as pd
import csv
import codecs
def readcsv(files):
    data=pd.read_csv(files,delimiter="\t")
    #print(data)
    i=0
    for line in data.values:
        # print(line)
        a=line.tolist()
       
        b=','.join(a)
        #print(type(b))  |(b[1]==' RcmScanInfo'
        b=b.split(",")
        if(b[1]=='提取列关键字'):
        #print(b)    
             writeToCSV(b)   
#def writeToCSV(filter):
   # with open(r'C:\Users\Administrator\Desktop\新建文件夹\zhang.csv', "w",newline='') as csv_file:
    #    writer = csv.writer(csv_file)
     #   for line in filter:
      #      if line!='':  # 去除空行
       #         writer.writerow([line])
def writeToCSV(line): 
    out = open('转存路径','a',newline='')
    csv_write=csv.writer(out,dialect='excel')
    #csv_write.writerow(data)
    csv_write.writerow(line)

if __name__=='__main__':
    readcsv(r"读取路径.csv")