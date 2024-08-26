from quart import Quart

app = Quart(__name__)


@app.route('/')
async def hello_world():
    return "hello world"


if __name__ == '__main__':
    app.run()