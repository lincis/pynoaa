import urllib.request
from urllib.parse import urljoin
import json
import inspect


class PyNOAA:
    def __init__(self, token, api_base = "https://www.ncdc.noaa.gov/cdo-web/api/v2/"):
        self._token = token
        self._api_base = api_base

    def _fetch_and_parse(self, path):
        p_frame = inspect.getouterframes( inspect.currentframe() )[1]
        args, _, _, values = inspect.getargvalues(p_frame)
        if id:
            path = urljoin(path, id)
        request = urllib.request.Request(urljoin(self._api_base, path), headers={"token": self._token})
        return json.loads(urlib.request.urlopen(request).read())

    def datasets(self,
        id = None
        datatypeid = None,
        locationid = None,
        stationid = None,
        startdate = None,
        enddate = None,
        sortfield = None,
        sortorder = None,
        limit = None,
        offset = None
    ):
        return self._fetch_and_parse("datasets")

# datasets_request = urllib.request.Request("https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets", headers={"token" : "KEQrNcMDIrZMyWtDslGKEkgETXbgIvjZ"})
# datasets = json.loads(urllib.request.urlopen(datasets_request).read())
# print("Datasets: %s" % json.dumps(datasets, indent=4, sort_keys=True))
locations_request = urllib.request.Request("https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/FIPS:LG", headers={"token" : "KEQrNcMDIrZMyWtDslGKEkgETXbgIvjZ"})
locations = json.loads(urllib.request.urlopen(locations_request).read())
print("Locations: %s" % json.dumps(locations, indent=4, sort_keys=True))

stations_request = urllib.request.Request("https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:LG", headers={"token" : "KEQrNcMDIrZMyWtDslGKEkgETXbgIvjZ"})
stations = json.loads(urllib.request.urlopen(stations_request).read())
print("Stations: %s" % json.dumps(stations, indent=4, sort_keys=True))
