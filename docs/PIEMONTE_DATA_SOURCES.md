# ARPA Piemonte — source inventory

See [API_REFERENCE.md](API_REFERENCE.md) for the detailed endpoint, parameter and data-format notebook. This file remains the high-level inventory of candidate datasets.

This is a working research inventory, not a list of supported integration
features. Findings must be rechecked against the source before implementation.
Record access dates, response examples, field semantics, update frequency,
quality flags and licence/attribution terms as the investigation progresses.

## Hydrometeorology

**Status: initial API reconnaissance completed; endpoint semantics and coverage
still require systematic documentation.**

- Official landing page: [ARPA Piemonte Open Data](https://www.arpa.piemonte.it/dato/open-data).
- Public station table and map: [Meteo-idro real-time network](https://www.arpa.piemonte.it/rischi_naturali/snippets_arpa_graphs/tabella_stazioni/).
- Detailed endpoint reference: [API_REFERENCE.md](API_REFERENCE.md).
- Official OpenAPI document:
  [api_realtime OpenAPI](https://utility.arpa.piemonte.it/api_realtime/openapi.json)
- API base:
  [api_realtime](https://utility.arpa.piemonte.it/api_realtime)
- Endpoints identified:
  - GET /status — service health.
  - GET /pie_anag — station registry and filters.
  - GET /data_pie — station observations, with station and date filters,
    pagination.
  - GET /pie_neve — snow-related data.
  - GET /ggd — heating/cooling degree days.
- A registry query for San Sebastiano Po returned station code S4825.
  Station codes must be treated as strings; do not assume they are numeric.
- The /data_pie response can include air temperature, humidity, precipitation
  accumulations, wind, gusts, snow height and hydrometric level. Availability
  varies by station and values may be null.
- A sample response for S4825 contained hydrometric readings and null values
  for the other listed meteorological fields. This is a station-specific
  observation, not a general statement about the API.
- Hydrometric level is relative to the station's hydrometric zero; it must not
  be represented as absolute elevation.
- The registry exposes fields such as station coordinates, municipality,
  river, elevation and threshold-like values. The meaning and intended use of
  each threshold field must be verified before it is exposed or used in
  automation logic.

**Next research tasks**

- Document every endpoint's schema, pagination, date limits, error behaviour
  and response timestamps.
- Establish station and sensor/parameter coverage and the meaning of station
  types.
- Verify measurement units, quality/validation states and update cadence.
- Investigate /pie_neve and /ggd independently.
- Establish source terms, licence and attribution requirements.

## Air quality

**Status: official entry points and two ArcGIS services identified; full measurement workflow and schemas still require inspection.**

- Official ARPA entry point: [Qualità dell'aria - dati osservati](https://www.arpa.piemonte.it/temi/aria/qualita-dellaria-dati-osservati).
- Regional data portal: [Aria Ambiente](https://aria.ambiente.piemonte.it/qualita-aria/dati).
- Technical details and service URLs: [API_REFERENCE.md](API_REFERENCE.md).

- ARPA Piemonte publishes fixed monitoring-station information and air-quality
  observations.
- An ArcGIS REST service has been identified for station metadata, including
  coordinates and station classification.
- The portal presents pollutant information such as particulate matter,
  nitrogen dioxide and ozone. The exact structured endpoint, pollutant
  availability, units, validation and forecast semantics remain to be verified.

**Next research tasks**

- Identify the official measurement and forecast endpoints from the portal's
  network requests or service documentation.
- Inspect station, analyser and pollutant metadata.
- Establish hourly/daily data availability, history, units, validation and
  licence.

## Groundwater

**Status: geospatial datasets identified; time-series availability not yet
established.**

- An ArcGIS FeatureServer has been identified for groundwater monitoring and
  related point/body classifications.
- The presence of monitoring points or status classifications does not imply
  that a live water-level time series is publicly available.

**Next research tasks**

- Inspect layer schemas, identifiers, relationships and update dates.
- Determine whether measurements and historical series are exposed.
- Establish sampling frequency, units, quality metadata and reuse terms.

## Pollen and aerobiology

**Status: official publications identified; structured data access still to be
verified.**

- The published network information indicates five active stations.
- Bulletins cover botanical taxa and fungal spores, with weekly sampling and
  publication.
- The exact machine-readable source, taxonomy, units, sample dates and forecast
  method require investigation.

**Next research tasks**

- Find the structured source, if available, and inspect historical records.
- Document taxa, units, sampling period, publication time and station metadata.
- Distinguish measured counts from forecasts or interpretive bulletins.

## Weather forecasts

**Status: source discovery incomplete.**

- Portal products, bulletins and possible KML/XML resources have been noted.
- No suitable structured forecast API has yet been confirmed.

**Next research tasks**

- Identify public machine-readable forecast products and their terms.
- Establish spatial resolution, forecast horizon, temporal resolution,
  variables and update cadence.
- Use Home Assistant's weather platform only if the data supports its
  semantics; do not mix air-quality or pollen forecasts into a weather entity.

## Surface water

**Status: source discovery incomplete.**

- ARPA Piemonte water-monitoring portals and geospatial resources have been
  identified at a high level.
- Sampling datasets, historical series, schemas and API access are not yet
  documented.

**Next research tasks**

- Identify monitoring-point and sampling-result endpoints.
- Distinguish physical, chemical and biological measurements and their
  sampling frequencies.
- Establish units, classifications, validation and reuse terms.

## Other areas

Seismology, geology/landslide monitoring, radioactivity, radon,
electromagnetic fields, noise, soil and climate indicators remain exploratory.
For each, first establish whether ARPA Piemonte is the authoritative source,
whether structured public data exists, and whether it supports a meaningful
Home Assistant use case.

## Research record template

For each dataset, record:

- Provider and dataset name.
- Official landing page and API/service endpoint.
- Access method and authentication, if any.
- Station/point identifiers and metadata.
- Parameters, units and definitions.
- Observation/sample time, publication time and retrieval time.
- Update and sampling frequency; historical retention.
- Validation, quality flags, estimates and missing-value conventions.
- Spatial and temporal coverage.
- Licence, attribution and redistribution conditions.
- Example raw responses and known limitations.
- Proposed Home Assistant representation, with rationale.
