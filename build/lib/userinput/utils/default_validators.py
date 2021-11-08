from validate_email import validate_email
from validate_version_code import validate_version_code
from .set_validator import set_validator
from validators import url
import socket
from IPy import IP


def hostname(server: str) -> bool:
    try:
        socket.gethostbyname(server)
        return True
    except socket.gaierror:
        return False


def validate_ip(address: str) -> bool:
    if address is None or not IP(address):
        return False
    try:
        socket.gethostbyaddr(address)
        return True
    except socket.error:
        return False


default_validators = {
    "email": lambda x: isinstance(x, str) and validate_email(x),
    "version_code": validate_version_code,
    "human_bool": set_validator(["yes", "y", "true", "si", "no", "n", "false"]),
    "url": url,
    "integer": lambda x: str(x).isdigit(),
    "positive_integer": lambda x: str(x).isdigit() and int(x) >= 0,
    "non_empty": lambda x: isinstance(x, str) and len(x) > 0,
    "hostname": hostname,
    "ip": validate_ip
}
