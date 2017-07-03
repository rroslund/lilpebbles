# -*- coding: utf-8 -*-
import os
import sys
from sanic import Sanic
from sanic import response
import glob
from sanic.response import json
import boto3
from sanic.response import stream, text

bucket='lilpebbles'


app = Sanic()

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

@app.route("/test")
async def test(request):
    return json("hello world!")

@app.route("/luna")
async def luna(request):
    return await response.file('./src/views/luna.html')

@app.route("/")
async def index(request):
    return await response.file('./src/views/index.html')

def uploadImage(file):
    print(file.name)
    s3 = boto3.resource('s3')
    s3.Bucket(bucket).put_object(Key=file.name, Body=file.body)



@app.route("/image", methods=['POST'])
async def img(request):
    uploadImage(request.files.get('img'))
    return json({"files":len(request.files)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=4)
