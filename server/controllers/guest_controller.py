from flask import Blueprint, request, jsonify
from server.models import Guest, db

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@guest_bp.route('/guests', methods=['POST'])
def create_guest():
    data = request.get_json()
    new_guest = Guest(name=data['name'])
    db.session.add(new_guest)
    db.session.commit()
    return jsonify(new_guest.to_dict()), 201
