from flask import Flask, request, jsonify, abort
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root123@localhost/notesdb'

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)
    parent_id = db.Column(db.Integer)

    def __init__(self, title, body, parent_id=-1):
        self.title = title
        self.body = body
        self.parent_id = parent_id


@app.route('/notes/api/v1/notes')
def notes():
    results = Note.query.filter_by(parent_id=-1).all()
        
    json_results = []
    for result in results:
        d = {'id': result.id,
             'title': result.title,
             'body': result.body,
             'parent_id': result.parent_id}
        json_results.append(d)
    return jsonify(items=json_results)


@app.route('/notes/api/v1/note/<int:note_id>', methods=['GET','POST'])
def note(note_id):
    if request.method == 'GET':
        results = Note.query.filter_by(id=note_id).all()
        
        if len(results) == 0:
            return jsonify({ "success": False,
                          "reason": "No notes with that id"}),400 
        
        json_results = []
        for result in results:
            d = {'title': result.title,
                 'body': result.body,
                 'parent_id': result.parent_id}
            json_results.append(d)
        return jsonify(items=json_results)

@app.route('/notes/api/v1/add', methods=['POST'])
def add():
    if not request.json or not 'title' in request.json:
        abort(400)
    note = Note(request.json['title'], request.json['body'])
    json_results = {
        'title': request.json['title'],
        'body': request.json['body'],
        'parent_id': -1
    }
    db.session.add(note)
    db.session.commit()
    return jsonify(items=json_results), 201

@app.route('/notes/api/v1/branch/<int:parent_id>', methods=['POST'])
def branch(parent_id):
    if not request.json:
        abort(400)
    note = Note(request.json['title'], request.json['body'], parent_id)
    
    parent = Note.query.filter_by(id=parent_id).all()
    if len(parent) == 0:
        return jsonify({ "success": False,
                          "reason": "No notes with that id"}),400 
    json_results = {
        'title': request.json['title'],
        'body': request.json['body'],
        'parent_id': parent_id
    }
    db.session.add(note)
    db.session.commit()
    return jsonify(items=json_results), 201

@app.route('/notes/api/v1/delete/<int:note_id>')
def delete(note_id):
    result = Note.query.filter_by(id=note_id).first()
    
    if result == None:
        return jsonify({ "success": False,
                          "reason": "No note with that id"})

    db.session.delete(result)
    db.session.commit()
    return jsonify({ "success": True }), 200

@app.route('/notes/api/v1/branches/<int:note_id>')
def branches(note_id):
    results = Note.query.filter_by(parent_id=note_id).all()

    if len(results) == 0:
        return jsonify({ "success": False,
                          "reason": "No parent notes with that id"})

    json_results = []
    for result in results:
        d = {'id': result.id,
             'title': result.title,
             'body': result.body,
             'parent_id': result.parent_id}
        json_results.append(d)
    return jsonify(items=json_results)


if __name__ == '__main__':
    app.run(debug=True)
