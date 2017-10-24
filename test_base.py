import pytest
from pynoaa import PyNOAA

noaa = PyNOAA("KEQrNcMDIrZMyWtDslGKEkgETXbgIvjZ")
@pytest.mark.parametrize('dummy',1:6)
def test_datasets(dummy):
    datasets = noaa.datasets(limit=1)
    results = datasets["results"]
    assert datasets["metadata"]["resultset"]["limit"] == 1
    assert results[0]["id"] == "GHCND"
