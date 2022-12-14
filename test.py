import psycopg2
conn = psycopg2.connect(database="register", user='postgres', password='test', host='127.0.0.1', port= '5432')
cursor = conn.cursor()
#cursor.execute("SELECT * FROM register;")
cursor.execute("INSERT INTO register (customerid, name, email, password, address, contact, nominee, relationship) VALUES (1234, 'Bhuma', 'bhuma@gmail.com', 'test123', 'chennai', 12334456, 'Lokesh', 'Mother');")
#data = cursor.fetchone()
#print(data)
