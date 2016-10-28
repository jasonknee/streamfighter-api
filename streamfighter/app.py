#!flask/bin/python
from streamfighter import app, db
from flask import Flask, jsonify, abort, make_response, request
from models import *

highlights = [
    {
        'highlight_id': 1,
        'title': u'KBrad loses his shit!',
        'event': u'Socal Regionals 2016', 
        'url': 'https://localhost:5000',
        'premiere': True
    },
    {
        'highlight_id': 2,
        'title': u'Kbrad is on some shit!',
        'event': u'Socal Regionals 2016', 
        'url': 'https://streamfighter.tv',
        'premiere': False
    }
]

@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1.0/highlights', methods=['GET'])
def getHighlights():
    return jsonify({'highlights': highlights})

@app.route('/api/v1.0/highlights/<int:highlight_id>', methods=['GET'])
def getHighlight(highlight_id):
    highlight = [highlight for highlight in highlights if highlight['highlight_id'] == highlight_id]
    if len(highlight) == 0:
        abort(404)
    return jsonify({'highlight': highlight[0]})

@app.route('/api/v1.0/highlights', methods=['POST'])
def createHighlight():
    if not request.json or not 'title' in request.json:
        abort(400)

    # highlight = Highlight(twitch_url=request.json['twitch_url'], poster=request.json['poster'])
    # try:
    #     db.session.add(highlight)
    #     db.session.commit()
    #     db.session.close()
    # except:
    #     db.session.rollback()
    # highlight = {
    #     'highlight_id': highlights[-1]['highlight_id'] + 1,
    #     'title': request.json['title'],
    #     'event': request.json.get('event', ""),
    #     'url': request.json.get('url', ""),
    #     'premiere': False
    # }
    # highlights.append(highlight)
    return jsonify({'highlight': highlight}), 201

@app.route('/api/v1.0/highlights/<int:highlight_id>', methods=['PUT'])
def updateHighlight(highlight_id):
    highlight = [highlight for highlight in highlights if highlight['highlight_id'] == highlight_id]
    if len(highlight) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'event' in request.json and type(request.json['event']) is not unicode:
        abort(400)
    if 'premiere' in request.json and type(request.json['premiere']) is not bool:
        abort(400)
    highlight[0]['title'] = request.json.get('title', highlight[0]['title'])
    highlight[0]['event'] = request.json.get('event', highlight[0]['event'])
    highlight[0]['premiere'] = request.json.get('premiere', highlight[0]['premiere'])
    return jsonify({'highlight': highlight[0]})

@app.route('/api/v1.0/highlights/<int:highlight_id>', methods=['DELETE'])
def deleteHighlight(highlight_id):
    highlight = [highlight for highlight in highlights if highlight['highlight_id'] == highlight_id]
    if len(highlight) == 0:
        abort(404)
    highlight.remove(highlight[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)