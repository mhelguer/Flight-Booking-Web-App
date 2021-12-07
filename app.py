from flask import Flask, render_template, request
from models import db, User
import psycopg2, logging
app = Flask(__name__)

output_file = open("query.sql", "w+")
output_file.close()

POSTGRES = {
 'user': 'postgres',
 'db': 'airportdb',
 'host': 'localhost',
 'port': '5432',
}
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

# homepage
@app.route('/')
def index():
    return render_template('index.html')

# inserts into the table
@app.route('/postU', methods=['POST', 'GET'])
def postU():
    # if "show all customers" button pressed
    if 'showAll' in request.form:
        return allCustomers()
    # goes to page showing all flights
    elif 'flights' in request.form:
        return allFlights()

    # goes to page showing all flights that go to the destination
    elif 'search' in request.form:            
        dest=request.form.get("destination")
        
        return destination(dest)
    
    # goes to page where customer wants to book a flight    
    elif 'boarded' in request.form:
        boarded_id=request.form.get("boarded")
        return customerBoarded(str(boarded_id))
        
    return render_template('addU.html')

# displays searched flights
@app.route("/search/<dest>")
def destination(dest):
    
    con = psycopg2.connect(database = "airportdb",user = 'postgres', port=5432, host="localhost")
    cur = con.cursor()

    # column names
    headings=(("flight id"), ("flight number"), ("scheduled departure"), 
    ("scheduled arrival"), ("departure airport"), ("arrival airport"), ("status"),
     ("seats available"), ("seats booked"))
    
    sql_query1= "SELECT flight_id, flight_no, scheduled_departure, scheduled_arrival, \
        departure_airport, arrival_airport, status, seats_available, seats_booked \
        FROM flights WHERE arrival_airport = '"+str(dest)+"';"

    cur.execute(sql_query1)
    with open("query.sql", "a") as output_file:
        output_file.write(sql_query1 + '\n')
    data = cur.fetchall()

    sql_query2= "SELECT flight_no FROM flights WHERE arrival_airport= '"+str(dest)+"';"
    cur.execute(sql_query2);
    with open("query.sql", "a") as output_file:
        output_file.write(sql_query1 + '\n')
    num = cur.fetchall()
    

    # if "home" button pressed go to homepage
    if 'home' in request.form:
        return index()
    # if "Book Flight" button pressed go to booking page
    elif 'book' in request.form:
        return book_flight(num)

    #return render_template('allFlights.html', headings=headings, data=data)
    return render_template('destination.html', headings=headings, data=data)

# displays forms to book flight
@app.route('/book/<num>', methods=['GET', 'POST'])
def book_flight(num):

    con = psycopg2.connect(database = "airportdb", user = 'postgres', port=5432, host="localhost")
    cur = con.cursor()

    # column names
    headings=(("flight id"), ("flight number"), ("scheduled departure"), 
    ("scheduled arrival"), ("departure airport"), ("arrival airport"), ("status"),
    ("seats available"), ("seats booked"))

    sql_query2 = "SELECT flight_id, flight_no, scheduled_departure, \
    scheduled_arrival, departure_airport, arrival_airport, status, \
    seats_available, seats_booked FROM flights WHERE flight_no = '"+num+"'"

    cur.execute(sql_query2)
    with open("query.sql", "a") as output_file:
        output_file.write(sql_query2 + '\n')
    data = cur.fetchall()

    # seeing if seat is available
    sql_query3 = "SELECT seats_booked < seats_available\nFROM flights\nWHERE flight_no = '"+num+"';"
    cur.execute(sql_query3)
    with open("query.sql", "a") as output_file:
        output_file.write(sql_query3 + '\n')
    seat_available = cur.fetchone()

    # seat not available, return same page but with "That Flight is Full!"
    if seat_available[0]==False:
        headings=(("flight id"), ("flight number"), ("scheduled departure"), 
        ("scheduled arrival"), ("departure airport"), ("arrival airport"), ("status"),
        ("seats available"), ("seats booked"))

        sql_query4 = "SELECT flight_id, flight_no, scheduled_departure, \
        scheduled_arrival, departure_airport, arrival_airport, status, \
        seats_available, seats_booked FROM flights"

        cur.execute(sql_query4)
        with open("query.sql", "a") as output_file:
            output_file.write(sql_query4 + '\n')
        data = cur.fetchall()

        return render_template('allFlights.html', headings=headings, data=data, error="That flight is full!")
    
    # seat is available
    if request.method=='POST':
        name=request.form.get("name")
        # needed or else it automatically sends empty values in User below
        while (not name):
            name=request.form.get("name")
            return render_template('bookFlight.html', headings=headings, data=data, num = num)


        # getting the values to put into each column in table "customer"
        user = User(
            name=name,
            telephone = request.form.get("telephone"),
            email=request.form.get("email"), 
            party = request.form.get("party"),
            card_number = request.form.get("card number"),
            flight_no = num,
            boarded = "No")
        
        # everything ready, commit new user into table "customer" and increment seats_booked of the flight
        db.session.add(user)
        db.session.commit()
        sql_query5="START TRANSACTION; UPDATE flights SET seats_booked=seats_booked+"+str(request.form.get("party"))+", seats_available=seats_available-"+str(request.form.get("party"))+" WHERE flight_no = '"+num+"'; COMMIT;"
        cur.execute(sql_query5)
        with open("query.sql", "a") as output_file:
            output_file.write(sql_query5 + '\n')

        # return to homepage
        return index()
        
    
    # if "home" button pressed go to homepage
    if 'home' in request.form:
        return index()

    return render_template('bookFlight.html', headings=headings, data=data, num = num)

