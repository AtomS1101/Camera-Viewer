import os
import sys
import cv2
import time
import shutil
from PIL import Image

FPS = 30
MODE = "ascii"
ASPECT_RATIO = 0.5
CHARACTER = {
	"ascii": { 200: "@", 150: "*", 100: "+", 50: ".", 0: " "},
	"pixel": { 200: "█", 150: "▓", 100: "▒", 50: "░", 0: " "},
	"upper": { 200: "G", 150: "D", 100: "C", 50: "I", 0: " "},
	"lower": { 200: "g", 150: "d", 100: "i", 50: ".", 0: " "},
}

def pickCHARACTER(pixel, mode: str) -> str:
	for threshold, char in CHARACTER[mode].items():
		if pixel > threshold:
			return char
	return " "

def render(pixelData, reWidth, reHeight, mode: str):
	for i in range(reHeight):
		print("".join([pickCHARACTER(pixel, mode) for pixel in pixelData[i*reWidth:(i+1)*reWidth]][::-1]))
	print()

def optimizeImage(image, screenWidth: int) -> tuple[list, int, int]:
	width, heigh = image.size
	reWidth = screenWidth
	reHeight = int(reWidth * heigh / width * ASPECT_RATIO)
	resized = image.resize((reWidth, reHeight))
	grayscale = resized.convert(mode="L")
	pixelData = list(grayscale.getdata())
	return pixelData, reWidth, reHeight

def capture(camera: cv2.VideoCapture) -> Image.Image:
	success, frame = camera.read()
	if not success:
		print("  !Couldn't access the Camera")
		return None
	return Image.fromarray(frame)

def main():
	terminalSize = shutil.get_terminal_size()
	screenSize = (terminalSize.columns, terminalSize.lines)
	camera = cv2.VideoCapture(0)
	while True:
		frame = capture(camera)
		if frame is None:
			continue
		pixelData, reWidth, reHeight = optimizeImage(frame, screenSize[0])
		os.system("clear")
		render(pixelData, reWidth, reHeight, MODE)
		time.sleep(1 / FPS)

if __name__ == "__main__":
	main()
