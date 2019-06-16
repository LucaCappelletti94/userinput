from validate_email import validate_email
from validate_version_code import validate_version_code
from validators import url

default_validators = {
    "email":validate_email,
    "version_code":validate_version_code,
    "url":url
}