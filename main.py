import os
import sys
import cv2
import time
import shutil
from PIL import Image

CHARACTER = {
	"ascii": { 200: "@", 150: "*", 100: "+", 50: ".", 0: " "},
	"pixel": { 200: "█", 150: "▓", 100: "▒", 50: "░", 0: " "},
	"upper": { 200: "G", 150: "D", 100: "C", 50: "I", 0: " "},
	"lower": { 200: "g", 150: "d", 100: "i", 50: ".", 0: " "},
	"kanji": { 200: "漢", 150: "林", 100: "丁", 50: "一", 0: "\u3000"},
}

def argHandler() -> str:
	if len(sys.argv) < 2:
		print("  Usage:　camera -<character>")
		sys.exit(1)
	arg = sys.argv[1]
	if not arg.startswith("-"):
		print("  Error: Argument must start with '-'.}")
		sys.exit(1)
	key = arg[1:]
	if key == "h":
		print(f"  Available options: \n    -{'\n    -'.join(CHARACTER.keys())}")
		sys.exit(0)
	if key not in CHARACTER:
		print(f"  Error: '{key}' is not a valid option.")
		sys.exit(1)
	return key

def pickCHARACTER(pixel, mode: str) -> str:
	for threshold, char in CHARACTER[mode].items():
		if pixel > threshold:
			return char
	return " "

def render(pixelData, reWidth, reHeight, mode: str) -> None:
	for i in range(reHeight):
		print("".join([pickCHARACTER(pixel, mode) for pixel in pixelData[i*reWidth:(i+1)*reWidth]][::-1]))
	print()

def optimizeImage(image: Image.Image, screenWidth: int, aspectRatio: float) -> tuple[list, int, int]:
	width, heigh = image.size
	reWidth = screenWidth
	reHeight = int(reWidth * heigh / width * aspectRatio)
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
	fps = 30
	aspectRatio = 0.5
	terminalSize = shutil.get_terminal_size()
	screenSize = (terminalSize.columns, terminalSize.lines)
	camera = cv2.VideoCapture(0)
	mode = argHandler()
	if mode == "kanji":
		aspectRatio = 1
		screenSize = (terminalSize.columns // 2, terminalSize.lines)
	while True:
		frame = capture(camera)
		if frame is None:
			continue
		pixelData, reWidth, reHeight = optimizeImage(frame, screenSize[0], aspectRatio)
		os.system("clear")
		render(pixelData, reWidth, reHeight, mode)
		time.sleep(1 / fps)

if __name__ == "__main__":
	main()
