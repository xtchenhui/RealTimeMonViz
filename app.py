from flask import Flask,render_template
import json
import random
import kafkadata

app = Flask(__name__)
app.config['DEBUG'] = True


data = {}
tname = {
		"node0":"192.168.10.160",
		"node1":"192.168.10.164",
		"node2":"192.168.10.165",
		"node3":"192.168.10.166",
		"node4":"192.168.10.161",
        "node5":"192.168.10.162",
		"node6":"192.168.10.163",
		"node7":"192.168.10.168"
	}

for i in range(8):
	key = "node" + str(i)
	y = [0]*500
	x = range(0,500)
	data[key] = [x,y]

kafakaagent =  kafkadata.KafkaMsg()

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
    msg = kafkaagent.getLatestData(tname[nodenum])
    values = msg.split("|")
    datetime = values[1]
    xvalue = datetime.split()[1]
    yvalue = float(values[2])
    y.pop(0)
    y.append(yvalue)
    x.pop(0)
    x.append(xvalue)
    return json.dumps([{"date":x[i],"close":y[i]} for i in range(datanum)])

if __name__ == "__main__":
    app.run(threaded = True, host="0.0.0.0",port = 6000)
