
from flask import Flask,render_template
import json
import random

app = Flask(__name__)
app.config['DEBUG'] = True


data = {}
for i in range(8):
	key = "node" + str(i)
	y = [0]*50
	x = range(2000,2050)
	data[key] = [x,y]

@app.route('/index')
def index():
	return render_template('index.html')

	
@app.route('/test')
def test():
	return render_template("test.html")
	
@app.route('/getdata/<nodenum>')
def getdata(nodenum):
	global data
	x = data[nodenum][0]
	y = data[nodenum][1]
	datanum = len(x)
	value = random.randint(20,100)
	xvalue = x[-1] + 1
	y.pop(0)
	y.append(value)
	x.pop(0)
	x.append(xvalue)
	return json.dumps([{"date":x[i],"close":y[i]} for i in range(datanum)])
	

if __name__ == "__main__":
	app.run(host="0.0.0.0")