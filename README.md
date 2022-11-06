
<!-- README.md is generated from README.Rmd. Please edit that file -->
<!--<img src="man/figures/logo.png" align="right" height=140/> -->

# Paramio

<!-- badges: start -->

[![Tests](https://github.com/matbmeijer/paramio/actions/workflows/tests.yaml/badge.svg)](https://github.com/matbmeijer/paramio/actions/workflows/tests.yaml)
[![License:
MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<!-- badges: end -->

*Paramio* is a light-weight package with a simple goal for any kind of
projects:

> **Define project parameters only once**

## Installation

You can install **Paramio** directly from Github following these `pip`
commands:

``` bash
pip install git+https://github.com/matbmeijer/paramio.git
```

## Example:

**Paramio** searches and updates recursively dynamic parameters defined
with the `f-string` annotation, e.g. `{env}`. It allows to define
dynamic parameters only once, and is able to update `dict`, `list`,
`tuple` or simple `string` objects. Yet, if it finds other objects
within these kind of formats, it does not raise an error.

Equally, if parameters are defined, which cannot be found in the
**Paramio** parameters set when initialized, it does not raise an error.
This is especially useful if different parameters are defined in
different moments.

This is a basic example showing how to use **Paramio**, which also
depicts how - although `{experiment}` is not defined, it does not fail
nor raise an error:

``` python
from paramio import Paramio

#Set parameters once
project_parameters = Paramio(
  env="dev",
  bucket="enterprise_dwh_global",
  group="extract",
  task="read_origins"
)

# e.g. dictionary
config_file = {
        "env": "{env}",
        "s3_bucket": "{bucket}",
        "group": {"task": "{bucket}/{group}/{task}/{experiment}"},
    }

# notice how experiment, which is not defined in Paramio, stays the same
print(project_parameters.parameterize(config_file))
#> {'env': 'dev', 's3_bucket': 'enterprise_dwh_global', 'group': {'task': 'enterprise_dwh_global/extract/read_origins/{experiment}'}}
```

## Code of Conduct

Please note that the ‘Paramio’ project is released with a [Contributor
Code of
Conduct](https://github.com/matbmeijer/paramio/blob/master/CODE_OF_CONDUCT.md).
By contributing to this project, you agree to abide by its terms.

## License

[MIT © Matthias
Brenninkmeijer](https://github.com/matbmeijer/paramio/blob/master/LICENSE)
