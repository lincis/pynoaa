try:
    from urllib.parse import urljoin
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urljoin
    from urllib2 import urlopen, Request, HTTPError

import json
import inspect
import logging

logging.basicConfig(
    filename = 'pynoaa.log',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
)

class PyNOAA:
    def __init__(self, token, api_base = "https://www.ncdc.noaa.gov/cdo-web/api/v2/"):
        self._token = token
        self._api_base = api_base
        logging.info('PyNOAA(%s) initialized' % self._token)

    def _fetch_and_parse(self):
        p_frame = inspect.currentframe().f_back
        path = inspect.getframeinfo(p_frame).function
        _, _, _, p_locals = inspect.getargvalues(p_frame)
        logging.info("%s(%s)" % (path, p_locals))
        values = p_locals.copy()
        values.update(p_locals.get("kwargs",{}))
        logging.debug("values = %s" % values)
        query = []
        for var, value in values.items():
            if var in ["self","kwargs"]:
                continue
            if not value:
                continue
            if var == "id":
                path = urljoin(path, value)
                continue
            if not (isinstance(value, list) or isinstance(value, set)):
                if not isinstance(value, str):
                    value = str(value)
                value = [value,]
            logging.debug("Working on %s = %s" % (var, value))
            for occ in value:
                query.append(var + "=" + occ)
        if len(query):
            path += "?" + "&".join(query)
        logging.debug("Create request to: %s" % urljoin(self._api_base, path))
        request = Request(urljoin(self._api_base, path), headers={"token": self._token})
        raw_data = urlopen(request).read()
        logging.debug("Got response: %s" % raw_data)
        return json.loads(raw_data)

    def datasets(self,
        id = None,
        datatypeid = None,
        locationid = None,
        stationid = None,
        **kwargs
    ):
        return self._fetch_and_parse()

    def datacategories(self,
        id = None,
        datasetid = None,
        locationid = None,
        stationid = None,
        **kwargs
    ):
        return self._fetch_and_parse()
