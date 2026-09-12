"""
Earthquakes occured in Greece during the last 24 hours.
Data are being retrieved from the Seismological Laboratory
of the University of Athens.
"""

import json
import warnings

# pylint: disable=import-error
import requests
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore")


def latest_event() -> json:
    """Returns the latest earthquake event."""

    res = requests.get("http://www.geophysics.geol.uoa.gr/stations/maps/seismicity.xml")

    if res.ok:
        soup = BeautifulSoup(res.content, "lxml").find("item")

        results = [x.strip() for x in soup.description.text.split("<br>")]

        if len(results) > 0:
            location = results[0]
            time = str(results[1]).split(":", maxsplit=1)[1].strip()
            lat = str(results[2]).split(":", maxsplit=1)[1].strip()
            lon = str(results[3]).split(":", maxsplit=1)[1].strip()
            depth = str(results[4]).split(":", maxsplit=1)[1].strip()
            magnitude = str(results[5]).strip()

            event = {
                "Location": location,
                "Time": time,
                "Latitude": lat,
                "Longtitude": lon,
                "Depth": depth,
                "Magnitude": magnitude,
            }

            return json.dumps(event, indent=4)
        return "No events found..."


if __name__ == "__main__":
    print(latest_event())
