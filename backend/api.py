from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/health', methods=['GET'])
def health():
    return 'API is up and running!', 200