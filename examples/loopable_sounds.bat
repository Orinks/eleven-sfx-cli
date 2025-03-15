@echo off
:: Loopable Sound Effects Examples

echo Generating loopable sound effects...

:: Loopable drum beat (precise BPM for easy looping)
python ..\eleven_sfx_cli.py generate "90s hip-hop drum loop at exactly 90 BPM, seamless looping with clean start and end points, no fade" ^^
  --output drum_loop_90bpm.mp3 ^^
  --duration 2.67 ^^
  --influence 0.8

:: Ambient loop (natural environment)
python ..\eleven_sfx_cli.py generate "Forest ambience with gentle rustling leaves and distant birds, perfectly seamless loop with no noticeable transition" ^^
  --output forest_ambience_loop.mp3 ^^
  --duration 10.0 ^^
  --influence 0.7

:: Sci-fi loop (synthetic sounds)
python ..\eleven_sfx_cli.py generate "Futuristic spaceship engine room hum, continuous and consistent tone, designed as perfect loop" ^^
  --output spaceship_hum_loop.mp3 ^^
  --duration 8.0 ^^
  --influence 0.9

:: Water loop
python ..\eleven_sfx_cli.py generate "Gentle stream flowing over rocks, continuous water babbling, seamless loop with no sudden changes" ^^
  --output stream_loop.mp3 ^^
  --duration 6.0 ^^
  --influence 0.8

echo Loopable sound effects have been generated!
echo.
echo Note: For perfect loops, you may need minor audio editing to ensure the start and end connect seamlessly.
