from flask import render_template, request, Blueprint, jsonify, redirect, url_for
from tdfmotorway import db
from tdfmotorway.models import Camera
import os

camerabp = Blueprint("camerabp", __name__, static_folder='static', template_folder='templates')

@camerabp.route("/", methods=['GET', 'POST'])
def get_frame():
	content = request.json
	tracking_id = content['tracking_id']
	frame_number = content['frame_number']
	lane = content['lane']
	datetime = content['datetime']
	image_path = content['image_path']
	print(content)
	
	optimal_frame = Camera(tracking_id = tracking_id)
	optimal_frame.frame_number = frame_number
	optimal_frame.lane = lane
	optimal_frame.datetime = datetime
	optimal_frame.image_path = image_path
	db.session.add(optimal_frame)
	db.session.commit()

	return jsonify(202)

@camerabp.route("/deepstream/", methods=["GET", "POST"])
def deepstream():
	if request.form:
		if request.form["submit_button"] == "Add Vehicle Record":
			optimal_frame = Camera(tracking_id=request.form.get("tracking_id"))
			optimal_frame.frame_number = request.form.get("frame_number")
			optimal_frame.lane = request.form.get("lane")
			optimal_frame.datetime = request.form.get("datetime")
			optimal_frame.image_path = request.form.get("image_path")
			print(optimal_frame)
			db.session.add(optimal_frame)
			db.session.commit()
		if request.form["submit_button"] == "Start Application":
			os.system("cd /opt/nvidia/deepstream/deepstream-5.0/sources/deepstream_python_apps/apps/tdfflask/tdfmotorway/prcosesses/ofe")
			os.system("python3 ofe_new.py rtsp://admin:abc12345@192.168.1.108 frames")
			#os.system("cd /opt/nvidia/deepstream/deepstream-5.0/sources/deepstream_python_apps/apps/ofe_datetime_db_test")
			#os.system("python3 ofe.py rtsp://admin:abc12345@192.168.1.108 frames")
			return redirect(url_for('ofe_views'))
		if request.form["submit_button"] == "Stop Application":
			os.system("exit()")
			return redirect(url_for('home'))
		if request.form["submit_button"] == "View OFE Records":
			return redirect(url_for('ofe_views'))
	return render_template("camera.html")

@camerabp.route("/ofe_views/", methods=["GET", "POST"])
def ofe_views():
	if request.form:
		if request.form["submit_button"] == "Home":
			return redirect(url_for('home'))
		if request.form["submit_button"] == "Delete Records":
			Camera.query.delete()
			db.session.commit()
			return redirect(url_for('ofe_views'))
	optimal_frames = Camera.query.all()
	return render_template("ofe_views.html", optimal_frames=optimal_frames)