from validate_email import validate_email
from validate_version_code import validate_version_code
from .set_validator import set_validator
from validators import url
import socket
from IPy import IP

def hostname(server: str)->bool:
    try:
        socket.gethostbyname(server)
        return True
    except socket.gaierror:
        return False

def ip(address: str)->bool:
    if address is None or not IP(address):
        return False
    try:
        socket.inet_aton(address)
        return True
    except socket.error:
        return False

default_validators = {
    "email":validate_email,
    "version_code":validate_version_code,
    "human_bool": set_validator(["yes", "y", "true", "no", "n", "false"]),
    "url":url,
    "integer":lambda x: str(x).isdigit(),
    "positive_integer":lambda x: str(x).isdigit() and int(x)>=0,
    "non_empty":lambda x: isinstance(x, str) and len(x)>0,
    "hostname":hostname,
    "ip":ip
}