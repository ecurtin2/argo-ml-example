from json import loads
from pathlib import Path

FEATS_JSON = Path(__file__).with_name("feats_schema.json").read_text()
FEATS_SCHEMA = loads(FEATS_JSON)
TARGET_JSON = Path(__file__).with_name("target_schema.json").read_text()
TARGET_SCHEMA = loads(TARGET_JSON)
FEAT_COLUMNS = list(FEATS_SCHEMA["properties"])
TARGET_COLUMNS = list(TARGET_SCHEMA["properties"])
COLUMNS = FEAT_COLUMNS + TARGET_COLUMNS
FLOAT_COLUMNS = [
    k for k, v in FEATS_SCHEMA["properties"].items() if v["type"] == "number"
]
