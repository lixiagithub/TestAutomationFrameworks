from untils.op_excel import Excel_rw
import requests
from requests.auth import HTTPBasicAuth
from untils.readYaml import baseConfig
from untils.op_mysql import execute_api
from log.log import logger
import json
from untils.tool import *
tiqu_path=baseConfig.TIQU_PATH
class  HttpClientRequest():
    def __init__(self,urlPre=None):
        self.session=requests.session()     #创建session,跨接口请求，统一会话管理
        self.urlPre=urlPre
        self.headers={
            "Content-Type": "application/json",
            "Cookie": "JSESSIONID=14827C4737598D566BF1186706A2D5A1"
        }#默认的headers,根据项目不同，内容不同，有的项目不需要cookie
        self.init_headers()
        self.ex = Excel_rw(filename=tiqu_path)

    def init_headers(self,headers=None):
        '''初始化headers，设置headers为 "application/json",一般都是json格式'''
        self.session.headers.update(self.headers)
        #设置auth，项目不需要auth的这里可以注释掉
        #self.session.auth = HTTPBasicAuth("atnc", 'atnc3745')
        if headers:
            #self.session.auth=None#删除headers中的Authorization：Basic标头，项目不需要auth的这里可以注释掉
            self.session.headers.update(headers) #headers添加 token或者修改Content-Type等headers信息

    def zhuanhua(self,data):
        '''
        替换入参中包含了变量的参数
        如果变量以美元符号开头，去调用tool文件里面的封装的方法
        :return:
        '''
        for key,value in data.items():
            if isinstance(value,str) and value.startswith("{{") and value.endswith("}}"):
                name=value.split("{{")[1].split("}}")[0]
                tiqu_value=self.ex.read_tiqu(name)
                data[key]=tiqu_value #替换参数中带有{{的值，data['topic_id']='5f78728bc3ba1963d844b6e0'
                # select username from user limit 1
            if isinstance(value,str) and value.startswith("select") and 'from' in value:
                self.res = execute_api(value)[0][0]
                data[key] = self.res
            if isinstance(value,str) and value.startswith('$'):
                v = value.split("$")[1]
                if v == 'generate_phone':
                    res = generate_phone()  # 随机手机号码方法
                    data[key] = res
                if 'random_GBK2312'in v:
                    v1=v.split("(")[1].split(")")[0]
                    res = random_GBK2312(int(v1))  # 指定长度的随机汉字
                    data[key] = res
                    logger.info("随机生成长度为{0}的汉字：{1}".format(v1,res))
                    self.ex.write_tiqu(key, res)#根据项目，key不同，excel提取时候的{{key}}就不同
        return data


    def validate(self,yuqi,shiji,msg='验证结果'):
        '''
        断言  ：支持多个值的断言，支持校验值是字典，
        待开发，整个返回值可能是list，值是list
        参数1：预期{"token":"huacetest","msg":"success"，'info': {'name': 'admin'},}
         参数2 实际结果

          {'adress': {'city': 'changsha'},
          'httpstatus': 200,
          'info': {'age': 18, 'name': 'admin'},
           'msg': 'success',
           'token': 'huacetest'}
        :return: 布尔值
        '''
        for key,value in yuqi.items():
            #直到预期结果不等于实际结果，才返回False
            if key=="list":
                if isinstance(value, list) and isinstance(shiji, list):
                   for x in value:
                       for y in shiji:
                            res = self.validate(self.zhuanhua(x), y)
                            if res[0] is False:
                                return res
            else:
                if key not in shiji:
                    msg+='{}根本不在实际结果里面'.format(key)
                    return False,msg
                else:
                    if isinstance(value,dict) and isinstance(shiji[key],dict):
                            #{'name': 'admin'}预期
                            #{'age': 18, 'name': 'admin'}#实际
                            #递归
                            res=self.validate(self.zhuanhua(value),shiji[key])#预期value值，转换select，$,{{}}
                            if res[0] is False:
                                return res
                    elif isinstance(value, list) and isinstance(shiji[key], list):
                       for x in value:
                           for y in shiji[key]:
                                res = self.validate(self.zhuanhua(x), y)
                                if res[0] is False:
                                    return res
                    elif  value != shiji[key]:
                        msg+='这个{}的值预期是:{},而实际返回的是:{}'.format(key,value,shiji[key])
                        print(msg)
                        return False,msg
        return True,msg

    def sendRequest(self,method,url,index,**kwargs):
        #print(kwargs)
        '''请求之前的判断：1.是否传了参数'''
        data=None
        if "data" in kwargs and kwargs['data'] is not None:
            data=kwargs["data"] #定义了一个变量，入参
            '''请求之前：含有变量的参数的转化'''
            data=self.zhuanhua(data)
        #url=self.urlPre+name
        logger.info("开始请求第{2}个接口,url:{0},入参:{1}".format(url,data,index))

        if "headers" in kwargs and kwargs['headers'] is not None:
            '''表示请求的该接口非json类型,比如是表单类型'''
            h=kwargs["headers"]
            self.init_headers(headers=h)
        else:#这个项目post，但是参数通过param传参
            if not method=='get':#如果方法为get，参数默认为字典
                data=json.dumps(data)#将字典类型的参数转化为json字符串

        if isinstance(url, str) and "{{" in url:
            url1 = url.split("{{")[0]
            value = url.split("{{")[1].split("}}")[0]
            tiqu_value = self.ex.read_tiqu(value)
            url = url1 + tiqu_value  # 替换参数中带有{{的值

        if method == 'get' or method == 'delete':
            res=self.session.request(method=method,
                                     url=url,
                                     params=data)  #真正所有get接口发送请求的入口
        else:
            res = self.session.request(method=method,
                                       url=url,
                                       data=data)  # 真正所有post接口发送请求的入口
            # if data is None:
            #     res = self.session.request(method=method,
            #                                url=url,
            #                                data=data)  # 真正所有post接口发送请求的入口
            # else:
            #     res = self.session.request(method=method,
            #                                url=url,
            #                                params=data)  # 真正所有post接口发送请求的入口

        res.encoding = 'utf-8'
        logger.info("接口响应值{}".format(res))
        #logger.info(res.text)
        respone=res.json() #转化成字典之后，响应值
        '''2.请求之后 a:提取变量 b.断言 c.连接数据库
        extract={"exToken":"token","zhuangtaima":"httpstatus"}
                {"authorId":{"data":"author_id"}}
                {"Authentication":{"data":"token"}}
        '''
        if 'tiqu' in kwargs and  kwargs['tiqu'] is not None : # 你想要提取变量，每个项目要修改
            extract=kwargs['tiqu']#{"topicID":"topic_id"}
            for key,value in extract.items(): #循环需要提取的值，以及命名,key是实际接口中参数名，excel文档
                if isinstance(value,str):
                    if value=='token':  #提取变量中，token单独处理，根据项目不同，vlaue不同，要修改，比如有的响应返回token="ABC"或者access_token="ABC"
                        headers_token={key:respone[value]}#key值，根据项目不同，在excel里面要修改,比如不同项目header里面Authorization="ABC"，或者t="ABC"
                        # headers_token = {"Authorization"    : "Bearer {0}".format(respone[value])}#根据不同项目，修改headers_token
                        #self.init_headers(headers=di)
                        self.session.headers.update(headers_token) #之前的session headers添加key
                    elif value=='Authorization':
                        headers_token = {"Authorization": res.headers[value]}
                        self.session.headers.update(headers_token)
                    else:  #提取的变量，存到一个文件，给下面的接口用
                        #调用一个封装好写入excel文件的方法
                        self.ex.write_tiqu(key,respone[value])
                elif isinstance(value,dict):
                    for _key,_value in value.items():
                        #print(respone[_key][_value])
                        if _value=='token':  #提取变量中，token单独处理
                            headers_token = {key: respone[_key][_value]}
                            # headers_token = {"Authorization": "Bearer {0}".format(respone[_key][_value])}
                            # self.init_headers(headers=di)
                            self.session.headers.update(headers_token)  # 之前的session headers添加key
                        elif _value == 'Authorization':
                            headers_token = {"Authorization": res.headers[value]}
                            self.session.headers.update(headers_token)
                        else:
                            if isinstance(_value,dict):  #三层
                                for _k,_v in _value.items():
                                    self.ex.write_tiqu(key,respone[_key][_k][0][_v])#根据项目不同可以修改
                            else:
                                self.ex.write_tiqu(key, respone[_key][_value])
                elif isinstance(value,list):#如果返回结果是list，提取Excel中tiqu的value是list，获取list中的第一个数据
                    for _value in value:
                        #print(respone[_key][_value])
                        if isinstance(_value,dict):
                            for _k, _v in _value.items():
                                self.ex.write_tiqu(key,respone[0][_v])

        logger.info("接口请求的头部信息{}".format(res.request.headers))
        logger.info("接口请求完成，响应值{}".format(respone))
        return respone

