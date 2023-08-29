from flask import Blueprint
from controller.taskController import taskController,store
task = Blueprint('task', __name__)
task.route('/', methods=['GET'])(taskController)
task.route('/create', methods=['POST'])(store)
# task.route('/<int:user_id>', methods=['GET'])(show)
# task.route('/<int:user_id>/edit', methods=['POST'])(update)
# task.route('/<int:user_id>', methods=['DELETE'])(destroy)