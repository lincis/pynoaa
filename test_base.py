import pytest
from pynoaa import PyNOAA

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
