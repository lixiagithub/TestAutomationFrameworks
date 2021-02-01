'''场景：用例执行之前，连接数据库，查前置数据'''
import pymysql
from untils.readYaml import baseConfig
api_database=baseConfig.apidatabase
web_database=baseConfig.webdatabase
class Exe_SQL():
    def __init__(self,username,password,dbname,serve):
        self.username=username
        self.password = password
        self.dbname = dbname
        self.serve = serve


    def exce_sql(self,sql):
        db_connect=pymysql.connect(host=self.serve,
                                   port=3307,
                                   user=self.username,
                                   passwd=self.password,
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
    res=connet.exce_sql(sql)
    return res

def execute_web(sql):
    connet=Exe_SQL(username=web_database['username'],
                   password=web_database['password'],
                   dbname=web_database['dbname'],
                   serve=web_database['serve'])
    res=connet.exce_sql_web(sql)
    return res

if __name__ == '__main__':
    #res=execute_api('select * from user limit 5')
    res = execute_web("SELECT c.communist_name,r.role_name,u.* FROM sp_sys_user u LEFT JOIN sp_sys_role r ON r.role_id = u.user_role LEFT JOIN sp_hr_communist c ON c.communist_no = u.user_relation_no WHERE u.status = 1 AND r.role_name = '基层管理员' AND (c.communist_name LIKE '%王鹏%' OR c.communist_no LIKE '%王鹏%')")
    print(len(res),res)