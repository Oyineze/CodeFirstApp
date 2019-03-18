from fizzbuzz import fizz_buzz
from flask import Flask, render_template, request

app = Flask( "App" )

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/<string:name>")
def hello_name(name):
    return render_template("index.html", name=name.title())

app.run(debug = True )



'''
@app.route("/test")
def hello_test():
    return "Hello test"
'''

'''
@app.route("/<string:name>")
def hello_name(name):
    return f"Hello {name}!"

app.run( debug = True )
'''
'''
def fizz_buzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)
'''
'''
@app.route("/<int:x>")
def hello_fizz(x):
    return f"Hello {fizz_buzz(x)}!"

app.run( debug = True )
'''