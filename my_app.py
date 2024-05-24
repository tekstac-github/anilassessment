from flask import Flask, jsonify
app = Flask(_name_)
@app.route("/sample", methods=["GET"])
def say_hello():
	return jsonify({"msg": "Welcome to BIRO Application"})
if _name_ == "_main_":
	# Please do not set debug=True in production
	app.run(host="0.0.0.0", port=5000, debug=True)
	
