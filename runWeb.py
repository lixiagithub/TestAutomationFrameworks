'''web端用例执行入口'''
import pytest
'''运行所有的web用例'''
pytest.main(['-rs','-vv','./WebTestcase/InformationManagement/testcase_pbdinfor.py','--alluredir','report/xml']) #-r跳过用例，-s显示print内容，--alluredir报告，./report/xml报告地址



'''运行某一个文件的用例'''


'''运行所有的app用例'''
#pytest.main(['-s','-vv','../TestAutomationFrameworks/AppTestCase','--alluredir','./report/xml'])



