#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from streamfighter import app, db, twitch


@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1.0/highlights/snip', methods=['POST'])
def snipHighlights():
    if not request.json or not 'twitch_url' in request.json:
        abort(400)

    snippet = twitch.TwitchSnippet(request.json['twitch_url'])
    highlight = {
        'twitch_url': snippet.getTwitchUrl(),
        'poster': snippet.getPoster(),
        'broadcaster_name': snippet.getBroadcasterName(),
        'embedUrl': snippet.getEmbed()
    }
    return jsonify({'highlight': highlight}), 201


# @app.route('/api/v1.0/highlights', methods=['GET'])
# def getHighlights():
#     query_db = Highlight.query.order_by(Highlight.highlight_id.desc()).limit(5)
#     for highlight in query_db:
#         print(highlight)
#     return jsonify({'highlights': highlights})

# @app.route('/api/v1.0/highlights/<int:highlight_id>', methods=['GET'])
# def getHighlight(highlight_id):
#     highlight = [highlight for highlight in highlights if highlight['highlight_id'] == highlight_id]
#     if len(highlight) == 0:
#         abort(404)
#     return jsonify({'highlight': highlight[0]})

# @app.route('/api/v1.0/highlights', methods=['POST'])
# def createHighlight():
#     if not request.json or not 'twitch_url' in request.json:
#         abort(400)

#     highlight = Highlight(twitch_url=request.json['twitch_url'])
#     try:
#         db.session.add(highlight)
#         db.session.commit()
#         db.session.close()
#     except:
#         db.session.rollback()

#     highlight_query = Highlight.query.limit(1)[0]
#     jsonified = {
#         'highlight_id': highlight_query.highlight_id,
#         'twitch_url': highlight_query.twitch_url
#     }
#     return jsonify({'highlight': jsonified}), 201

# @app.route('/api/v1.0/highlights/<int:highlight_id>', methods=['PUT'])
# def updateHighlight(highlight_id):
#     highlight = [highlight for highlight in highlights if highlight['highlight_id'] == highlight_id]
#     if len(highlight) == 0:
#         abort(404)
#     if not request.json:
#         abort(400)
#     if 'title' in request.json and type(request.json['title']) != unicode:
#         abort(400)
#     if 'event' in request.json and type(request.json['event']) is not unicode:
#         abort(400)
#     if 'premiere' in request.json and type(request.json['premiere']) is not bool:
#         abort(400)
#     highlight[0]['title'] = request.json.get('title', highlight[0]['title'])
#     highlight[0]['event'] = request.json.get('event', highlight[0]['event'])
#     highlight[0]['premiere'] = request.json.get('premiere', highlight[0]['premiere'])
#     return jsonify({'highlight': highlight[0]})

# @app.route('/api/v1.0/highlights/<int:highlight_id>', methods=['DELETE'])
# def deleteHighlight(highlight_id):
#     highlight = [highlight for highlight in highlights if highlight['highlight_id'] == highlight_id]
#     if len(highlight) == 0:
#         abort(404)
#     highlight.remove(highlight[0])
#     return jsonify({'result': True})


# if __name__ == '__main__':
#     app.run(debug=True)