# -*- coding: utf-8 -*-
from sanic import Sanic
from sanic import response


app = Sanic()

app.static('/index.html', './src/index.html')
app.static('/sw.js', './sw.js')
app.static('/', './')
app.static('/images/first.jpg', './src/images/first.jpg')
app.static('/images/second.jpg', './src/images/second.jpg')
app.static('/images/third.jpg', './src/images/third.jpg')
app.static('/images/fourth.jpg', './src/images/fourth.jpg')
app.static('/images/fifth.jpg', './src/images/fifth.jpg')
app.static('/images/first.small.jpg', './src/images/first.small.jpg')
app.static('/images/second.small.jpg', './src/images/second.small.jpg')
app.static('/images/third.small.jpg', './src/images/third.small.jpg')
app.static('/images/fourth.small.jpg', './src/images/fourth.small.jpg')
app.static('/images/fifth.small.jpg', './src/images/fifth.small.jpg')

app.static('/js/app.js', './src/js/app.js')
app.static('/css/main.css', './src/css/main.css')
app.static('/css/pebbles.css', './src/css/pebbles.css')

@app.route("/")
async def test(request):
    return await response.file('./src/index.html')
    #return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=4)
