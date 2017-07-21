'''
Created on 2017年4月22日

@author: test
'''
import excel
import readText as rt
import unittest
import ddt

@ddt.ddt
class tests(unittest.TestCase):
    
    def setUp(self):
        print("begin")
    def tearDown(self):
        print("end")
        
    @ddt.data(*excel.excel_table_byname("data/abc.xlsx", 0, "a"))
    def test_mian(self,data):
#        #通过excel获取数据
#        excelList =excel.excel_table_byname("data/abc.xlsx", 0, "a")
#        data =excel.excel_get_valueFromTitle(excelList, "name", "黑铁之堡")
        #将数据通过字典传入到数据字段
        log = rt.readTexts.logger(self,data["logname"])
        file = rt.readTexts.file(self,data["filename"])
        driver = rt.readTexts.driver(self)
        rt.readTexts.setA(self,data["a"])
        rt.readTexts.setB(self,data["b"])
        rt.readTexts.setC(self,data["c"])
        rt.readTexts.setD(self,data["d"])
        baseUrl = data["baseurl"]
        locatePath=data["locatepath"]
        titlePath=data["titlepath"]
        textPath=data["textpath"]
        #记录日志
        log.info("loading字典数据：")
        log.info(data)
        rt.readTexts.doText(self,log,file,driver,baseUrl,locatePath,titlePath,textPath)

if __name__ == "__main__":
    unittest.main()        
#tests =tests()
#tests.mian()



        
       
        



