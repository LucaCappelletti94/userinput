default_sanitizers = {
    "human_bool": lambda x: x.lower() in ["yes", "y", "si", "true"],
    "integer": lambda x: int(x),
    "float": lambda x: float(x),
    "strip": lambda x: " ".join(x.strip().split())
}
