from flask import Blueprint, request, jsonify
import gym_producer.app.service.member_service as member_service
import gym_producer.app.service.trainer_service as trainer_service


gym_blueprint = Blueprint('menu', __name__)


@gym_blueprint.route('/new_member/', methods=['POST'])
def new_member():
    member = request.json
    member_service.produce_member(member)
    return jsonify("info for new member recived"), 200


@gym_blueprint.route('/new_trainer/', methods=['POST'])
def new_trainer():
    trainer = request.json
    trainer_service.produce_trainer(trainer)
    return jsonify("info for new trainer recived"), 200