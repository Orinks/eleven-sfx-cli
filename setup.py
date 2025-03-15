from setuptools import setup

setup(
    name="eleven-sfx-cli",
    version="1.0.0",
    py_modules=["eleven_sfx_cli"],
    install_requires=[
        "elevenlabs",
        "python-dotenv",
        "typer",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "eleven-sfx=eleven_sfx_cli:app",
        ],
    },
)
