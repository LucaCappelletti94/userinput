"""Submodule with default validators for userinput package."""
from validate_email import validate_email
from validate_version_code import validate_version_code
from validators import url
import socket
from IPy import IP
from .set_validator import set_validator


def hostname(server: str) -> bool:
    """Return whether the given server is a valid hostname.

    Parameters
    -----------------------
    server: str,
        Server to validate.
    """
    try:
        socket.gethostbyname(server)
        return True
    except socket.gaierror:
        return False


def validate_ip(address: str) -> bool:
    """Return whether the given address is a valid IP."""
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
    "human_bool": set_validator(
        ["yes", "ye", "y", "true", "si", "no", "n", "false"],
        normalize_to_lowercase=True,
    ),
    "url": url,
    "integer": lambda x: str(x).isdigit(),
    "positive_integer": lambda x: str(x).isdigit() and int(x) >= 0,
    "non_empty": lambda x: isinstance(x, str) and len(x) > 0,
    "hostname": hostname,
    "ip": validate_ip,
}
