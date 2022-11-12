# -*- coding: utf-8 -*-
from paramio.get_parameters import get_parameters


def test_get_parameters():
    config_file = {
        "env": "{env}",
        "s3_bucket": "{bucket}",
        "iterations": 1,
        "{variable_key}": 10,
        "tuple_test": ("{env}", "{not_env}", "{env}"),
        "runs": ["{run}_{env}", "{run}_{env}", "{run}_{env}"],
        "group": {"task": "{bucket}/{group}/{task}/{experiment}"},
    }
    parameters = get_parameters(config_file)
    assert parameters == [
        "env",
        "bucket",
        "not_env",
        "run",
        "group",
        "task",
        "experiment",
    ]
