default_sanitizers = {
    "human_bool": lambda x: x.lower() in ["yes", "y", "si", "true"],
    "strip": lambda x: " ".join(x.strip().split())
}
