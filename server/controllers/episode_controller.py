from flask import Blueprint, request, jsonify
from server.models import Episode, db

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes])

@episode_bp.route('/episodes', methods=['POST'])
def create_episode():
    data = request.get_json()
    new_episode = Episode(date=data['date'], number=data['number'])
    db.session.add(new_episode)
    db.session.commit()
    return jsonify(new_episode.to_dict()), 201
