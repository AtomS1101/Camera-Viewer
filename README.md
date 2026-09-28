# Camera-Viewer
A small command-line tool that shows your camera feed as ASCII art right in the terminal.

## Usage

```
camera [-h] [-ascii | -pixel | -upper | -lower | -kanji | -color | -3bit] [-f N]
```

## Options

### General

| Option | Description |
| --- | --- |
| `-h`, `--help` | Show the help message and exit |
| `-f N`, `--fps N` | Frame rate in frames per second (default: `30`) |

### Character sets

These options only change which characters are used to draw the image.
You can pick **one** at a time (they are mutually exclusive).

| Option | Character set |
| --- | --- |
| `-ascii` | Standard ASCII characters |
| `-pixel` | Pixel-style characters |
| `-upper` | Uppercase letters |
| `-lower` | Lowercase letters |
| `-kanji` | Kanji characters |
| `-color` | Display with full-color |
| `-3bit` | Display with 3-bit color |

## Examples

```sh
# Run with the default settings
camera

# Draw with kanji characters
camera -kanji

# Draw with uppercase letters at 15 fps
camera -upper -f 15

# Use 3-bit color at 60 fps
camera -3bit --fps 60
```
