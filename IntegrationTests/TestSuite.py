from urllib.parse import urlencode
from urllib.request import Request, urlopen
import configparser
import pytest

@pytest.fixture()
def server_backend_prefix():
    print("Initalizing server prefix")
    config = configparser.ConfigParser()
    configFile = config.read('Config.ini')
    backendAddress=config['BackendAddress']['uri']
    backendport = config['BackendAddress']['port']
    url = "http://" + backendAddress + ":" + backendport  # Set destination URL here
    yield url
    print("teardown")


@pytest.fixture()
def resource1():
    print("setup1")
    config = configparser.ConfigParser()
    configFile = config.read('Config.ini')
    backendAddress=config['BackendAddress']['uri']
    backendport = config['BackendAddress']['port']
    url = "http://" + backendAddress + ":" + backendport  # Set destination URL here
    yield "xxxxx"
    print("teardown1")

def inc(x):
    return x + 1

def test_env():
    assert inc(3) == 4, "this is what i expect"

def test_env2():
    assert inc(3) == 5, "this is what i expect"

def test_env3():
    assert inc(3) == 4, "this is what i expect"

def test_env4():
    assert inc(3) == 4, "this is what i expect"

def test_env5():
    assert inc(3) == 4, "this is what i expect"

def test_alert_server_is_actually_alive(server_backend_prefix):
    url = server_backend_prefix +"/Alerts/health"  # Set destination URL here
    post_fields = {'foo': 'bar'}  # Set POST fields here
    request = Request(url, urlencode(post_fields).encode())
    requestResult = urlopen(request)
    assert requestResult.code == 200, "this is what i expect"
    json = requestResult.read().decode()
    print(json)

def test_audit_server_is_actually_alive(server_backend_prefix):
    url = server_backend_prefix +"/Audit/health"  # Set destination URL here
    post_fields = {'foo': 'bar'}  # Set POST fields here
    request = Request(url, urlencode(post_fields).encode())
    requestResult = urlopen(request)
    assert requestResult.code == 200, "this is what i expect"
    json = requestResult.read().decode()
    print(json)

