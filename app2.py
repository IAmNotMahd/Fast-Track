from flask import Flask
from flask import request
app = Flask(__name__)
 
#, methods=['GET', 'POST']
@app.route('/FastTrackPython', methods=['GET', 'POST'])
def hello():
	#if request.method == 'POST':
	src = str(request.form['src'])
	dst = str(request.form['dst'])
	output = "Length of src was: " + str(len(src)) + " and recieved data was: " + src + "\n" + 	"Length of dst was: " + str(len(dst)) + " and recieved data was: " + dst
	#return output
		#return "Argument recieved"
 
if __name__ == "__main__":
    app.run()