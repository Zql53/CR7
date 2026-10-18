import redis
import pymysql


class MySQLService:

    def __init__(self,
                 host="192.168.88.100",
                 port=3306,
                 user="root",
                 pswd="123456",
                 db="my_db",
                 charset="utf8"):
        # 连接对象
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=pswd,
            db=db,
            charset=charset
        )
        # 创建游标对象，用于执行sql
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_user_info(self, username):
        sql = "SELECT * FROM userinfo WHERE name=%s"
        self.cursor.execute(sql, [username])

        # 获取结果
        return self.cursor.fetchall()


class RedisService:

    def __init__(self, ms: MySQLService, host="192.168.88.100", port=6379, pswd=None, db=0):
        self.redis_conn = redis.Redis(
            host=host,
            port=port,
            password=pswd,
            db=db,
            decode_responses=True,
        )

        self.ms: MySQLService = ms

    def __del__(self):
        self.redis_conn.close()

    def __ttl_reset(self, key, ttl_time=15):
        # 设置TTL
        self.redis_conn.expire(key, ttl_time)

    def __save_user_info(self, username, infos):
        # 周杰轮: -> ((), ())
        # redis: key:周杰轮， value：list[(id, name, age), (), ()]
        for info in infos:
            msg = ",".join([str(col) for col in info])
            self.redis_conn.rpush(username, msg)
        # 首次设置过期时间
        self.__ttl_reset(username)

    def get_user_info(self, username):
        # redis有没有？
        if self.redis_conn.exists(username):        # 1 True
            # 找到缓存
            print(f"查询{username}，缓存命中，重设TTL")
            # 重设TTL
            self.__ttl_reset(username)

            #
            return self.redis_conn.lrange(username, 0, -1)

        print(f"查询{username}，缓存未命中，跳转MySQL查询")

        infos = self.ms.get_user_info(username)     # ((), ())

        if infos:       # 空元组是False，非空是True
            print(f"查询{username}，缓存未命中，从MySQL中查询得到信息，同检索到{len(infos)}条信息")
            self.__save_user_info(username, infos)
        else:
            print(f"查询{username}，缓存未命中，MySQL也没查到，没有此用户")

        return infos


if __name__ == '__main__':
    ms = MySQLService()
    rs = RedisService(ms)

    while True:
        username = input("输入要查询的姓名，要退出输入exit")
        if username == "exit":
            break

        infos = rs.get_user_info(username)
        print(infos)


























