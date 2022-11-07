import numpy as np

from paramio.paramio import Paramio


def test_init():
    project_parameters = Paramio(env="pro", folder="inference")
    assert project_parameters.parameters() == {"env": "pro", "folder": "inference"}


def test_init_order():
    project_parameters = Paramio(folder="inference", env="pro")
    assert project_parameters.parameters() == {"folder": "inference", "env": "pro"}


def test_parameterize():
    project_parameters = Paramio(
        env="dev", bucket="enterprise_dwh_global", group="extract", task="read_origins"
    )

    config_file = {
        "env": "{env}",
        "s3_bucket": "{bucket}",
        "iterations": 1,
        "{variable_key}": 10,
        "numpy": np.array([1]),
        "tuple_test": ("{env}", "{not_env}", "{env}"),
        "runs": ["{run}_{env}", "{run}_{env}", "{run}_{env}"],
        "group": {"task": "{bucket}/{group}/{task}/{experiment}"},
    }

    updated_config_file = project_parameters.parameterize(config_file)

    test_config_file = {
        "env": "dev",
        "s3_bucket": "enterprise_dwh_global",
        "iterations": 1,
        "{variable_key}": 10,
        "numpy": np.array([1]),
        "tuple_test": ("dev", "{not_env}", "dev"),
        "runs": ["{run}_dev", "{run}_dev", "{run}_dev"],
        "group": {"task": "enterprise_dwh_global/extract/read_origins/{experiment}"},
    }

    assert updated_config_file == test_config_file


def test_missing_parameters():
    project_parameters = Paramio(
        env="dev",
        bucket="enterprise_dwh_global",
        run="fast",
        group="extract",
        task="read_origins",
    )

    config_file = {
        "env": "{env}",
        "s3_bucket": "{bucket}",
        "iterations": 1,
        "{variable_key}": 10,
        "numpy": np.array([1]),
        "tuple_test": ("{env}", "{not_env}", "{env}"),
        "runs": ["{run}_{env}", "{run}_{env}", "{run}_{env}"],
        "group": {"task": "{bucket}/{group}/{task}/{experiment}"},
    }

    assert project_parameters.missing_parameters(config_file) == [
        "not_env",
        "experiment",
    ]


def test_parameters_1():
    project_parameters = Paramio(folder="inference", env="pro")
    assert project_parameters.parameters() == {"folder": "inference", "env": "pro"}


def test_parameters_2():
    project_parameters = Paramio(folder="inference", env="pro")
    assert project_parameters.parameters() == project_parameters.parameters()


def test_add():
    project_parameters = Paramio(folder="inference", env="pro")
    project_parameters.add(env="dev", weather="rainy")
    assert project_parameters.parameters() == {
        "folder": "inference",
        "env": "dev",
        "weather": "rainy",
    }


def test_delete():
    project_parameters = Paramio(folder="inference", env="pro")
    project_parameters2 = Paramio(folder="inference", env="pro")
    project_parameters3 = Paramio(folder="inference", env="pro")

    project_parameters.delete("env")
    project_parameters2.delete(["env"])
    project_parameters3.delete({"env": "dev"})

    assert (
        project_parameters.parameters()
        == project_parameters2.parameters()
        == project_parameters3.parameters()
    )


def test_empty_paramio():
    empty_parameters = Paramio()
    assert empty_parameters.parameters() == {}
