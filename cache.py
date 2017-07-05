from sanic.response import json
from sanic import Blueprint
import redis

cachebp = Blueprint('cache')

redis_cache = redis.StrictRedis(host='redis', port=6379, db=0)

@cachebp.route('/cache', methods=['GET'])
async def cache_root(request):
    return json(redis_cache.hgetall('images'))

@cachebp.route('/cache/<key>/<value>', methods=['POST','PUT'])
async def cache_root(request,key,value):
    redis_cache.hset('images',key,value)
    return json(redis_cache.hget('images',key))