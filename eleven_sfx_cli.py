#!/usr/bin/env python3
"""
Eleven Labs Sound Effects CLI

A command-line tool for generating sound effects using the Eleven Labs API.
"""

import os
import sys
import time
from pathlib import Path
from typing import List, Optional

import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from elevenlabs.client import ElevenLabs
from elevenlabs.text_to_sound_effects.types.text_to_sound_effects_convert_request_output_format import (
    TextToSoundEffectsConvertRequestOutputFormat,
)

# Initialize typer app and console
app = typer.Typer(
    help="Generate sound effects using Eleven Labs API",
    add_completion=False,
)
console = Console()

# Available output formats
OUTPUT_FORMATS = [
    "mp3_44100_128",  # Default: MP3 with 44.1kHz sample rate at 128kbps
    "mp3_44100_192",  # Creator tier+: MP3 with 44.1kHz sample rate at 192kbps
    "mp3_44100_96",   # MP3 with 44.1kHz sample rate at 96kbps
    "mp3_44100_64",   # MP3 with 44.1kHz sample rate at 64kbps
    "mp3_44100_32",   # MP3 with 44.1kHz sample rate at 32kbps
    "mp3_22050_32",   # MP3 with 22.05kHz sample rate at 32kbps
    "pcm_44100",      # Pro tier+: PCM with 44.1kHz sample rate
    "pcm_22050",      # PCM with 22.05kHz sample rate
    "mulaw_8000",     # μ-law format (commonly used for Twilio audio inputs)
]


def validate_api_key() -> str:
    """Validate that the API key is available."""
    # Try to load from .env file
    load_dotenv()
    
    # Check environment variable
    api_key = os.getenv("ELEVENLABS_API_KEY")
    
    if not api_key:
        console.print(
            "\n[bold red]Error:[/bold red] ELEVENLABS_API_KEY environment variable not found."
        )
        console.print(
            "\nPlease either:"
            "\n  1. Create a .env file with your ELEVENLABS_API_KEY, or"
            "\n  2. Set the ELEVENLABS_API_KEY environment variable, or"
            "\n  3. Use the --api-key option to provide your key directly.\n"
        )
        sys.exit(1)
    
    return api_key


@app.command()
def generate(
    text: str = typer.Argument(
        ..., 
        help="The text description of the sound effect to generate"
    ),
    output_file: Path = typer.Option(
        "output.mp3", 
        "--output", "-o",
        help="Output file path"
    ),
    api_key: Optional[str] = typer.Option(
        None, 
        "--api-key", 
        help="Eleven Labs API key (if not set via environment variable)",
        envvar="ELEVENLABS_API_KEY"
    ),
    output_format: str = typer.Option(
        "mp3_44100_128", 
        "--format", "-f",
        help=f"Output format of the generated audio",
        show_choices=True,
    ),
    duration: Optional[float] = typer.Option(
        None, 
        "--duration", "-d",
        help="Duration of sound in seconds (0.5 to 22). If not specified, optimal duration will be determined from the text"
    ),
    prompt_influence: float = typer.Option(
        0.3, 
        "--influence", "-i",
        help="Prompt influence value (0.0 - 1.0). Higher values make generation follow the prompt more closely",
        min=0.0,
        max=1.0,
    ),
    verbose: bool = typer.Option(
        False, 
        "--verbose", "-v", 
        help="Enable verbose output"
    ),
    list_formats: bool = typer.Option(
        False, 
        "--list-formats", 
        help="List available output formats and exit"
    ),
) -> None:
    """Generate a sound effect from a text description."""
    # Check if we just need to list formats
    if list_formats:
        console.print("\n[bold]Available Output Formats:[/bold]")
        console.print("\n[bold yellow]Default tier:[/bold yellow]")
        console.print("  mp3_44100_128  - MP3, 44.1kHz sample rate, 128kbps")
        console.print("  mp3_44100_96   - MP3, 44.1kHz sample rate, 96kbps")
        console.print("  mp3_44100_64   - MP3, 44.1kHz sample rate, 64kbps")
        console.print("  mp3_44100_32   - MP3, 44.1kHz sample rate, 32kbps")
        console.print("  mp3_22050_32   - MP3, 22.05kHz sample rate, 32kbps")
        console.print("  pcm_22050      - PCM, 22.05kHz sample rate")
        console.print("  mulaw_8000     - μ-law format, 8kHz (for Twilio)")
        console.print("\n[bold yellow]Creator tier or above:[/bold yellow]")
        console.print("  mp3_44100_192  - MP3, 44.1kHz sample rate, 192kbps")
        console.print("\n[bold yellow]Pro tier or above:[/bold yellow]")
        console.print("  pcm_44100      - PCM, 44.1kHz sample rate")
        return

    # Validate output format
    if output_format not in OUTPUT_FORMATS:
        console.print(
            f"\n[bold red]Error:[/bold red] Invalid output format: {output_format}"
            f"\nUse --list-formats to see available options.\n"
        )
        sys.exit(1)
        
    # Validate duration
    if duration is not None and (duration < 0.5 or duration > 22):
        console.print(
            f"\n[bold red]Error:[/bold red] Duration must be between 0.5 and 22 seconds.\n"
        )
        sys.exit(1)
    
    # Use provided API key or validate from environment
    if not api_key:
        api_key = validate_api_key()
    
    # Display generation info
    console.print(f"\n[bold]Generating Sound Effect:[/bold] {text}")
    if verbose:
        console.print(f"[dim]Output File:[/dim] {output_file}")
        console.print(f"[dim]Format:[/dim] {output_format}")
        console.print(f"[dim]Duration:[/dim] {'Auto' if duration is None else f'{duration}s'}")
        console.print(f"[dim]Prompt Influence:[/dim] {prompt_influence}")
    
    # Initialize Eleven Labs client
    try:
        elevenlabs_client = ElevenLabs(api_key=api_key)
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] Failed to initialize Eleven Labs client: {e}\n")
        sys.exit(1)
    
    # Generate the sound effect
    try:
        start_time = time.time()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold green]Generating sound effect..."),
            transient=True,
        ) as progress:
            progress.add_task("Generating", total=None)
            
            # Call the API
            result = elevenlabs_client.text_to_sound_effects.convert(
                text=text,
                output_format=output_format,
                duration_seconds=duration,
                prompt_influence=prompt_influence,
            )
            
            # Save the result
            with open(output_file, "wb") as f:
                for chunk in result:
                    f.write(chunk)
        
        # Calculate and display generation time
        generation_time = time.time() - start_time
        console.print(f"\n[bold green]Success![/bold green] Generated in {generation_time:.2f}s")
        console.print(f"[bold]Sound effect saved to:[/bold] {output_file}\n")
        
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {e}\n")
        sys.exit(1)


@app.command()
def version():
    """Show the version of the tool."""
    console.print("Eleven Labs Sound Effects CLI v1.0.0")


if __name__ == "__main__":
    app()
