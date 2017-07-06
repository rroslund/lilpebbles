# -*- coding: utf-8 -*-
import os
import sys
import re
import json
from sanic import Sanic
from sanic import response
import glob
from sanic.response import json
import boto3
from sanic.response import stream, text
from cache import cachebp
from s3util import s3wrapper
from redisutil import rediswrapper



app = Sanic()
app.blueprint(cachebp)

bucket='lilpebbles'
s3 = s3wrapper(bucket,'images/')
redis = rediswrapper(hashname='images')

app.static('/or-does-she', './src/views/ordoesshe.html')
app.static('/', './')
def addfiles(directory,virtualdir,regex):
    files= glob.glob(os.path.dirname(os.path.abspath(__file__))+"/"+directory+regex)
    for fullfile in files:
        f = os.path.basename(fullfile)
        virpath='/'+virtualdir+f
        app.static(virpath,fullfile)


addfiles('src/css/','css/','*.css')
addfiles('src/js/','js/','*.js')
addfiles('src/dist/','js/','*.js')
addfiles('src/images/','images/','*.*')
addfiles('src/views/','','*.html')
addfiles('src/dist/','dist/','*.js')
app.static('sw.js','sw.js')

def buildCacheValue(file):
    return {
        "main":'https://s3.amazonaws.com/lilpebbles/images/'+file,
        "thumb":'https://s3.amazonaws.com/lilpebbles/images/thumb/'+file,
        "xsmall":'https://s3.amazonaws.com/lilpebbles/images/xsmall/'+file,
        "small":'https://s3.amazonaws.com/lilpebbles/images/small/'+file,
        "medium":'https://s3.amazonaws.com/lilpebbles/images/medium/'+file,
        }

@app.route("/test")
async def test(request):
    return json("hello world!")

@app.route("/luna")
async def luna(request):
    return await response.file('./src/views/luna.html')

@app.route("/")
async def index(request):
    return await response.file('./src/views/index.html')

@app.route("/images", methods=['GET'])
async def img_get(request):
    res = redis.all()
    return json(res)

@app.route("/images/<image>", methods=['DELETE'])
async def img_delete(request,image):
    print("deleting "+image)
    file = image
    s3.delete(image)
    redis.delete(file)
    return json(redis.count())

@app.route("/images", methods=['POST'])
async def img(request):
    f=request.files.get('img')
    file = f.name
    #uploadImage('images/',f)
    s3.upload(f.name,f.body)
    res = buildCacheValue(file)
    redis.set(file,res)
    return json(res)

@app.route("/refresh", methods=['GET'])
async def refresh(request):
    allimgs = s3.all(prefix="images/original/")
    for img in allimgs:
        file = os.path.basename(img)
        res = buildCacheValue(file)
        redis.set(file,res)
    return json(redis.all())

@app.route("/clear", methods=['GET'])
async def refresh(request):
    redis.deleteall();
    return json(redis.all())
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=4)
