
<!-- README.md is generated from README.Rmd. Please edit that file -->
<!--<img src="man/figures/logo.png" align="right" height=140/> -->

# Paramio

<!-- badges: start -->

[![Tests](https://github.com/matbmeijer/paramio/actions/workflows/tests.yaml/badge.svg)](https://github.com/matbmeijer/paramio/actions/workflows/tests.yaml)
[![License:
MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<!-- badges: end -->

*Paramio* is a light-weight package with a simple objective:

> **Define project parameters only once**

Workflows/jobs depend multiple times upon parameter/config files, which
have a dynamic component. For example, paths might vary depending on the
environment the job is executed (e.g. `dev` vs `pro`). Equally, complex
jobs have multiple times a variety of parameter files, dictionaries and
simple Python elements, which need to be updated in each execution.
*Paramio* focuses on finding an easy solution for this problem.

It allows to: 1. Centralize the definition of dynamic parameters in a
single object 2. Update dynamic parameters defined in the f-string
format `{}` recursively 3. Support for any kind of common Python object
(`dict`, `list`, `tuple` & `str`) 4. Ignores other objects, which cannot
be updated (e.g. numpy array) 5. Contrary to f-string annotation, it
does not raise a `KeyError` if a dynamic parameter is not defined. This
is especially useful if some dynamic parameters need to be defined at
different moments of the execution (for example if they depend on the
run task results).

## Installation

You can install **Paramio** directly from Github following this `pip`
command:

``` bash
pip install git+https://github.com/matbmeijer/paramio.git
```

## Examples:

This is a basic example showing how to use **Paramio**. It also depicts
how *Paramio* does not throw a KeyError if a parameter is not defined -
in this case the parameter `{experiment}` is not defined, yet it does
not fail:

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

# Parameterize parameter dictionary
updated_config_file = project_parameters.parameterize(config_file)

# notice how experiment, which is not defined in Paramio, stays the same
updated_config_file
#> {'env': 'dev', 's3_bucket': 'enterprise_dwh_global', 'group': {'task': 'enterprise_dwh_global/extract/read_origins/{experiment}'}}
```

Yet now if we add the `experiment` parameter it will be updated:

``` python
#Add parameter for experiment
project_parameters.add(experiment="1234")

# Parameterize parameter dictionary
updated_config_file_v2 = project_parameters.parameterize(config_file)

# notice how now experiment is defined
updated_config_file_v2
#> {'env': 'dev', 's3_bucket': 'enterprise_dwh_global', 'group': {'task': 'enterprise_dwh_global/extract/read_origins/1234'}}
```

## Code of Conduct

Please note that the ‘Paramio’ project is released with a [Contributor
Code of
Conduct](https://github.com/matbmeijer/paramio/blob/master/CODE_OF_CONDUCT.md).
By contributing to this project, you agree to abide by its terms.

## License

[MIT © Matthias
Brenninkmeijer](https://github.com/matbmeijer/paramio/blob/master/LICENSE)
