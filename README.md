# Greece Earthquake Alert

A small command-line utility that retrieves the latest earthquake listed in the Seismological Laboratory of the University of Athens feed and prints its details as formatted JSON.

The script is designed for a quick terminal check. It does not run continuously, send notifications, or provide a web dashboard.


## How it works

1. Fetches the live XML feed from the University of Athens.
2. Parses the first `<item>` with BeautifulSoup and `lxml`.
3. Extracts the location, time, coordinates, depth, and magnitude.
4. Prints the event as JSON.

The first event returned by the feed is treated as the latest event. The script does not keep a history or apply magnitude or location filters.

Data source: [University of Athens seismicity feed](http://www.geophysics.geol.uoa.gr/stations/maps/seismicity.xml)

## Requirements

- Python 3.12+
- Internet access
- `uv` (recommended) or `pip`

## Installation

### Using `uv` (recommended)

```bash
uv sync
```

### Using `pip`

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install requests beautifulsoup4 lxml
```

## Usage

Run the script from the project directory with `uv`:

```bash
uv run python main.py
```

Or, with an activated virtual environment:

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

The values will change as the feed is updated. Internet access is required when the script runs.

## Project files

- `main.py` — fetches and parses the earthquake XML feed
- `pyproject.toml` — project metadata and Python dependencies
- `README.md` — project documentation

## Notes

- The data source is an external university feed and may be unavailable or change format without notice.
- This project is a lightweight example for checking recent seismic activity in Greece.
- This project is not intended for commercial use.
