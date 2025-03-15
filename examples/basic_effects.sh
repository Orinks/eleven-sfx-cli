#!/bin/bash
# Basic Sound Effects Generation Examples

# Simple dog bark effect
python ../eleven_sfx_cli.py generate "Dog barking in the distance" --output dog_bark.mp3

# Atmospheric wind sound
python ../eleven_sfx_cli.py generate "Gentle wind blowing through autumn leaves" --output wind.mp3

# Glass breaking sound effect
python ../eleven_sfx_cli.py generate "Glass shattering on concrete floor" --output glass_break.mp3

# Thunder sound
python ../eleven_sfx_cli.py generate "Distant thunder rumbling, approaching storm" --output thunder.mp3

echo "Basic sound effects have been generated!"
