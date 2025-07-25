from flask import Flask,render_template,request,redirect,url_for
from lru import LRUCache
import os

app = Flask(__name__)

# Set capacity here
cache = None

@app.route("/", methods=["GET"])
def home():
    if cache is None:
        return render_template("index.html", initialized=False)
    return render_template("index.html", initialized=True, capacity=cache.cap, cache=get_cache_contents(), result=None)

@app.route("/init", methods=["POST"])
def init():
    global cache
    capacity = int(request.form["capacity"])
    cache = LRUCache(capacity=capacity)
    return redirect(url_for("home"))

@app.route("/put", methods=["POST"])
def put():
    key = int(request.form["key"])
    value = int(request.form["value"])
    cache.put(key, value)
    return redirect(url_for("home"))

@app.route("/get", methods=["POST"])
def get():
    key = int(request.form["key"])
    value = cache.get(key)
    return render_template('index.html',initialized=True, capacity=cache.cap, cache=get_cache_contents(), result=f"Value = {value}")

def  get_cache_contents():
    node = cache.head.next
    contents=[]
    while node!=cache.tail:
        contents.append((node.key,node.value))
        node = node.next
    return contents

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port or default to 5000
    app.run(host="0.0.0.0", port=port)

    