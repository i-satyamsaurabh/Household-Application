from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

from model import Service_Category, Service_Type, ServiceRequest, Review, Professional, Customer, db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    is_blocked = db.Column(db.Boolean, default=False)

    professional = db.relationship('Professional', back_populates='user', uselist=False, cascade='all, delete-orphan')
    customer = db.relationship('Customer', back_populates='user', uselist=False, cascade='all, delete-orphan')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///household_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'satyamsaurabh'

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
                login_user(user)
                # Redirect based on the user's role after login
                if user.role == 'Admin':
                    return redirect(url_for('admin_dashboard'))
                elif user.role == 'Professional':
                    return redirect(url_for('professional_dashboard'))
                elif user.role == 'Customer':
                    return redirect(url_for('customer_dashboard'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password']) 
        role = request.form['role']
        address = request.form['address']
        pincode = request.form['pincode']

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please use another email or log in.')
            return redirect(url_for('register'))

        # Create the common User entry
        new_user = User(name=name, email=email, password=password, role=role, address=address, pincode=pincode)
        db.session.add(new_user)
        db.session.flush()  # Get the new_user's ID before committing

        # Save the user in Customer or Professional table based on role
        if role == 'Customer':
            new_customer = Customer(user_id=new_user.id, email=email, name=name, address=address, pincode=pincode)
            db.session.add(new_customer)
        elif role == 'Professional':
            service_type_id = request.form['service_type_id']
            experience = request.form.get('experience', 0)
            description = request.form.get('description', '')
            new_professional = Professional(
                user_id=new_user.id, email=email, name=name, address=address, pincode=pincode,
                service_type_id=service_type_id, experience=experience, description=description
            )
            db.session.add(new_professional)

        # Commit the transaction to save data
        db.session.commit()
        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))

    return render_template('register.html')



@app.route('/admin_dashboard')
def admin_dashboard():
    if current_user.role != 'Admin':
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('unauthorized')) 

    services = Service_Type.query.all()
    professionals = Professional.query.all()
    customers = Customer.query.all()
    category=Service_Category.query.all()
    total_users = User.query.count()
    total_customers = Customer.query.count()
    total_professionals = Professional.query.count()

    # Assuming you have a model or a method to get service request details
    service_requests = ServiceRequest.query.all()
    completed_requests = sum(1 for r in service_requests if r.status == 'Accepted' or r.status == 'Completed')
    in_process_requests = sum(1 for r in service_requests if r.status == 'Pending')
    declined_requests = sum(1 for r in service_requests if r.status == 'Declined')

    return render_template('admin_dashboard.html', 
                           services=services, 
                           professionals=professionals, 
                           customers=customers,
                           category=category,
                           total_users=total_users, 
                           total_customers=total_customers, 
                           total_professionals=total_professionals,
                           service_requests=service_requests,
                           declined_requests=declined_requests,
                           completed_requests=completed_requests,
                           in_process_requests=in_process_requests)

@app.route('/professional_dashboard')
@login_required
def professional_dashboard():

    services = Service_Type.query.all()
    user = User.query.filter_by(id=current_user.id).first()
    category = Service_Category.query.all()
    professional = Professional.query.filter_by(user_id=current_user.id).first()
    service_requests = ServiceRequest.query.filter_by(professional_id=professional.id).all()

    # Service request summary data
    total_requests = len(service_requests)
    completed_requests = len([req for req in service_requests if req.status == 'Accepted' or req.status == 'Completed'])
    pending_requests = len([req for req in service_requests if req.status == 'Pending'])
    rejected_requests = len([req for req in service_requests if req.status == 'Declined'])


    available_requests = ServiceRequest.query.filter_by(status='Pending', professional_id=professional.id).all()
    my_services = ServiceRequest.query.filter_by(status='Accepted', professional_id=professional.id).all()
    declined_requests = ServiceRequest.query.filter_by(status='Declined', professional_id=professional.id).all()

    if current_user.role != 'Professional':
        flash('Unauthorized error!', 'error')
        return redirect(url_for('unauthorized'))
    return render_template('professional_dashboard.html', service_requests=service_requests, professional=professional, user=user, services=services, category=category, total_requests=total_requests, completed_requests=completed_requests, pending_requests=pending_requests, my_services=my_services, available_requests=available_requests, declined_requests=declined_requests, rejected_requests=rejected_requests)

