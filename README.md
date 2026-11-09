# ARPA Piemonte for Home Assistant

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![Validate](https://github.com/OWNER/ha-arpa-piemonte/actions/workflows/validate.yml/badge.svg)](https://github.com/OWNER/ha-arpa-piemonte/actions/workflows/validate.yml)
[![CI](https://github.com/OWNER/ha-arpa-piemonte/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/ha-arpa-piemonte/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Environmental data published by **ARPA Piemonte** (the Piedmont regional
environmental protection agency) as native Home Assistant entities: river
levels, air quality, pollen, groundwater, snow and more.

> **Status: pre-alpha.** The repository, validation pipeline and config flow
> exist; **no entities are exposed yet**. The first service (hydrometeorology)
> is the next milestone. Nothing here is stable.

This is an **unofficial** project. It is not affiliated with, endorsed by, or
sponsored by ARPA Piemonte or any other public body. Other Italian regions have
their own agencies and their own integrations; this one covers Piemonte only.

## Goals

Not another weather integration: a modular layer that collects, normalizes and
exposes heterogeneous environmental data while keeping the meaning and
provenance of the original measurements.

- **Multi-service**: each service (hydrometeorology, air quality, pollen, ...)
  has its own client, coordinator and update cycle. A failing source never
  takes down the others.
- **Semantic correctness**: units, device classes and statistics reflect what
  is actually measured. Missing is never turned into zero; forecasts are never
  turned into observations.
- **Provenance**: measurement time, acquisition time and validation status are
  kept apart.
- **Official sources first**: documented APIs and open datasets, no HTML
  scraping when a structured interface exists.
- **You choose** services and stations. Nothing is auto-created in bulk.

## Planned coverage

| Domain | Examples |
|---|---|
| Hydrometeorology | River levels, flow, temperature, rain, wind |
| Air quality | PM1, PM2.5, PM10, O3, NO2, SO2, CO |
| Weather forecast | Hourly / daily forecasts via the `weather` platform |
| Pollen | Concentrations per taxon |
| Groundwater, surface water | Levels, chemical and biological parameters |
| Snow | Depth, water equivalent |
| Other | Seismology, geology, radioactivity, EMF, noise |

Availability depends on what ARPA Piemonte publishes and under which license.

## Installation

Not released yet. Once the first release is out:

### HACS (custom repository)

1. HACS → ⋮ → **Custom repositories**
2. Add `https://github.com/OWNER/ha-arpa-piemonte` as type **Integration**
3. Download **ARPA Piemonte** and restart Home Assistant
4. **Settings → Devices & services → Add integration → ARPA Piemonte**

### Manual

Copy `custom_components/arpa_piemonte` into your Home Assistant
`custom_components` directory and restart.

Requires Home Assistant 2026.3.0 or newer.

## Data sources and attribution

Data belongs to ARPA Piemonte and is subject to its licenses and terms of use.
Each service documents its source, license and required attribution in
[`docs/`](docs/). The integration exposes the source on every entity.

## Development

```bash
# VS Code: "Reopen in Container", then
scripts/develop   # local Home Assistant on :8123 with the integration loaded
scripts/lint      # ruff format + check
pytest            # tests
```

Python 3.14+ is required (Home Assistant 2026.3+ requirement).

- Project brief and roadmap: [`docs/PROJECT_BRIEF.md`](docs/PROJECT_BRIEF.md)
- Design decisions: [`docs/DECISIONS.md`](docs/DECISIONS.md)
- Source inventory: [`docs/PIEMONTE_DATA_SOURCES.md`](docs/PIEMONTE_DATA_SOURCES.md)
- Work items: GitHub milestones and issues (phases F0 to F8)

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) for the software. Data licenses are those of the source.
