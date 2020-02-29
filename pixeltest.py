import time
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18,46)

while True:
	pixels.fill((255, 0, 0))
	time.sleep(1)
	pixels.fill((0,255,0))
	time.sleep(1)
	pixels.fill((0,0,255))
	time.sleep(1)
