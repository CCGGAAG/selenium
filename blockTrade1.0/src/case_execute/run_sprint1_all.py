import sys
sys.path.append("..")

test = TestRunner.TestRunner('../test_case/test_sprint1','测试demo','测试环境：Chrome')
test  =TestRunner.TestRunner()
test.run()

'''
说明：
'../test_case/baidu_case' ： 测试脚本目录。
'百度页面搜索测试报告' ： 测试项目标题。
'测试环境：Chrome' ： 测试环境描述。
'''
