# Greece Earthquake Alert

A small Python utility that checks the live seismic feed from the Seismological Laboratory of the University of Athens and prints the most recent earthquake information in the terminal.

## Overview

This project fetches the XML feed from:

- http://www.geophysics.geol.uoa.gr/stations/maps/seismicity.xml

It then parses the first item in the feed and prints the event details. The script is intentionally minimal and designed for quick checks rather than a full dashboard or alert system.

## What it does

- fetches live earthquake data from the University of Athens feed
- parses the XML with BeautifulSoup
- extracts the latest event information
- prints the result to the terminal

## Requirements

- Python 3.12+
- Internet access
- `uv` (recommended) or `pip`

## Installation

With `uv`:

```bash
uv sync
```

With `pip`:

```bash
pip install requests beautifulsoup4 lxml
```

## Usage

Run the script from the project folder:

```bash
uv run .\main.py
```

Or:

```bash
python main.py
```

## Example output

```text
{
    "Location": "12.0 km NE of Patras",
    "Time": "12-Sep-2026 12:04:44 (UTC)",
    "Latitude": "38.33N",
    "Longtitude": "21.82E",
    "Depth": "2km",
    "Magnitude": "M 0.9"
}
```

The exact values will vary depending on the current feed data.

## Project files

- `main.py` — fetches and parses the earthquake XML feed
- `pyproject.toml` — project metadata and Python dependencies
- `README.md` — project documentation

## Notes

- The data source is an external university feed and may change without notice.
- This project is a lightweight example for checking recent seismic activity in Greece.
- This project is not intended for commercial use.
