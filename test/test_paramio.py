import numpy as np

from paramio.paramio import update_config


def test_update_config_1():
    config_file = {
        "env": "{env}",
        "s3_bucket": "{bucket}",
        "iterations": 1,
        "{variable_key}": 10,
        "numpy": np.array([1]),
        "runs": ["{run}_{env}", "{run}_{env}", "{run}_{env}"],
        "group": {"task": "{bucket}/{group}/{task}/{experiment}"},
    }

    res = update_config(
        config_file,
        env="dev",
        bucket="enterprise_dwh_global",
        group="extract",
        task="read_origins",
    )

    test_res = {
        "env": "dev",
        "s3_bucket": "enterprise_dwh_global",
        "iterations": 1,
        "{variable_key}": 10,
        "numpy": np.array([1]),
        "runs": ["{run}_dev", "{run}_dev", "{run}_dev"],
        "group": {"task": "enterprise_dwh_global/extract/read_origins/{experiment}"},
    }

    assert res == test_res
