# -*- coding: utf-8 -*-
import os
import sys
from sanic import Sanic
from sanic import response
from aoiklivereload import LiveReloader
import glob


app = Sanic()

app.static('/or-does-she', './src/views/ordoesshe.html')
app.static('/', './')
def addfiles(directory,virtualdir,regex):
    files= glob.glob(os.path.dirname(os.path.abspath(__file__))+"/src/"+directory+regex)
    for fullfile in files:
        f = os.path.basename(fullfile)
        virpath='/'+virtualdir+f
        app.static(virpath,fullfile)
        print('('+virpath+','+fullfile+')')


addfiles('css/','css/','*.css')
addfiles('js/','js/','*.js')
addfiles('images/','images/','*.*')
addfiles('views/','','*.html')


@app.route("/")
async def test(request):
    return await response.file('./src/views/index.html')
    #return json({"hello": "world"})


if __name__ == "__main__":
    src_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if src_path not in sys.path:
            sys.path.append(src_path)
    reloader = LiveReloader()
    reloader.start_watcher_thread()
    app.run(host="0.0.0.0", port=8000, workers=4)
