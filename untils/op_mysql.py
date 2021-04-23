'''场景：用例执行之前，连接数据库，查前置数据'''
import pymysql
from untils.readYaml import baseConfig
from untils import tool
api_database=baseConfig.apidatabase
web_database=baseConfig.webdatabase
class Exe_SQL():
    def __init__(self,username,password,dbname,serve):
        self.username=username
        self.password = password
        self.dbname = dbname
        self.serve = serve


    def exce_sql_api(self,sql):
        db_connect=pymysql.connect(host=self.serve,
                                   port=3306,
                                   user=self.username,
                                   passwd=str(self.password),
                                   charset='utf8',
                                   database=self.dbname,
                                   autocommit=True)
        cursor=db_connect.cursor()
        result=''
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
        except Exception as e:
            print(e)
        db_connect.close()
        return result

    def exce_sql_web(self,sql):
        db_connect=pymysql.connect(host=self.serve,
                                   port=3306,
                                   user=self.username,
                                   passwd=str(self.password),#密码都是数字，要转成字符串
                                   charset='utf8',
                                   database=self.dbname,
                                   autocommit=True)
        cursor=db_connect.cursor()
        result=''
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
        except Exception as e:
            print(e)
        db_connect.close()
        return result

def execute_api(sql):
    connet=Exe_SQL(username=api_database['username'],
                   password=api_database['password'],
                   dbname=api_database['dbname'],
                   serve=api_database['serve'])
    res=connet.exce_sql_api(sql)
    return res

def execute_web(sql):
    connet=Exe_SQL(username=web_database['username'],
                   password=web_database['password'],
                   dbname=web_database['dbname'],
                   serve=web_database['serve'])
    res=connet.exce_sql_web(sql)
    return res

if __name__ == '__main__':
    # res=execute_api('select * from user limit 5')
    # res = execute_web("select * from sp_cms_article WHERE article_cat in (SELECT cat_id FROM sp_cms_article_category WHERE cat_id = 10 or cat_pid = 10) AND article_title like '%测试空管资讯标题%' AND add_time BETWEEN '"+tool.get_date_time()+" 00:00:00' AND '"+tool.get_date_time()+" 23:59:59' ORDER BY istop desc,article_order desc,add_time desc limit 0,10")
    # res = execute_web ('select * from sp_cms_article limit 5')
    res= execute_api("SELECT * FROM tb_training_tag where tag_name like '%理论%' and pid='62543b49e3804dba92c88b28c15193d0'")
    print(len(res),res)