# -*- coding: utf-8 -*-
import os
import sys
from sanic import Sanic
from sanic import response
import glob
from sanic.response import json


app = Sanic()

app.static('/or-does-she', './src/views/ordoesshe.html')
app.static('/', './')
def addfiles(directory,virtualdir,regex):
    files= glob.glob(os.path.dirname(os.path.abspath(__file__))+"/src/"+directory+regex)
    for fullfile in files:
        f = os.path.basename(fullfile)
        virpath='/'+virtualdir+f
        app.static(virpath,fullfile)


addfiles('css/','css/','*.css')
addfiles('js/','js/','*.js')
addfiles('dist/','js/','*.js')
addfiles('images/','images/','*.*')
addfiles('views/','','*.html')

@app.route("/test")
async def test(request):
    return json("hello world")

@app.route("/")
async def index(request):
    return await response.file('./src/views/index.html')
    #return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=4)
