import pymysql

class DBHelper():

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'spider'
        self.passwd = 'password'
        self.db = 'spider'

    #连接mysql
    def connectMysql(self):
        conn=pymysql.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             charset='utf8')
        return conn

    #连接数据库
    def connectDatabase(self):
        conn=pymysql.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             db=self.db,
                             charset='utf8')
        return conn

    #创建数据表
    def createTable(self, sql):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()

    #插入数据
    def insert(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, *params)
        conn.commit()
        cur.close()
        conn.close()

    #更新数据
    def update(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, *params)
        conn.commit()
        cur.close()
        conn.close()

    #删除数据
    def delete(self, sql, *params):
        conn = self.connectDatabase()

        cur = conn.cursor()
        cur.execute(sql, *params)
        conn.commit()
        cur.close()
        conn.close()

    #查询数据
    def query(self, sql):
        conn = self.connectDatabase()

        cursor = conn.cursor()
        results = []
        try:
            # 执行SQL语句
            cursor.execute(sql)
            num = cursor.rowcount
            print('num %s' % num)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                print(row)
        except Exception as e:
            raise e
        conn.close()
        return num

