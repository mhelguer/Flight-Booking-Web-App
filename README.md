There is a "make_airline_sql.sql" file included that you will need to
run in the schema to clear out the tables.

In order to run the file on Windows you need to first need to make sure you have pip installed. 
In the Visual Studio Code terminal type "pip-V"and it will tell you whether or not 
you have pip installed(if you downloaded a recent version of python then pip should already be installed).
Then in the terminal type "pip install flask psycopg2 flask_sqlalchemy" since you need those modules
installed to be able to run the code. Next you type in "python app.py" in the terminal and after it runs 
it will give you the address that the program is running off of. For instance it's more than likely going to be 
http://127.0.0.1:5000 like it shows in the video. 

You should see the options to press "Show All Customers" and "Show All Flights"
as well as "Destination" with a search bar next to it. If you know the desired
Arrival Airport(HOU, ORD, LAX, JFK, MIA) you can type it in the search to bring up all the flights
that go to that airport. If you choose "Show All Flights" it will bring up the flights table where
you can book a flight. When you click book flight it will bring up a page where you will enter your
information and click submit, which will update the table "customer" in the database. 

Link to demo:
https://drive.google.com/file/d/14PqBCPLGSdaWZpmb_rjEZEumAYgEI9FQ/view?usp=sharing
