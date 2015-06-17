from app import db


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    education = db.Column(db.String(300))
    expertise = db.Column(db.String(300))
    experience = db.Column(db.Integer)
    email = db.Column(db.String(100))
    description = db.Column(db.String(500))
    specialization = db.Column(db.String(50))
    area = db.Column(db.String(100), index=True)
    city = db.Column(db.String(100), index=True)
    country = db.Column(db.String(100), index=True)
    completeaddress = db.Column(db.String(300))
    fee = db.Column(db.Integer)
    timings = db.Column(db.String(300))
    phone_number = db.Column(db.String(10))
    dial_extension = db.Column(db.String(5))
    sponsored = db.Column(db.Boolean, default=False)
    recommended = db.Column(db.Integer)

    def __init__(self, name=None, education=None, expertise=None, experience=None, email=None, description=None, specialization=None, area=None, city=None, country=None, completeaddress=None, fee=None, phone_number=None, timings=None):
        self.name = name
        self.education = education
        self.expertise = expertise
        self.expertise = experience
        self.email = email
        self.description = description
        self.specialization = specialization
        self.area = area
        self.city = city
        self.country = country
        self.completeaddress = completeaddress
        self.fee = fee
        self.phone_number = phone_number
        self.timings = timings


class AreaMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(100))
    city = db.Column(db.String(100))

    def __init__(self, area=None, city=None):
        self.area = area
        self.city = city

# class Clinic(db.Model):
# 	id = db.Column(db.Integer,primary_key = True)
# 	name = db.Column(db.String(64),index=True)
# 	education = db.Column(db.String(300))
# 	expertise = db.Column(db.String(300))
# 	experience = db.Column(db.Integer)
# 	description = db.Column(db.String(500))
# 	area = db.Column(db.String(100),index=True)
# 	city = db.Column(db.String(100),index=True)
# 	country = db.Column(db.String(100),index=True)
# 	completeaddress = db.Column(db.String(300))
# 	fee = db.Column(db.Integer)
# 	expertise_field = db.Column(db.String(100))
# 	consult_start_day = db.Column(db.Integer)
# 	consult_end_day = db.Column(db.Integer)
# 	consult_start_time_hour = db.Column(db.Integer)
# 	consult_end_time_hour = db.Column(db.Integer)
# 	consult_start_time_minute = db.Column(db.Integer)
# 	consult_end_time_minute = db.Column(db.Integer)
# 	phone_number = db.Column(db.String(10))
# 	dial_extension = db.Column(db.String(5))
# 	specialization = db.Column(db.String(50))
# 	sponsored = db.Column(db.Boolean,default=True)
# 	recommended = db.Column(db.Integer)
