# ARPA Piemonte for Home Assistant

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![CI](https://github.com/shhhrodingercat/ha-arpa-piemonte/actions/workflows/validate.yaml/badge.svg)](https://github.com/shhhrodingercat/ha-arpa-piemonte/actions/workflows/validate.yaml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Home Assistant custom integration for environmental data published by **ARPA Piemonte**.

> **Status: pre-alpha / project foundation.** The repository contains the initial
> integration skeleton and development checks. It does not yet collect data or
> create entities. API reconnaissance and data modelling come before the first
> working service.

This is an **unofficial** community project. It is not affiliated with, endorsed
by, or sponsored by ARPA Piemonte or any other public body. The scope is
Piemonte only.

## Project principles

- **Piemonte first.** This integration targets ARPA Piemonte. Possible future
  expansion is not part of the current scope.
- **Source-led development.** A service is implemented only after its source,
  API, semantics, update behaviour and terms of use have been investigated.
- **Semantic correctness.** Units and entity classes must reflect the actual
  measurement. Missing values are not zero; forecasts are not observations.
- **Provenance.** Preserve source, station, measurement time, retrieval time
  and quality/validation information whenever the source provides them.
- **Independent services.** A failure in one data service must not stop other
  independent services.
- **User choice.** Users should be able to select the services and stations
  they need. Avoid creating entities in bulk without a clear use.
- **No unnecessary dependencies.** Prefer Home Assistant's existing
  capabilities and standard Python libraries.

## Areas under investigation

These are research areas, **not a promise that every dataset is available or
will be implemented**.

| Area | Examples to investigate |
|---|---|
| Hydrometeorology | River levels, precipitation, temperature, wind and snow observations |
| Air quality | Particulate matter and gaseous pollutants |
| Pollen / aerobiology | Pollen and spore observations and bulletins |
| Weather forecasts | Forecast products suitable for Home Assistant's weather platform |
| Groundwater and surface water | Levels, sampling results and environmental status |
| Snow | Snow depth, snow water equivalent and bulletins |
| Other environmental data | Further ARPA Piemonte datasets, subject to source and use-case review |

See [the source inventory](docs/PIEMONTE_DATA_SOURCES.md) for the current
research status and [the project brief](docs/PROJECT_BRIEF.md) for scope.

## Installation

There is no usable release yet. The integration is not ready for installation
or everyday use.

When a release is available, it will be installable through HACS as a custom
repository, or manually by copying
`custom_components/arpa_piemonte` into the Home Assistant
`custom_components` directory.

## Development

Development tooling currently targets Python 3.13.

~~~bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\\Scripts\\activate
python -m pip install -r requirements_test.txt

ruff check .
ruff format --check .
pytest
~~~

GitHub Actions runs the official HACS repository validation and Home Assistant
Hassfest checks on pushes to main, pull requests and manual dispatches. Ruff
and pytest remain available as local development checks; they are not separate
jobs in the validation workflow.

See [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

## Project documents

- [Project brief and scope](docs/PROJECT_BRIEF.md)
- [Architecture and project decisions](docs/DECISIONS.md)
- [ARPA Piemonte source inventory](docs/PIEMONTE_DATA_SOURCES.md)

## License

The integration code is licensed under [MIT](LICENSE). Dataset licences,
attribution requirements and permitted uses must be assessed individually and
documented before each source is integrated.
