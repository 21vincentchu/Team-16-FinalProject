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

def generate_eticket(name):
    base ="INFOTC4320"
    eticket = ""

    for i in range(max(len(name), len(base))):
        if i < len(name):
            eticket += name[i]
        if i < len(base):
            eticket += base[i]
    
    return eticket.lower()

#Routes
@app.route('/', methods=['GET','POST'])
def index():
    menu_option = request.form.get('menuOption')
    
    if menu_option == 'admin':
        return redirect(url_for('login_post'))
    elif menu_option == 'reserve':
        return redirect(url_for('reserve'))
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username, password=password).first()
        if admin:
            return redirect(url_for('admin_dashboard'))
        flash('Invalid username/password combination')
    return render_template('admin.html')

@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        name = request.form['name']
        row = int(request.form['seatRow'])
        col = int(request.form['seatColumn'])

        eTicketNumber = generate_eticket(name)

        new_reservation = Reservation(
            passengerName=name,
            seatRow=row,
            seatColumn=col,
            eTicketNumber=eTicketNumber
        )
        db.session.add(new_reservation)
        db.session.commit()

        flash(f"Reservation confirmed for {name}! Your eTicket is {eTicketNumber}", "success")
        return redirect(url_for('index'))

    return render_template('reserve.html')


#Run Program
if __name__ == '__main__':
    with app.app_context():
        test_database_connection()
    
    app.run(debug=True, port=5000)
