# Greece Earthquake Alert

A small command-line utility that fetches the latest earthquake listed in the Seismological Laboratory of the University of Athens feed and prints its details as formatted JSON.

The script performs one request each time it runs. It does not poll continuously, send notifications, store event history, or provide a web dashboard.

## Requirements

- Python 3.12 or newer
- Internet access when the script runs
- [`uv`](https://docs.astral.sh/uv/) or `pip`

## Setup

Using `uv`:

```bash
uv sync
```

Using `pip` in a virtual environment:

```bash
python -m venv .venv
```

Activate the environment in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then install the dependencies:

```bash
pip install -e .
```

## Usage

Run the command from the project directory:

```bash
uv run python main.py
```

With an activated virtual environment, use:

```bash
python main.py
```

The first `<item>` returned by the feed is treated as the latest event. A successful response includes the location, UTC time, latitude, longitude, depth, and magnitude:

```json
{
    "Location": "12.0 km NE of Patras",
    "Time": "12-Sep-2026 12:04:44 (UTC)",
    "Latitude": "38.33N",
    "Longtitude": "21.82E",
    "Depth": "2km",
    "Magnitude": "M 0.9"
}
```

The values change as the feed is updated. If no event is available, the script reports that no events were found; if the feed cannot be reached, it reports the response reason.

## Data source

[University of Athens seismicity feed](http://www.geophysics.geol.uoa.gr/stations/maps/seismicity.xml)

The external feed may be unavailable or change format without notice.
This project is intended for personal and educational use and is not intended for commercial use.

## Project files

- `main.py` - fetches and parses the earthquake XML feed
- `pyproject.toml` - project metadata and dependencies
- `README.md` - project documentation
