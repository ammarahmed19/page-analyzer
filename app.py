from flask import Flask, render_template, request
from urllib.request import urlopen
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    words = list(map(lambda x : x.strip() ,list(map(lambda x: x.lower(), request.form.get("Phrases/Words").split(',')))))
    pglink = request.form.get("Page Link")
    found = []
    message = "Here are the highlited words/phrases: "
    try:
        pghandle = urlopen(str(pglink).strip())
    except:
        return "Link is invalid"
    pgtext = pghandle.read()
    for word in words:
        pattern = r"\W?{}\W?".format(word)
        if re.search(pattern, str(pgtext).lower().strip()):
            found.append(word)
    
    for word in found:
        message += "<br>g" + word 

    if found:
        return message
    else:
        return "No words/phrases were found matching your criteria"
    #return "Words: " + str(words) + '\n' + "Page Link:" + str(pglink)

if __name__ == "__main__":
    app.run(debug=True)