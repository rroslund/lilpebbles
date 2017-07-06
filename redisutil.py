import redis
import json
import pickle

class rediswrapper(object):
    def __init__(self, host='redis', port=6379,db=0,hashname="images"):
        self.client=redis.StrictRedis(host, port, db)
        self.hashname=hashname
    def get(self,hkey):
        return pickle.loads(self.client.hget(self.hashname,hkey))
    def set(self,hkey,value):
        self.client.hset(self.hashname,hkey,pickle.dumps(value))
    def all(self):
        all = self.client.hgetall(self.hashname)
        return {k:pickle.loads(v) for k,v in all.items()}
    def delete(self,hkey):
        return self.client.hdel(self.hashname,hkey)
    def deleteall(self):
        return self.client.delete(self.hashname)
    def count(self):
        return self.client.hlen(self.hashname)