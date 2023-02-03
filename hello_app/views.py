from datetime import datetime
import math
from flask import Flask, render_template
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/sleep/")
def sleep():
    
    import time
    import random
    time.sleep(random.random())
    return "hello"

def isPrime(n):
   if n == 1:
      return False
   if n == 2:
      return True
   if n > 2 and n % 2 ==0:
      return False

   max_divisor = math.floor(math.sqrt(n))
   for d in range(3, 1 + max_divisor,2):
     if n % d ==0:
        return False
   return True

@app.route("/prime/")
def prime():
    
    primes = [x for x in range(1,100000) if isPrime(x) ==True]
    return str(sum(primes))


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
