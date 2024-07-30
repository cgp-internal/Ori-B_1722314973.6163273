from flask import Blueprint, request, jsonify
from services.note_service import get_all_notes, get_note, create_note, update_note, delete_note

notes_router = Blueprint('notes', __name__)

@notes_router.route('/notes', methods=['GET'])
def all_notes():
    return jsonify(get_all_notes())

@notes_router.route('/notes/<int:note_id>', methods=['GET'])
def get_single_note(note_id):
    note = get_note(note_id)
    if note:
        return jsonify(note)
    else:
        return jsonify({'error': 'Note not found'}), 404

@notes_router.route('/notes', methods=['POST'])
def create_new_note():
    data = request.json
    if 'title' in data and 'content' in data:
        new_note = create_note(data['title'], data['content'])
        return jsonify(new_note), 201
    else:
        return jsonify({'error': 'Bad request'}), 400

@notes_router.route('/notes/<int:note_id>', methods=['PUT'])
def update_note_route(note_id):
    data = request.json
    if 'title' in data and 'content' in data:
        updated_note = update_note(note_id, data['title'], data['content'])
        if updated_note:
            return jsonify(updated_note)
        else:
            return jsonify({'error': 'Note not found'}), 404
    else:
        return jsonify({'error': 'Bad request'}), 400

@notes_router.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note_route(note_id):
    if delete_note(note_id):
        return jsonify({'message': 'Note deleted successfully'}), 200
    else:
        return jsonify({'error': 'Note not found'}), 404