#!/usr/bin/env python3
# Why didn't I write using classes???
# I just didn't expect the project to grow this large...

import os
import shutil
import time

import cv2

from argHandler import argHandler
from console import render
from imagHandler import capture, optimizeImage


def main():
	args = argHandler()
	aspectRatio = 0.5 if args.mode != "kanji" else 1
	camera = cv2.VideoCapture(0)
	try:
		while True:
			frame = capture(camera)
			if frame is None:
				continue
			terminalSize = shutil.get_terminal_size()
			screenSize = (terminalSize.columns if args.mode != "kanji" else terminalSize.columns // 2, terminalSize.lines)
			pixelDataFull, pixelDataGray, reWidth, reHeight = optimizeImage(frame, screenSize[0], aspectRatio, args)
			os.system("clear")
			render(pixelDataFull, pixelDataGray, reWidth, reHeight, args)
			time.sleep(1 / args.fps)
	except KeyboardInterrupt:
		print("  Exiting...")
	finally:
		camera.release()
		cv2.destroyAllWindows()

if __name__ == "__main__":
	main()
