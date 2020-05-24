from flask import Flask, render_template, request
import speedtest
app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/test')
def test():
	s = speedtest.Speedtest()
	s.get_servers()
	s.get_best_server()
	s.download()
	s.upload()
	res = s.results.dict()
	download = round(res["download"])/1000
	upload = round(res["upload"])/1000
	ping = round(res["ping"])
	client = res["client"]["isp"]
	country = res["client"]["country"]
	print("-->Download Speed: {:.2f} Kb/s\n-->Upload Speed: {:.2f} Kb/s\n-->Ping: {}\n-->ISP: {}, {}".format(download,upload,ping, client,country))
	return render_template('result.html', download=download, upload=upload,ping=ping,client=client)

if __name__ == '__main__':
    app.run()