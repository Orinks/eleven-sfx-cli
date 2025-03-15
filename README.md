# Eleven Labs Sound Effects CLI

A command-line interface tool for generating sound effects using the Eleven Labs API. This CLI provides all the functionality and parameters supported by the API for maximum flexibility.

## Features

- Generate high-quality sound effects from text descriptions
- Support for all audio output formats (MP3, PCM, μ-law)
- Configurable duration and prompt influence
- Rich terminal output with progress indicators

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

You'll need an API key from Eleven Labs. You can provide it in one of three ways:

1. Create a `.env` file in the project directory with your API key:

```
ELEVENLABS_API_KEY=your_api_key_here
```

2. Set the `ELEVENLABS_API_KEY` environment variable

3. Pass it directly with the `--api-key` option when running the command

## Usage

### Basic Usage

```bash
python eleven_sfx_cli.py generate "Dog barking in the distance"
```

### With Options

```bash
python eleven_sfx_cli.py generate \
    "Spacious braam suitable for high-impact movie trailer moments" \
    --output trailer_braam.mp3 \
    --format mp3_44100_192 \
    --duration 5.5 \
    --influence 0.7 \
    --verbose
```

### List Available Output Formats

```bash
python eleven_sfx_cli.py generate --list-formats
```

## Options

- `text`: The text description of the sound effect to generate (required)
- `--output, -o`: Output file path (default: `output.mp3`)
- `--api-key`: Eleven Labs API key (if not set via environment variable)
- `--format, -f`: Output format of the generated audio (default: `mp3_44100_128`)
- `--duration, -d`: Duration of sound in seconds (0.5 to 22). If not specified, optimal duration will be determined automatically
- `--influence, -i`: Prompt influence value (0.0 - 1.0). Higher values make generation follow the prompt more closely (default: 0.3)
- `--verbose, -v`: Enable verbose output
- `--list-formats`: List available output formats and exit

## Output Formats

### Default Tier
- `mp3_44100_128` - MP3, 44.1kHz sample rate, 128kbps
- `mp3_44100_96` - MP3, 44.1kHz sample rate, 96kbps
- `mp3_44100_64` - MP3, 44.1kHz sample rate, 64kbps
- `mp3_44100_32` - MP3, 44.1kHz sample rate, 32kbps
- `mp3_22050_32` - MP3, 22.05kHz sample rate, 32kbps
- `pcm_22050` - PCM, 22.05kHz sample rate
- `mulaw_8000` - μ-law format, 8kHz (for Twilio)

### Creator Tier or Above
- `mp3_44100_192` - MP3, 44.1kHz sample rate, 192kbps

### Pro Tier or Above
- `pcm_44100` - PCM, 44.1kHz sample rate

## License

MIT
