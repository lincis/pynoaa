import pytest
from pynoaa import PyNOAA

noaa = PyNOAA("KEQrNcMDIrZMyWtDslGKEkgETXbgIvjZ")
def test_datasets():
    datasets = noaa.datasets(limit=1)
    results = datasets["results"]
    assert datasets["metadata"]["resultset"]["limit"] == 1
    assert results[0]["id"] == "GHCND"
