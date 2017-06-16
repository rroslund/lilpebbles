from sanic import Sanic
from sanic import response


app = Sanic()

app.static('/index.html', './src/index.html')
app.static('/sw.js', './sw.js')
app.static('/', './')
app.static('/js/app.js', './src/js/app.js')
app.static('/css/main.css', './src/css/main.css')
app.static('/css/pebbles.css', './src/css/pebbles.css')

@app.route("/")
async def test(request):
    return await response.file('./src/index.html')
    #return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=4)
