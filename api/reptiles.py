from flask import (Blueprint, request, jsonify)
from .import models

bp = Blueprint('reptiles', __name__, url_prefix='/reptiles')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        request_data = request.get_json()

        print(request_data)

        conservation_state = request_data['conservation_status']

        new_reptile = models.Reptile(
            common_name = request_data['common_name'],
            scientific_name = request_data['scientific_name'],
            native_habitat = request_data['native_habitat'],
            fun_fact = request_data['fun_fact'],
            conservation_status = models.ConservationStatus[conservation_state]
        )

        models.db.session.add(new_reptile)
        models.db.session.commit()
        
        return jsonify({ 'id' : new_reptile.id }), 200
    
    results = models.Reptile.query.all()

    reptiles_list = [
        {
            'common_name' : reptile.common_name,
            'scientific_name' : reptile.scientific_name,
            'native_habitat' : reptile.native_habitat,
            'fun_fact' : reptile.fun_fact,
            'conservation_status' : str(reptile.conservation_status)
        } for reptile in results
    ]

    return jsonify(reptiles_list), 200

@bp.route('/<reptile_id>')
def get_reptile(reptile_id):
    reptile = models.Reptile.query.filter_by(id=reptile_id).first()
    
    print(reptile)

    return jsonify({ 'reptile_id': reptile_id}), 200