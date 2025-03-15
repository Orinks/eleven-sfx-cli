#!/usr/bin/env python3
"""
Batch Sound Effect Generation

This script demonstrates how to generate multiple sound effects programmatically
using the Eleven Labs CLI tool after it's been installed globally.
"""

import os
import subprocess
import time
from pathlib import Path

# Create output directory
output_dir = Path("generated_sounds")
output_dir.mkdir(exist_ok=True)

# List of sound effects to generate with their descriptions
sound_effects = [
    {
        "name": "footsteps_wood",
        "description": "Footsteps walking on wooden floor, slow pace",
        "duration": 4.0,
        "influence": 0.6
    },
    {
        "name": "door_creak",
        "description": "Old wooden door creaking open slowly",
        "duration": 3.0,
        "influence": 0.7
    },
    {
        "name": "rain_light",
        "description": "Light rain falling on rooftop, gentle patter",
        "duration": 8.0,
        "influence": 0.5
    },
    {
        "name": "fire_crackling",
        "description": "Fire crackling in fireplace, warm and cozy",
        "duration": 6.0,
        "influence": 0.6
    },
    {
        "name": "keyboard_typing",
        "description": "Fast typing on mechanical keyboard",
        "duration": 5.0,
        "influence": 0.8
    }
]

# Generate each sound effect
for idx, effect in enumerate(sound_effects, 1):
    print(f"[{idx}/{len(sound_effects)}] Generating: {effect['name']}")
    
    # Construct the output path
    output_file = output_dir / f"{effect['name']}.mp3"
    
    # Build the command
    cmd = [
        "eleven_sfx_cli",  # If installed globally, otherwise use full path
        "generate", 
        effect["description"],
        "--output", str(output_file),
        "--duration", str(effect["duration"]),
        "--influence", str(effect["influence"]),
    ]
    
    # Run the command
    try:
        subprocess.run(cmd, check=True)
        print(f"✓ Created {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating {effect['name']}: {e}")
    
    # Small pause between generations
    if idx < len(sound_effects):
        time.sleep(1)

print(f"\nAll sound effects have been generated in the '{output_dir}' directory.")
