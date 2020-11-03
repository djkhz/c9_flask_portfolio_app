from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os
from flask import Flask, jsonify
from flask import Flask, make_response
from flask import Flask, redirect, url_for
from flask import json
import flask_sijax
from laonlp.tokenize import word_tokenize

#https://gist.github.com/spantaleev/4433109
#from flask_sijax import sijax


app = Flask(__name__)

app.config["SIJAX_STATIC_PATH"] = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app.config["SIJAX_JSON_URI"] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/<name>')
def profile(name):
	return render_template('index.html', name=name)


@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('add_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      total = 0
  	      try:
  	      	for str_num in request.form['text'].split():
  	      		total += int(str_num)
  	      	return render_template('add_numbers.html', result=str(total))
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! 2 numbers with a space between them please"


@app.route('/shopping_list', methods=['GET','POST'])
def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          shop_list = []
          try:
            for item in request.form['text'].split():
              
              shop_list.append(item)

              
              
            return render_template('shopping_list.html', result="\n".join([str(item) for item in shop_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"
          
  	      
@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          for item in request.form['text'].split():
            answer = (datetime.datetime.now(pytz.timezone("Europe/Dublin")).strftime('Time = ' + '%H:%M:%S' + ' GMT ' + ' Year = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')

              
              
            return render_template('time.html', result=answer)

         

@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')

@app.route('/test')
def test_page():
    """Return homepage."""
    json_data = {'Hello': 'World der!'}
    return jsonify(json_data)

def generateMetrics():
    return "hello world"


@app.route('/metrics')
def metrics():
    response = make_response(generateMetrics(), 200)
    response.mimetype = "text/plain"
    return response

@app.route('/metrics2')
def metrics2():
    return generateMetrics()

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')

@app.route("/nlp", , methods=['GET','POST'])
def hellox():
    # sentence= request.args.get('text')
    # test = word_tokenize(sentence)#("ພາສາລາວໃນປັດຈຸບັນ.") # ['ພາສາລາວ', 'ໃນ', 'ປັດຈຸບັນ', '.']
    #test = json.dumps(test)
    #test = json.loads(test)
	#https://www.guru99.com/python-json.html
    #test = json.dumps(text, ensure_ascii=False).encode('utf8')
    if request.method == 'GET':
      return render_template('json.html')
    elif request.method == 'POST':
        sentence= request.form['text']
        test = word_tokenize(sentence)#("ພາສາລາວໃນປັດຈຸບັນ.") # ['ພາສາລາວ', 'ໃນ', 'ປັດຈຸບັນ', '.']
        return render_template('json.html', test=test)
        #   print(request.form['text'].split())
          
        #   shop_list = []
        #   try:
        #     for item in request.form['text'].split():
              
        #       shop_list.append(item)

              
              
            #return render_template('json.html', result="\n".join([str(item) for item in shop_list]))
            #return render_template('json.html', test=test)
        #   except ValueError:
        #     return "Easy now! Let's keep it simple! Just words with a space between them"
          
    #return render_template('json.html', test=test)
    #return json.dumps(text)

@app.route("/jax")
def hello():
    text = word_tokenize("ພາສາລາວໃນປັດຈຸບັນ.") # ['ພາສາລາວ', 'ໃນ', 'ປັດຈຸບັນ', '.']
    return jsonify(text)
	#json_string = flask.json.dumps(text, ensure_ascii=False).encode('utf8')
	#return jsonify(json_string.decode())
	#return json.dumps(text)
#result = flask.json.dumps(my_dictionary)
#print result
    #return jsonify(text)
    #return Response(json.dumps(js),  mimetype='application/json')
    #test=json.dumps(text)
    #return test

    #return text #"Hello World!<br /><a href='/sijax'>Go to Sijax test</a>"

# Sijax enabled function - notice the `@Sijax.route` decorator
# used instead of `@app.route` (above).
@flask_sijax.route(app, "/sijax")
def hello_sijax():
    # Sijax handler function receiving 2 arguments from the browser
    # The first argument (obj_response) is passed automatically
    # by Sijax (much like Python passes `self` to object methods)
    def hello_handler(obj_response, hello_from, hello_to):
        obj_response.alert('Hello from %s to %s' % (hello_from, hello_to))
        obj_response.css('a', 'color', 'green')

    # Another Sijax handler function which receives no arguments
    def goodbye_handler(obj_response):
        obj_response.alert('Goodbye, whoever you are.')
        obj_response.css('a', 'color', 'red')

    if g.sijax.is_sijax_request:
        # The request looks like a valid Sijax request
        # Let's register the handlers and tell Sijax to process it
        g.sijax.register_callback('say_hello', hello_handler)
        g.sijax.register_callback('say_goodbye', goodbye_handler)
        return g.sijax.process_request()

    return render_template('hello.html')

app.run(host=os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
	app.run(debug=False)
