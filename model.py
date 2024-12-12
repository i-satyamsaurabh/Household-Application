from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class Professional(db.Model):
    __tablename__ = 'professional'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    service_type_id = db.Column(db.Integer, db.ForeignKey('service_type.id'), nullable=False)  # Fixed FK to 'service_type'
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    experience = db.Column(db.Integer)  # in years
    address = db.Column(db.String(150), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    is_approved = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text)

    user = db.relationship('User', back_populates='professional')
    service_type = db.relationship('Service_Type', back_populates='professionals')
    service_requests = db.relationship('ServiceRequest', back_populates='professional', foreign_keys='ServiceRequest.professional_id')


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    user = db.relationship('User', back_populates='customer')
    service_requests = db.relationship('ServiceRequest', back_populates='customer', foreign_keys='ServiceRequest.customer_id')
    reviews = db.relationship('Review', back_populates='customer', cascade='all, delete-orphan')


class Service_Type(db.Model):
    __tablename__ = 'service_type'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('service_category.id'), nullable=False)

    name = db.Column(db.String(100), nullable=False )
    price = db.Column(db.Float, nullable=False)
    time_required = db.Column(db.Integer)  # in minutes
    description = db.Column(db.Text)
    professional_id = db.Column(db.Integer, nullable=False) 

    professionals = db.relationship('Professional', back_populates='service_type') 
    service_category = db.relationship('Service_Category', back_populates='services')
    service_requests = db.relationship('ServiceRequest', back_populates='service')


class Service_Category(db.Model):
    __tablename__ = 'service_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    services = db.relationship('Service_Type', back_populates='service_category')

    def __repr__(self):
        return f'<Service Category: {self.name}>'


class ServiceRequest(db.Model):
    __tablename__ = 'service_request'
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service_type.id'), nullable=False)
    service_name= db.Column(db.String(100))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('professional.id'))
    date_of_request = db.Column(db.DateTime, default=datetime.utcnow)
    date_of_completion = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='requested')
    remarks = db.Column(db.Text)

    service = db.relationship('Service_Type', back_populates='service_requests')  # Fixed relationship
    customer = db.relationship('Customer', back_populates='service_requests')
    professional = db.relationship('Professional', back_populates='service_requests')
    review = db.relationship('Review', back_populates='service_request', uselist=False)


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    service_request_id = db.Column(db.Integer, db.ForeignKey('service_request.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    service_request = db.relationship('ServiceRequest', back_populates='review')
    customer = db.relationship('Customer', back_populates='reviews')