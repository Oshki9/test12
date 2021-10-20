import json

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    with open('entities.json', encoding='utf-8') as f:
        entities = json.load(f)
        return render_template("main-all-items.html", entities=entities)


@app.route('/paging/<int:paging>')
def paging(paging: int):
    entities = ""
    with open('entities.json', encoding='utf-8') as f:
        entities = json.load(f)
    return render_template("paging.html", entities=entities, page=paging)


@app.route('/search')
def search():
    model = request.args.get('model')
    with open('entities.json', encoding='utf-8') as f:
        entities = json.load(f)
        response = []
        if not model:
            response = entities
        else:
            for x in model.split(" "):
                for e in entities:
                    if x.lower() in e["model"]:
                        response.append(e)
        return render_template("search_ause.html", entities=response)


@app.route('/card/<int:eid>')
def card(eid: int):
    with open('entities.json') as f:
        entities = json.load(f)
        for ent in entities:
            if ent["id"] == eid:
                return render_template("card_full.html", entity=ent)


@app.route('/card_short/<int:eid>')
def card_short(eid: int):
    with open('entities.json') as f:
        entities = json.load(f)
        for ent in entities:
            if ent["id"] == eid:
                return render_template("card__short.html", entity=ent)


if __name__ == '__main__':
    app.run(debug=True)