# displays all flights
@app.route('/flight/all',methods=['GET', 'POST'])
def allFlights():
    con = psycopg2.connect(database = "airportdb", user = 'postgres', port=5432, host="localhost")
    cur = con.cursor()
    
    # column names
    headings=(("flight id"), ("flight number"), ("scheduled departure"), 
    ("scheduled arrival"), ("departure airport"), ("arrival airport"), ("status"),
     ("seats available"), ("seats booked"))

    sql_query6 = "SELECT flight_id, flight_no, scheduled_departure, \
    scheduled_arrival, departure_airport, arrival_airport, status, \
    seats_available, seats_booked FROM flights"

    cur.execute(sql_query6)
    with open("query.sql", "a") as output_file:
        output_file.write(sql_query6 + '\n')
    data = cur.fetchall()

    # if "home" button pressed go to homepage
    if 'home' in request.form:
        return index()
    # if "Book Flight" button pressed go to booking page
    elif 'book' in request.form:        
        return book_flight(num)
    
    return render_template('allFlights.html', headings=headings, data=data)

# displays table "customer" at the URL in the @app.route()
@app.route('/customer/all',methods=['GET', 'POST']) 
def allCustomers():
    con = psycopg2.connect(database = "airportdb", user = 'postgres', port=5432, host="localhost")
    cur = con.cursor()
    
    # column names
    headings=(("passenger id"), ("name"), ("telephone"), ("email"), ("boarding id"), ("party"), ("card number"), ("flight number"), ("boarded"))

    sql_query7 = "SELECT * FROM customer"

    cur.execute(sql_query7)
    with open("query.sql", "a") as output_file:
        output_file.write(sql_query7 + '\n')
    data = cur.fetchall()

    # if "home" button pressed go to homepage
    if 'home' in request.form:
        return index()
    elif 'boarded' in request.form:        
        return render_template('index.html')
        #return customerBoarded(boarded_id)
    return render_template('customer.html', headings=headings, data=data)
    
    
    #FIXME: pid increases each time a board button is pressed, and updates the row of the new pid to Boarded=Yes
@app.route('/customer/<pid>', methods=['GET', 'POST'])
def customerBoarded(pid):
    con = psycopg2.connect(database = "airportdb", user = 'postgres', port=5432, host="localhost")
    cur = con.cursor()
    
    sql_query8 = "SELECT * FROM customer"

    cur.execute(sql_query8)
    with open("query.sql", "a") as output_file:
        output_file.write(sql_query8 + '\n')
    data = cur.fetchall()
    headings=(("passenger id"), ("name"), ("telephone"), ("email"), ("boarding id"), ("party"), ("card number"), ("flight number"), ("boarded"))

    sql_query9="START TRANSACTION; UPDATE customer SET boarded='Yes' WHERE passenger_id = '"+pid+"'; COMMIT;"
    # column names
    cur.execute(sql_query9)
    with open("query.sql", "a") as output_file:
        output_file.write(sql_query9 + '\n')

    cur.execute(sql_query8)
    with open("query.sql", "a") as output_file:
        output_file.write(sql_query8 + '\n')
    data = cur.fetchall()
    # seat is available
    if 'board' in request.form:
        sql_query9="START TRANSACTION; UPDATE customer SET boarded='Yes' WHERE passenger_id = '"+pid+"'; COMMIT;"
        # column names
        
        cur.execute(sql_query8)
        with open("query.sql", "a") as output_file:
            output_file.write(sql_query8 + '\n')
        data = cur.fetchall()

    return render_template('customer.html', headings=headings,  data=data)

if __name__ == '__main__':
    app.run(debug=True)
