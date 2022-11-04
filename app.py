import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        form_prompt = request.form["image_prompt"]
        response = openai.Image.create(
            prompt=form_prompt,
            n=1,
            size="256x256",
        )
        return redirect(url_for("index", image_url = response['data'][0]['url']))

    image_url = request.args.get("image_url")
    return render_template("index.html", image_url=image_url)
