
<!-- README.md is generated from README.Rmd. Please edit that file -->
<!--<img src="man/figures/logo.png" align="right" height=140/> -->

# 🎛️ Paramio

<!-- badges: start -->

[![Tests](https://github.com/matbmeijer/paramio/actions/workflows/tests.yaml/badge.svg)](https://github.com/matbmeijer/paramio/actions/workflows/tests.yaml)
[![License:
MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<!-- badges: end -->

**Paramio** is a light-weight package with a simple objective:

> **Define project parameters only once**

It is common for batch execution task workflows to depend on
parameters/config files with dynamic characteristics. For example, input
and output paths might vary depending on the environment the job is
executed (e.g. `dev` vs `pred` vs `prod`). Additionally, complex task
workflows contain multiple times a variety of parameter files,
dictionaries, and simple Python elements, whose parameters need to be
updated dynamically. **Paramio’s** objective is to offer a simple
solution when dealing with these habitual circumstances in workflow
projects.

## Features

1.  **Centralize** the **definition** of **dynamic parameters** in a
    single object.
2.  **Recursively update** dynamic parameters defined in the `f-string`
    format `"{__dynamic__parameter__}"` recursively.
3.  Support for **any** kind of common **Python object** (`dict`,
    `list`, `tuple` & `str`).
4.  Ignores other objects, which cannot be updated (e.g. `numpy`
    arrays).
5.  Contrary to `f-string` annotation, it does not raise a `KeyError` if
    a dynamic parameter is not defined. This is especially useful if
    some dynamic parameters need to be defined at different moments of
    the execution (for example if they depend on the run task results).
6.  Paramio is a lightweight **no-dependencies** library intended to
    keep projects’ dependencies lean.

## Installation

You can install **Paramio** directly from Github following this `pip`
command:

``` bash
pip install git+https://github.com/matbmeijer/paramio.git
```

## Example

#### Example parameter file

Let’s see a basic example showing how to use **Paramio**. Imagine having
a `parameters.yaml` file with all the project parameters as the
following. The file could be in any common config file format
(e.g. yaml, toml, json, etc.), the objective is to exemplify a realistic
use case. An important aspect here is that the **dynamic variables** are
defined with `f-string` formatting syntax:

``` yaml
project_parameters:
  env: "{env}"
  s3_bucket: "{bucket}"
  group:
    task:
      path: "{bucket}/{group}/{task}/{experiment}.snappy.parquet"
```

So evaluating the `parameters.yaml` file we have the dynamic variables:

- `"{env}"`
- `"{bucket}"`
- `"{group}"`
- `"{task}"`
- `"{experiment}"`

#### Load parameter file

We load now the `parameters.yaml` file with the usual PyYAML library to
have the parameters available as a Python dictionary (`dict`). Again,
the file format does not matter, it’s only to depict a common process
loading project parameter files:

``` python
# Dependencies to load yaml file from project package
import yaml
import pkg_resources

# Imaginary loading method
resource_dir = pkg_resources.resource_filename("resources", "data_preparation")
yaml_parameters_path = f"{resource_dir}/parameters.yaml"
with open(yaml_parameters_path) as stream:
  parameters_file = yaml.safe_load(stream)
```

Having loaded the yaml file as dictionary, let’s look at it’s structure:

``` python
print(parameters_file)
#> {'env': '{env}', 's3_bucket': '{bucket}', 'group': {'task': '{bucket}/{group}/{task}/{experiment}.snappy.parquet'}}
```

#### Apply **Paramio**

Now it’s time to apply **Paramio**, which will update all the parameters
in the `parameters_file` object recursively. Notice how the variable
`{experiment}` is not set, yet - contrary to `f-string` annotation -
**Paramio** does not throw a `KeyError` when applying the
`Paramio().parameterize()` method:

``` python
from paramio import Paramio

# Set parameters once
project_parameters = Paramio(
  env="dev",
  bucket="enterprise_dwh_global",
  group="extract",
  task="read_origins"
)

# Parameterize the parameters dictionary
updated_parameters_file = project_parameters.parameterize(parameters_file)

# Notice how experiment, which is not defined in Paramio, stays the same
updated_parameters_file
#> {'env': 'dev', 's3_bucket': 'enterprise_dwh_global', 'group': {'task': 'enterprise_dwh_global/extract/read_origins/{experiment}.snappy.parquet'}}
```

#### Update **Paramio** paramaters

Imagine the `{experiment}` parameter depends on execution runtime
results, and is added along the process. New parameters can be added (or
deleted) later. Let’s showcase how to add the `experiment` parameter,
and notice how the new parameter dictionary `parameters_file_v2`
changes:

``` python
#Add parameter for experiment
project_parameters.add(experiment="1234")

# Parameterize parameter dictionary
parameters_file_v2 = project_parameters.parameterize(parameters_file)

# notice how now experiment is defined
parameters_file_v2
#> {'env': 'dev', 's3_bucket': 'enterprise_dwh_global', 'group': {'task': 'enterprise_dwh_global/extract/read_origins/1234.snappy.parquet'}}
```

## Code of Conduct

Please note that the Paramio project is released with a [Contributor
Code of
Conduct](https://github.com/matbmeijer/paramio/blob/main/CODE_OF_CONDUCT.md).
By contributing to this project, you agree to abide by its terms.

## License

[MIT © Matthias
Brenninkmeijer](https://github.com/matbmeijer/paramio/blob/main/LICENSE)
