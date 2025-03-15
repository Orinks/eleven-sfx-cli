# Eleven Labs Sound Effects CLI Examples

This directory contains example scripts demonstrating various ways to use the Eleven Labs Sound Effects CLI tool.

## Examples Overview

### Basic Sound Effects
- `basic_effects.bat` (Windows) / `basic_effects.sh` (Linux/Mac)
- Demonstrates generating simple sound effects with default parameters

### Loopable Sounds
- `loopable_sounds.bat`
- Shows how to create sound effects designed to loop seamlessly
- Uses specific prompt engineering and parameters for better looping results

### Output Formats
- `output_formats.bat`
- Examples of generating the same sound in different audio formats and qualities

### Programmatic Usage
- `batch_generation.py`
- Python script that demonstrates how to generate multiple sound effects programmatically
- Creates a batch of different sound effects with customized parameters

## Running the Examples

### Windows
Double-click on any `.bat` file or run from command prompt:
```
cd examples
basic_effects.bat
```

### Linux/Mac
Make the shell scripts executable and run:
```bash
cd examples
chmod +x basic_effects.sh
./basic_effects.sh
```

### Python Script
```bash
cd examples
python batch_generation.py
```

## Note on API Keys

All examples assume you've already configured your API key using one of the methods described in the main README:
1. Creating a `.env` file in the project root
2. Setting the `ELEVENLABS_API_KEY` environment variable
3. Passing the key via the `--api-key` parameter (not recommended for scripts)
