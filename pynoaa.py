import urllib.request
from urllib.parse import urljoin
import json
import inspect


class PyNOAA:
    def __init__(self, token, api_base = "https://www.ncdc.noaa.gov/cdo-web/api/v2/"):
        self._token = token
        self._api_base = api_base

    def _fetch_and_parse(self):
        p_frame = inspect.getouterframes( inspect.currentframe() )[1]
        path = inspect.getframeinfo(p_frame.frame).function
        args, _, _, values = inspect.getargvalues(p_frame.frame)
        query = []
        for arg in args:
            if arg in ["self",]:
                continue
            value = values.get(arg, None)
            if not value:
                continue
            if arg == "id":
                path = urljoin(path, value)
                continue
            if not (isinstance(value, list) or isinstance(value, set)):
                if not isinstance(value, str):
                    value = str(value)
                value = [value,]
            print("Working on %s = %s" % (arg, value))
            for occ in value:
                query.append(arg + "=" + occ)
        if len(query):
            path += "?" + "&".join(query)
        request = urllib.request.Request(urljoin(self._api_base, path), headers={"token": self._token})
        return json.loads(urllib.request.urlopen(request).read())

    def datasets(self,
        id = None,
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
        return self._fetch_and_parse()
