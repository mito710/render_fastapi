from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/index")
def index():
    html_content = """
    <!DOCTYPE html>
<html lang="ja">

<head>
	<meta charset="UTF-8">
	<title>HOME</title>
	<link rel="stylesheet" href="css/indexstyle.css">
</head>

<body>
	<h1>~ 図書館を紹介 ~</h1>
	<nav>
		<ul>
			<li><a href="index.html">HOME</a></li>
			<li><a href="goodpoint.html">Good Point </a></li>
			<li><a href="howto.html">How to</a></li>
		</ul>
	</nav>
	<h4>24FI075のページへようこそ！</h4>
	<div class="intro">
		<h3>このサイトでは,<a class="intr" href="goodpoint.html">図書館のいいところ</a>や<a class="intr"
				href="howto.html">おすすめな図書館の使い方</a>を紹介します
			<br>
			また、このサイトはスマホなどから見れないこともないです
		</h3>
	</div>
	<div class="libe">
		<img class="homeimg" src="images/lib1.jpg" alt="図書館内の画像">
		<p class="imagetext">図書館のせかいへ</p>
	</div>
	<h6>画像：pngtree.com</h6>
</body>

</html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]