@app.route('/customer_dashboard')
@login_required
def customer_dashboard():
    services = Service_Type.query.all()
    user = User.query.filter_by(id=current_user.id).first()
    category = Service_Category.query.all()
    customer = Customer.query.filter_by(user_id=current_user.id).first()
    service_requests = ServiceRequest.query.filter_by(customer_id=customer.id).all()
    reviews = Review.query.filter_by(customer_id=customer.id).all()

    # Service request summary data
    total_requests = len(service_requests)
    completed_requests = len([i for i in service_requests if i.status == 'Completed' or i.status == 'Accepted'])
    pending_requests = total_requests - completed_requests

    if current_user.role != 'Customer':
        flash('Unauthorized access.', 'error')
        return redirect(url_for('unauthorized'))
    
    return render_template('customer_dashboard.html', 
                           services=services, 
                           category=category, 
                           customer=customer, 
                           user=user, 
                           service_requests=service_requests, 
                           reviews=reviews,
                           total_requests=total_requests,
                           completed_requests=completed_requests,
                           pending_requests=pending_requests)


@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/services')
@login_required
def services():
    services = Service_Type.query.all()
    service_professionals = Professional.query.all()
    return render_template('services.html', services=services, service_professionals=service_professionals)

@app.route('/create_service', methods=['POST'])
def create_service():
    # Get form data
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    time_required = request.form.get('time_required')
    category_id = request.form.get('service_category')
    professional_id = request.form.get('professional_id')

    # Create a new service type instance
    new_service = Service_Type(
        name=name, 
        description=description, 
        price=price, 
        time_required=time_required,
        category_id=category_id,
        professional_id=professional_id
    )

    # Add the new service to the database
    db.session.add(new_service)
    db.session.commit()

    # Redirect to admin dashboard
    return redirect(url_for('admin_dashboard'))


@app.route('/create_service_category', methods=['POST'])
def create_service_category():
    name = request.form.get('name')
    description = request.form.get('description')
    
    # Create a new service instance
    new_service = Service_Category(name=name, description=description)

    # Add the new service to the session and commit
    db.session.add(new_service)
    db.session.commit()

    return redirect(url_for('admin_dashboard'))


@app.route('/delete_service/<int:id>')
@login_required
def delete_service(id):
    services=Service_Type.query.filter_by(id=id).first()
    if services:
        db.session.delete(services)
        db.session.commit()
    return redirect ('/admin_dashboard')

@app.route('/delete_customers/<int:id>')
@login_required
def delete_customers(id):
    customers=Customer.query.filter_by(id=id).first()
    if customers:
        db.session.delete(customers)
        db.session.commit()
    return redirect ('/admin_dashboard')

@app.route('/delete_professional/<int:id>')
@login_required
def delete_professional(id):
    professionals=Professional.query.filter_by(id=id).first()
    if professionals:
        db.session.delete(professionals)
        db.session.commit()
    return redirect ('/admin_dashboard')

@app.route('/delete_service_request/<int:request_id>')
def delete_service_request(request_id):
    # Find the service request
    service_request = ServiceRequest.query.get_or_404(request_id)
    
    # Find and delete all reviews related to this service request
    reviews = Review.query.filter_by(service_request_id=service_request.id).all()
    
    for review in reviews:
        db.session.delete(review)
    
    # Delete the service request itself
    db.session.delete(service_request)
    
    # Commit changes to the database
    db.session.commit()
    return redirect(url_for('customer_dashboard'))


