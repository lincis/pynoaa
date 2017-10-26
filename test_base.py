import pytest
from pynoaa import PyNOAA
from time import sleep

noaa = PyNOAA("KEQrNcMDIrZMyWtDslGKEkgETXbgIvjZ")
@pytest.mark.parametrize('startdate,locationid',(
    ['1994-05-20',None],
    [None,['FIPS:36','FIPS:37']],
))
def test_datasets(startdate, locationid):
    datasets = noaa.datasets(limit = 1, startdate = startdate, locationid = locationid)
    results = datasets["results"]
    assert datasets["metadata"]["resultset"]["limit"] == 1
    assert results[0]["id"] == "GHCND"
    sleep(0.3)

@pytest.mark.parametrize('fun,id',(
    ['datasets','NEXRAD2',],
    ['datacategories','ANNPRCP',],
    ['datatypes','ANN-DUTR-NORMAL',],
    ['locationcategories','CNTRY',],
    ['locations','CITY:AG000007',],
    ['stations','COOP:010148',],
))
def test_id(fun, id):
    results = getattr(noaa, fun)(id=id)
    assert results["id"] == id
    sleep(0.3)
