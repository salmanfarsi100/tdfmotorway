#from datetime import datetime

from tdfmotorway import db

class Camera(db.Model):	
	tracking_id = db.Column(db.String(10), unique=True, nullable=False, primary_key=True)
	frame_number = db.Column(db.String(10), nullable=False)
	lane = db.Column(db.String(10), nullable=False)
	datetime = db.Column(db.String(10), nullable=False)
	image_path = db.Column(db.String(10), nullable=False)

	def __repr__(self):
		return "<Tracking ID: {}>".format(self.tracking_id)
		return "<Frame Number: {}>".format(self.frame_number)
		return "<Lane: {}>".format(self.lane)
		return "<Datetime: {}>".format(self.datetime)
		return "<Image Path: {}>".format(self.image_path)

# Radar Data table model
class Radar(db.Model):
    entry_id = db.Column(db.String(10), unique=True, nullable=False, primary_key=True)
    speed = db.Column(db.String(10), nullable=False)
    vehiclerange = db.Column(db.String(10), nullable=False)
    date_time = db.Column(db.String(10), nullable=False)
    def __repr__(self):
        return "<speed: {}>".format(self.speed)
        return "<range: {}>".format(self.range)