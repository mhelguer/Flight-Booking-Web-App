SELECT flight_id, flight_no, scheduled_departure,     scheduled_arrival, departure_airport, arrival_airport, status,     seats_available, seats_booked FROM flights WHERE flight_no = 'PG0100'
SELECT seats_booked < seats_available
FROM flights
WHERE flight_no = 'PG0100';
SELECT flight_id, flight_no, scheduled_departure,         scheduled_arrival, departure_airport, arrival_airport, status,         seats_available, seats_booked FROM flights
SELECT flight_id, flight_no, scheduled_departure,     scheduled_arrival, departure_airport, arrival_airport, status,     seats_available, seats_booked FROM flights WHERE flight_no = 'PG0100'
SELECT seats_booked < seats_available
FROM flights
WHERE flight_no = 'PG0100';
SELECT flight_id, flight_no, scheduled_departure, scheduled_arrival,         departure_airport, arrival_airport, status, seats_available, seats_booked         FROM flights WHERE arrival_airport = 'JFK';
SELECT flight_id, flight_no, scheduled_departure, scheduled_arrival,         departure_airport, arrival_airport, status, seats_available, seats_booked         FROM flights WHERE arrival_airport = 'JFK';
SELECT flight_id, flight_no, scheduled_departure,     scheduled_arrival, departure_airport, arrival_airport, status,     seats_available, seats_booked FROM flights WHERE flight_no = 'PG0010'
SELECT seats_booked < seats_available
FROM flights
WHERE flight_no = 'PG0010';
SELECT flight_id, flight_no, scheduled_departure,     scheduled_arrival, departure_airport, arrival_airport, status,     seats_available, seats_booked FROM flights WHERE flight_no = 'PG0010'
SELECT seats_booked < seats_available
FROM flights
WHERE flight_no = 'PG0010';
START TRANSACTION; UPDATE flights SET seats_booked=seats_booked+2, seats_available=seats_available-2 WHERE flight_no = 'PG0010'; COMMIT;
SELECT * FROM customer
SELECT * FROM customer
START TRANSACTION; UPDATE customer SET boarded='Yes' WHERE passenger_id = '1'; COMMIT;
SELECT * FROM customer
SELECT * FROM customer
SELECT flight_id, flight_no, scheduled_departure,     scheduled_arrival, departure_airport, arrival_airport, status,     seats_available, seats_booked FROM flights
SELECT flight_id, flight_no, scheduled_departure,     scheduled_arrival, departure_airport, arrival_airport, status,     seats_available, seats_booked FROM flights
SELECT flight_id, flight_no, scheduled_departure,     scheduled_arrival, departure_airport, arrival_airport, status,     seats_available, seats_booked FROM flights WHERE flight_no = 'PG0100'
SELECT seats_booked < seats_available
FROM flights
WHERE flight_no = 'PG0100';
SELECT flight_id, flight_no, scheduled_departure,     scheduled_arrival, departure_airport, arrival_airport, status,     seats_available, seats_booked FROM flights WHERE flight_no = 'PG0100'
SELECT seats_booked < seats_available
FROM flights
WHERE flight_no = 'PG0100';
START TRANSACTION; UPDATE flights SET seats_booked=seats_booked+50, seats_available=seats_available-50 WHERE flight_no = 'PG0100'; COMMIT;
SELECT flight_id, flight_no, scheduled_departure,     scheduled_arrival, departure_airport, arrival_airport, status,     seats_available, seats_booked FROM flights
SELECT flight_id, flight_no, scheduled_departure,     scheduled_arrival, departure_airport, arrival_airport, status,     seats_available, seats_booked FROM flights WHERE flight_no = 'PG0100'
SELECT seats_booked < seats_available
FROM flights
WHERE flight_no = 'PG0100';
SELECT flight_id, flight_no, scheduled_departure,         scheduled_arrival, departure_airport, arrival_airport, status,         seats_available, seats_booked FROM flights
SELECT * FROM customer
