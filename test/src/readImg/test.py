from urllib.request import urlretrieve

if __name__ == "__main__":
   data=[1,2,3,4,5,6,7]
   print("输出：%s%s%s%s%s%s%s"%data[0],%data[1],%data[2],%data[3],%data[4],%data[5],%data[6])
   # print("PPPPPP%s%s%s%s%s%s%s"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
   sqls = "insert into student(department,major,class,name,sex,phone,phoneType) values('%s','%s','%s','%s','%s','%s','%s',);"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6])