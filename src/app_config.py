import json
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def get_password() -> str:
    config_path = Path(__file__).resolve().parent.parent / "config.json"
    with config_path.open(encoding="utf-8") as f:
        data = json.load(f)
    return str(data["password"])
