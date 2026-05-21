from flask import blueprint , request ,jsonify
from detection.detector import detect_attack

routes = Blueprint("routes",_name_)

@routes.route("/")
def home():
return "sentinelshield running"

@routes.route("/analyze", methods=["post"])
def analyze():
data = request.get_json()

result = detect_attack(str(data))

return jsonify(result)