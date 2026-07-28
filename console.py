import argparse

from characterSet import MODE


def pickCHARACTER(pixel, mode: str) -> str:
	for threshold, char in MODE[mode if mode != None else "ascii"].items():
		if pixel > threshold:
			return char
	return " "

def render(fullColor, grayscale, reWidth, reHeight, args: argparse.Namespace) -> None:
	if args.mode == "color" or args.mode == "3bit":
		for y in range(reHeight):
			line = ""
			threshold = 128
			for x in range(y * reWidth, (y + 1) * reWidth):
				if args.mode == "color":
					color = (fullColor[x][0], fullColor[x][1], fullColor[x][2])
				else:
					color = (255 if fullColor[x][0] > threshold else 0, 255 if fullColor[x][1] > threshold else 0, 255 if fullColor[x][2] > threshold else 0)
				char = f"\033[38;2;{color[0]};{color[1]};{color[2]}m{MODE["color"]}\033[0m"
				line = char + line
			print(line)
	else:
		for i in range(reHeight):
			print("".join([pickCHARACTER(pixel, args.mode) for pixel in grayscale[i*reWidth:(i+1)*reWidth]][::-1]))
