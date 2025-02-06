from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="API_KEY")


@app.route("/")
def ana_sayfa():
    return render_template("index.html")

@app.route("/cevap", methods=["POST"])
def cevap_al():
    data = request.get_json()
    messages = data["messages"]
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    cevap = completion.choices[0].message['content']
    return jsonify({"cevap": cevap})

if __name__ == "__main__":
    app.run(debug=True)
