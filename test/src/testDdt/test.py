'''
Created on 2017年4月22日

@author: test
'''
import excel
import readText as rt
import ddt 
import unittest

@ddt.ddt
class tests(unittest.TestCase):
    
    def setUp(self):
        print("Start!")
 
    def tearDown(self):
        print("end!")
#        excel.excel_get_valueFromTitle(list, "name", "黑铁之堡")
    
    @ddt.data(*excel.excel_table_byname("data/abc.xlsx", 0, "a"))
    def test_mian(self,data):
        print(data["name"],data["a"],data["b"],data["c"],data["d"])
        
        
    
if __name__ == "__main__":
    unittest.main()



        
       
        



