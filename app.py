from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

#App configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'reservations.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'your_secret_key'

#SQLAlchmey models for reservation table
class Reservation(db.Model):
    '''
    Creates a reservation class and maps the reservation table into callable object
    '''
    __tablename__ = 'reservations'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    passengerName = db.Column(db.String(100), nullable=False)
    seatRow = db.Column(db.Integer, nullable=False)
    seatColumn = db.Column(db.Integer, nullable=False)
    eTicketNumber = db.Column(db.String(10), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Reservation {self.passengerName}>'
    
#SQLAlchemy model for admin table
class Admin(db.Model):
    '''
    creates a Admin class that maps the admin table into callable object
    '''
    __tablename__ = 'admins'
    
    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'<Admin {self.username}>'
    
def test_database_connection():
    """
    Simple test to check if database models are working
    """
    try:
        # Try to query the tables
        admin_count = Admin.query.count()
        reservation_count = Reservation.query.count()
        
        print(f"Database connection successful!")
        print(f"Found {admin_count} admins and {reservation_count} reservations")
        return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False


#helper functions
def get_cost_matrix():
    return 1

def get_seating_chart():
    return 1

def calculate_total_sales():
    return 1

#Routes
# index route
@app.route('/')
def index():
    return render_template('index.html')

# Admin login GET route
@app.route('/admin', methods=("GET", ))
def login_get():
    return render_template('admin.html')

# Admin login POST route
@app.route('/admin', methods=("POST", ))
def login_post():
    # gather form values
    admin_username = request.form.get('admin_username')
    admin_password = request.form.get('admin_password')

    # validate results are not empty.
    if not admin_password or not admin_username: 
        flash("Fields cannot be empty. Please enter a Username and Password.")
        return render_template('admin.html')
    
    # compare results to those on file
    admin = Admin.query.filter_by(username=admin_username).first()

    # validate password
    if admin and (admin.password == admin_password):
        # get seating chart
        seating_chart = get_seating_chart()

        # get reservation list
        reservation_list = Reservation.query.all()

    # return a render template
        return render_template('admin.html', logged_in=True, seating_chart=seating_chart, reservation_list=reservation_list)
    else:
        flash("Invalid username/password.")
        return render_template('admin.html')

# delete route
@app.route('/<res_id>/delete', methods=('GET', ))
def delete(res_id):
    # gather the reservation, delete the row
    res = Reservation.query.filter_by(id=res_id).delete()

    # commit changes
    db.session.commit()

    # flash a message
    flash(f"Reservation {res_id} successfully deleted!")

    # gather new page results
    seating_chart = get_seating_chart()
    reservation_list = Reservation.query.all()
    
    return render_template('admin.html', logged_in=True, seating_chart=seating_chart, reservation_list=reservation_list)



#Run Program
if __name__ == '__main__':
    with app.app_context():
        test_database_connection()
    
    app.run(debug=True, port=5000)
