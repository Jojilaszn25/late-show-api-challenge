from flask import Blueprint, request, jsonify
from server.models import Appearance, db

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([a.to_dict() for a in appearances])

@appearance_bp.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    new_appearance = Appearance(
        guest_id=data['guest_id'],
        episode_id=data['episode_id'],
        rating=data['rating']
    )
    db.session.add(new_appearance)
    db.session.commit()
    return jsonify(new_appearance.to_dict()), 201
