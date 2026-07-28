import argparse

from characterSet import MODE


def argHandler() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		prog="camera",
		description="Camera control tool",
	)

	char_group = parser.add_mutually_exclusive_group(required=False)
	for key in MODE:
		char_group.add_argument(
			f"-{key}",
			dest="mode",
			action="store_const",
			const=key,
		)

	parser.add_argument(
		"-f", "--fps",
		type=int,
		default=30,
		metavar="N",
		help="Frame rate in frames per second (default: 30)",
	)

	args = parser.parse_args()
	return args
