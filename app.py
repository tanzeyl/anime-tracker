import http.client
import json
from flask import Flask, render_template, request, flash

conn = http.client.HTTPSConnection("anime-db.p.rapidapi.com")
headers = { 'X-RapidAPI-Key': "afb343f435msh201413b2885819ep1b98fdjsn17ca616f6885", 'X-RapidAPI-Host': "anime-db.p.rapidapi.com" }

app = Flask(__name__)
app.secret_key = "abc"

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('signup.html')

@app.route("/signup", methods=["GET", "POST"])
def getInfo():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        rePass = request.form.get("rePass")
        if password != rePass:
            flash("Passwords do not match!")
            return render_template("signup.html")
        return "Info Sent Succesfully!"

@app.route("/search", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        query = str(request.form.get("query"))
        print(f"Raw: {query}")
        q = query
        s = query.split()
        query = ""
        for word in s:
            query += word + "%20"
        query = "/anime?page=1&size=10&search=" + query[:-3] + "&sortBy=ranking&sortOrder=desc"
        print(f"Query: {query}")
        conn.request("GET", query, headers=headers)
        res = conn.getresponse()
        data = res.read()
        res = json.loads(data.decode("utf-8"))
        allInfo = []
        for i in range(len(res["data"])):
            current = {}
            current["name"] = res["data"][i]["title"]
            current["genres"] = res["data"][i]["genres"]
            current["image"] = res["data"][i]["image"]
            current["type"] = res["data"][i]["type"]
            allInfo.append(current)
        return render_template("search.html", animes=allInfo, query=q.capitalize(), len=len(allInfo))


if __name__ == "__main__":
    app.run(debug = True)
