from paramio.paramio import update_config


def test_update_config_1():
    config_file = {
        "env": "{env}",
        "s3_bucket": "{bucket}",
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
        "group": {"task": "enterprise_dwh_global/extract/read_origins/{experiment}"},
    }

    assert res == test_res
