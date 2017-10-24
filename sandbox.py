from pynoaa import PyNOAA

noaa = PyNOAA("KEQrNcMDIrZMyWtDslGKEkgETXbgIvjZ")
print(noaa.datasets(enddate = ["1954-05-20"]))

# datasets_request = urllib.request.Request("https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets", headers={"token" : "KEQrNcMDIrZMyWtDslGKEkgETXbgIvjZ"})
# datasets = json.loads(urllib.request.urlopen(datasets_request).read())
# print("Datasets: %s" % json.dumps(datasets, indent=4, sort_keys=True))
# locations_request = urllib.request.Request("https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/FIPS:LG", headers={"token" : "KEQrNcMDIrZMyWtDslGKEkgETXbgIvjZ"})
# locations = json.loads(urllib.request.urlopen(locations_request).read())
# print("Locations: %s" % json.dumps(locations, indent=4, sort_keys=True))
#
# stations_request = urllib.request.Request("https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:LG", headers={"token" : "KEQrNcMDIrZMyWtDslGKEkgETXbgIvjZ"})
# stations = json.loads(urllib.request.urlopen(stations_request).read())
# print("Stations: %s" % json.dumps(stations, indent=4, sort_keys=True))
