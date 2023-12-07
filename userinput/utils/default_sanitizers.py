"""Default sanitizers for userinput."""

default_sanitizers = {
    "human_bool": lambda x: x.lower() in ["yes", "ye", "y", "si", "true"],
    "integer": int,
    "float": float,
    "strip": lambda x: " ".join(x.strip().split()),
}
