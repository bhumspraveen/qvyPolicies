import psycopg2
from flask import Flask, request, render_template


app = Flask(__name__)  

@app.route('/', methods =["GET", "POST"])
def gfg(): 
   if request.method == "POST":
      
      
      customerid = request.form.get("customerid")
      name = request.form.get("name")
      email = request.form.get("email")
      password = request.form.get("password")
      address = request.form.get("address")
      contact = request.form.get("contact")
      nominee = request.form.get("nominee")
      relationship = request.form.get("relationship")
      data = cursor.fetchall()
      print(customerid, name, email, password, address, contact, nominee, relationship)
       
   return render_template("index.html")
 
if __name__=='__main__':
   app.run()

conn.close()