@app.route('/delete_service_request_professional/<int:request_id>')
def delete_service_request_professional(request_id):
    # Find the service request
    service_request = ServiceRequest.query.get_or_404(request_id)
    
    # Find and delete all reviews related to this service request
    reviews = Review.query.filter_by(service_request_id=service_request.id).all()
    
    for review in reviews:
        db.session.delete(review)
    
    # Delete the service request itself
    db.session.delete(service_request)
    
    # Commit changes to the database
    db.session.commit()
    return redirect(url_for('professional_dashboard'))

@app.route('/accept_service_request/<int:request_id>', methods=['GET', 'POST'])
def accept_service_request(request_id):
    # Query the service request from the database
    service_request = ServiceRequest.query.get_or_404(request_id)
    
    # Update the status to "Accepted"
    service_request.status = 'Accepted'
    
    # Commit the changes to the database
    db.session.commit()

    
    # Redirect back to the dashboard
    return redirect(url_for('professional_dashboard'))

@app.route('/decline_service_request/<int:request_id>', methods=['GET', 'POST'])
@login_required
def decline_service_request(request_id):
    # Query the service request from the database
    service_request = ServiceRequest.query.get_or_404(request_id)
    
    # Update the status to "Declined"
    service_request.status = 'Declined'
    
    # Commit the changes to the database
    db.session.commit()

    
    # Redirect back to the dashboard
    return redirect(url_for('professional_dashboard'))




@app.route('/edit_service/<int:id>', methods=['POST','GET'])
@login_required
def edit_service(id):
    if current_user.role != 'Admin':
        flash('You do not have permission to access this page.')
        return redirect(url_for('admin_dashboard'))
    if request.method == 'POST' and current_user.role=='Admin':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        time_required = request.form.get('time_required')
        services=Service_Type.query.filter_by(id=id).first()
        services.name=name
        services.description=description
        services.price=price
        services.time_required=time_required
        db.session.add(services)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))
    services=Service_Type.query.filter_by(id=id).first()
    return render_template ("edit_service.html", services=services)

@app.route('/edit_profile/<int:id>', methods=['POST','GET'])
def edit_profile(id):
    user=User.query.filter_by(id=id).first()
    if request.method == 'POST':
        user.name = request.form.get('name')
        user.email = request.form.get('email')
        user.address = request.form.get('address')
        user.pincode = request.form.get('pincode')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))
    return render_template ("edit_profile.html", user=user)

@app.route('/edit_service_request/<int:id>', methods=['GET', 'POST'])
def edit_service_request(id):
    # Fetch the specific service request based on the provided id
    service_request = ServiceRequest.query.filter_by(id=id).first()

    # Logic to handle form submission and update the service request
    if request.method == 'POST':
        # Update the service request with form data
        service_request.remarks = request.form['remarks']
        service_request.status = request.form['status']
        
        # Commit the changes to the database
        db.session.commit()
        return redirect(url_for('customer_dashboard'))

    # Render the template and pass the service request object
    return render_template('edit_service_request.html', service_request=service_request)

@app.route('/edit_service_request_professional/<int:id>', methods=['GET', 'POST'])
def edit_service_request_professional(id):
    # Fetch the specific service request based on the provided id
    service_request = ServiceRequest.query.filter_by(id=id).first()

    # Logic to handle form submission and update the service request
    if request.method == 'POST':
        # Update the service request with form data
        service_request.remarks = request.form['remarks']
        service_request.status = request.form['status']
        
        # Commit the changes to the database
        db.session.commit()
        return redirect(url_for('professional_dashboard'))

    # Render the template and pass the service request object
    return render_template('edit_service_request_professional.html', service_request=service_request)



