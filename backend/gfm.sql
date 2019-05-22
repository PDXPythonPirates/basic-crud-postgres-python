SELECT flight_id, name, origin, destination FROM flights 
INNER JOIN passengers
ON passengers.flight_id = flights.id
ORDER BY flights.id;
