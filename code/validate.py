import csv
from itertools import filterfalse, tee
from typing import Dict, Generator, List, Tuple

import jsonschema

from schema import COLUMNS, FEATS_SCHEMA, FLOAT_COLUMNS, TARGET_SCHEMA


def partition(pred, iterable):
    "Use a predicate to partition entries into false entries and true entries"
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)


def validate_features(x):
    jsonschema.validate(x, FEATS_SCHEMA)


def is_valid_features(x):
    try:
        validate_features(x)
    except jsonschema.ValidationError:
        return False
    return True


def is_valid_target(x: Dict) -> bool:
    try:
        jsonschema.validate(x, TARGET_SCHEMA)
    except jsonschema.ValidationError:
        return False
    return True


def parse_csv(csvfile) -> Generator[Dict, None, None]:

    with open(csvfile) as f:
        reader = csv.reader(f)
        for line in reader:
            d = dict(zip(COLUMNS, line))
            for k in d:
                if k in FLOAT_COLUMNS:
                    d[k] = float(d[k])
            yield d


def parse_csv_and_validate(csvfile) -> Tuple[List[Dict], List[Dict]]:
    parsed = parse_csv(csvfile)
    invalid, valid = partition(is_valid_features, parsed)
    return list(valid), list(invalid)