@app.route('/service_requests', methods=['POST'])
def service_requests():
    # Extract form data
    customer = Customer.query.filter_by(user_id=current_user.id).first()
    service_id = request.form.get('service_id')
    professional_id = request.form.get('professional_id')
    service_name = request.form.get('service_name')
    
    # Create a new ServiceRequest
    new_request = ServiceRequest(
        service_id=service_id,
        customer_id=customer.id,
        professional_id=professional_id,
        service_name=service_name,
        date_of_request=datetime.utcnow(),
        status='Pending',  
        remarks=''
    )
    
    # Add the new request to the database
    db.session.add(new_request)
    db.session.commit()
    return redirect(url_for('customer_dashboard'))

@app.route('/rate_service/<int:id>', methods=['GET', 'POST'])
def rate_service(id):
    # Fetch the specific service request based on the provided id
    service_request = ServiceRequest.query.filter_by(id=id).first()

    if request.method == 'POST':
        rating = request.form['rating']
        comment = request.form['comment']
        date_of_review = datetime.utcnow()

        # Create a new Review instance
        review = Review(
            service_request_id=service_request.id,
            customer_id=service_request.customer_id,
            rating=rating,
            comment=comment,
            date_created=date_of_review
        )
        # Commit the changes to the database
        db.session.add(review)
        db.session.commit()
        
        return redirect(url_for('customer_dashboard'))

    # Render the template (no need to pass `review` here)
    return render_template('rate_service.html', service_request=service_request)

@app.route('/search_services', methods=['GET'])
def search_services():
    query = request.args.get('query')
    customer=Customer.query.filter_by(user_id=current_user.id).first()
    user=User.query.filter_by(id=current_user.id).first()
    service_requests = ServiceRequest.query.filter_by(customer_id=customer.id).all()
    reviews=Review.query.filter_by(customer_id=customer.id).all()
    
    # Example search logic
    if query:
        services = Service_Type.query.filter(
            (Service_Type.name.ilike(f'%{query}%'))
        ).all()
    else:
        services = Service_Type.query.all()

    total_requests = len(service_requests)
    completed_requests = len([req for req in service_requests if req.status == 'Completed'])
    pending_requests = total_requests - completed_requests
    

    return render_template('customer_dashboard.html', services=services, customer=customer, user=user, service_requests=service_requests, reviews=reviews, total_requests=total_requests, completed_requests=completed_requests, pending_requests=pending_requests, query=query)


@app.route('/search_services_admin', methods=['GET'])
def search_services_admin():
    query = request.args.get('query')
    services = Service_Type.query.all()
    professionals = Professional.query.all()
    customers = Customer.query.all()
    category=Service_Category.query.all()
    total_users = User.query.count()
    total_customers = Customer.query.count()
    total_professionals = Professional.query.count()

    # Assuming you have a model or a method to get service request details
    service_requests = ServiceRequest.query.all()
    completed_requests = sum(1 for r in service_requests if r.status == 'Completed')
    in_process_requests = sum(1 for r in service_requests if r.status == 'Pending')
    
    # Example search logic
    if query:
        services = Service_Type.query.filter(
            (Service_Type.name.ilike(f'%{query}%'))
        ).all()
    else:
        services = Service_Type.query.all()
    

    return render_template('admin_dashboard.html',  services=services, 
                           professionals=professionals, 
                           customers=customers,
                           category=category,
                           total_users=total_users, 
                           total_customers=total_customers, 
                           total_professionals=total_professionals,
                           service_requests=service_requests,
                           completed_requests=completed_requests,
                           in_process_requests=in_process_requests, query=query)



@app.route('/view_service_request/<int:request_id>')
def view_service_request(request_id):
    # Query the service request and related customer details
    service_request = ServiceRequest.query.get_or_404(request_id)
    customer = Customer.query.filter_by(id=service_request.customer_id).first_or_404()

    # Render the template with service request and customer data
    return render_template('view_service_request.html', service_request=service_request, customer=customer)

@app.route('/booking_admin')
def booking_admin():
    if current_user.role != 'Admin':
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('unauthorized'))
    service_requests=ServiceRequest.query.all()

    return render_template ('booking_admin.html' , service_requests=service_requests)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html'), 403


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)