from flask import Flask, render_template, request
import time
import board
import neopixel
import sys
pixels = neopixel.NeoPixel(board.D18,46)

red = 0
green = 0
blue = 255


app = Flask(__name__)
@app.route("/")

def index():
	templateData = {
		'title' : 'Parts Storage Database',
		}
	return render_template('index.html', **templateData)

@app.route("/drawer/<drawerStr>")
def action(drawerStr):
	drawerNo = int(drawerStr)
	pixels.fill((0,255,0))
	if(drawerNo == 1):
		pixels[0] = (red,green,blue)
		pixels[1] = (red,green,blue)
		pixels[2] = (red,green,blue)
	else:
		pixels[drawerNo+1] = (red,green,blue)

	return render_template('index.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)

