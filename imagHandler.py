import argparse

import cv2
from PIL import Image


def capture(camera: cv2.VideoCapture) -> Image.Image:
	success, frame = camera.read()
	if not success:
		print("  !Couldn't access the Camera")
		return None
	return Image.fromarray(frame)

def optimizeImage(image: Image.Image, screenWidth: int, aspectRatio: float, args: argparse.Namespace) -> tuple[list, list,int, int]:
	width, heigh = image.size
	reWidth = screenWidth
	reHeight = int(reWidth * heigh / width * aspectRatio)
	resized = image.resize((reWidth, reHeight))
	grayscale = resized.convert(mode="L")
	pixelDataFull = list(resized.getdata())   # type: ignore
	pixelDataGray = list(grayscale.getdata()) # type: ignore
	return pixelDataFull, pixelDataGray, reWidth, reHeight
