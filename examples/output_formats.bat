@echo off
:: Output Format Examples

echo Generating sound effects in different formats...

:: Standard MP3 (Default Tier)
python ..\eleven_sfx_cli.py generate "Piano chord progression in C major" ^^
  --output piano_mp3_44100_128.mp3 ^^
  --format mp3_44100_128

:: Lower quality MP3 (good for size constraints)
python ..\eleven_sfx_cli.py generate "Piano chord progression in C major" ^^
  --output piano_mp3_22050_32.mp3 ^^
  --format mp3_22050_32

:: PCM format (if available on your plan)
python ..\eleven_sfx_cli.py generate "Piano chord progression in C major" ^^
  --output piano_pcm_22050.wav ^^
  --format pcm_22050

:: mulaw format (for telephony applications like Twilio)
python ..\eleven_sfx_cli.py generate "Piano chord progression in C major" ^^
  --output piano_mulaw_8000.mulaw ^^
  --format mulaw_8000

echo Output format examples have been generated!
