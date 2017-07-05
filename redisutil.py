import redis

class rediswrapper(object):
    def __init__(self, host='redis', port=6379,db=0,hashname="images"):
        self.client=redis.StrictRedis(host, port, db)
        self.hashname=hashname
    def get(self,hkey):
        return self.client.hget(self.hashname,hkey)
    def set(self,hkey,value):
        self.client.hset(self.hashname,hkey,value)
    def all(self):
        return self.client.hgetall(self.hashname)
    def delete(self,hkey):
        return self.client.hdel(self.hashname,hkey)
    def count(self):
        return self.client.hlen(self.hashname)