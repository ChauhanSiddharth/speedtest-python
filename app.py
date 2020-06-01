from flask import Flask, render_template, request
import speedtest
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET','POST'])
def home():
	if request.method == 'POST':
		s = speedtest.Speedtest()
		s.get_servers()
		s.get_best_server()
		s.download()
		s.upload()
		res = s.results.dict()
		download = round(res["download"]/1000,2)
		upload = round(res["upload"]/1000,2)
		ping = round(res["ping"])
		client = res["client"]["isp"]
		country = res["client"]["country"]
		print("-->Download Speed: {:.2f} Kb/s\n-->Upload Speed: {:.2f} Kb/s\n-->Ping: {}\n-->ISP: {}, {}".format(download,upload,ping, client,country))
		return render_template('home.html', download=download, upload=upload,ping=ping,client=client)
	else:
		return render_template('home.html', download=0, upload=0,ping=0,client="---")	

if __name__ == '__main__':
	app.run()