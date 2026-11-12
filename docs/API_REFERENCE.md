# ARPA Piemonte — API and data-source technical reference

This is the working technical notebook for source/API reconnaissance. It records
what has actually been identified, what is documented by the provider, and what
has merely been observed in a sample. Update it whenever a new endpoint,
response field, data product, limitation or licence condition is verified.

**Last reviewed:** 2026-11-11  
**Scope:** public ARPA Piemonte environmental data relevant to Home Assistant.  
**Status:** preliminary; not an implementation contract.

## 1. Official starting points

| Resource | Purpose | Access |
|---|---|---|
| [ARPA Piemonte Open Data](https://www.arpa.piemonte.it/dato/open-data) | Main landing page for machine-readable environmental datasets | Public web page |
| [Meteo-idro real-time station table](https://www.arpa.piemonte.it/rischi_naturali/snippets_arpa_graphs/tabella_stazioni/) | Public entry point for the automatic weather/hydrological network, station map and API documentation | Public web page |
| [Realtime API OpenAPI](https://utility.arpa.piemonte.it/api_realtime/openapi.json) | OpenAPI 3.1 specification for the realtime API | JSON |
| [Realtime API Swagger UI](https://utility.arpa.piemonte.it/api_realtime/docs) | Interactive API documentation | Web UI |
| [Historical database API documentation](https://utility.arpa.piemonte.it/docs/) | Meteoweb REST API documentation linked by the Open Data page | Web UI |
| [Air-quality observed data](https://www.arpa.piemonte.it/temi/aria/qualita-dellaria-dati-osservati) | Observations, maps, SRRQA download and links to Aria Piemonte | Public web page |
| [Aria Ambiente](https://aria.ambiente.piemonte.it/qualita-aria/dati) | Regional air-quality data consultation/download | Regional portal |

ARPA's Open Data page says the automatic hydrometeorological network provides
recent data for the last six days. It separately describes the historical
database as daily and monthly meteorological/hydrological/snow data from the
start of each sensor's operation. These are distinct products and must not be
treated as one endpoint or one retention policy.

## 2. Realtime hydrometeorological API

### 2.1 Service

- Base URL: https://utility.arpa.piemonte.it/api_realtime
- OpenAPI: https://utility.arpa.piemonte.it/api_realtime/openapi.json
- OpenAPI version: 3.1.0
- API info version: 1.1
- Authentication: no authentication parameter is described in the published
  OpenAPI document.
- Server entries: relative /api_realtime and absolute base URL.
- Error schema: ProblemDetail with type, title, status, detail, optional
  instance.
- Important documentation limitation: the published OpenAPI defines request
  parameters and status/error schemas, but the successful data endpoints have
  untyped/empty response schemas. The actual payload shape therefore needs to
  be captured and documented from live responses.

### 2.2 Endpoints

#### GET /status

Health check.

Documented success response:
- status: string
- version: string

Use: diagnostic/availability check. It is not a substitute for validating
individual data responses.

#### GET /pie_anag

Station registry.

Optional query parameters:

| Parameter | Type | Meaning in OpenAPI |
|---|---|---|
| station_code | string | Station code |
| name | string | Station name |
| station_type | string | Station type |
| municipality_code | string | Municipality code |
| municipality | string | Municipality |
| basin | string | Basin |
| codice_istat_comune | string | Part 1 of extended station ID |
| progr_punto_com | integer | Part 2 of extended station ID |

Use: discover stations and their metadata. The precise response fields, coordinate
reference, code semantics, sensor/parameter relationships and threshold fields
still need to be verified against a captured response and provider metadata.

#### GET /data_pie

Weather-station observations. The OpenAPI summary describes data from the last
three days, while the Open Data landing page describes the public automatic
network dataset as covering the last six days. Treat these as a documentation
discrepancy until tested; do not assume either is a guaranteed retention limit.

Optional query parameters:

| Parameter | Type | Meaning |
|---|---|---|
| station_code | string | Filter by station code |
| date_from | string | Start date/time, described as Y-m-dTH:M |
| date_to | string | End date/time, described as Y-m-dTH:M |
| page | integer, minimum 1 | Page number; default 1 |
| page_size | integer, maximum 10000 | Page size; default 100 |

Observed/identified parameter names in sample records include:
- air_temperature
- humidity
- cum_rain_1h, cum_rain_3h, cum_rain_6h,
  cum_rain_12h, cum_rain_24h
- wind speed/direction and gust speed/direction fields
- snow_height
- hydrometric_level

This is a preliminary field inventory, not a guarantee that every station
reports every parameter. Null values have been observed and must remain null;
they must never be converted to zero.

Queries for station S4825 (San Sebastiano Po) returned records with
hydrometric data while several meteorological values were null. In a sample
covering 2026-11-06 through 2026-11-09 00:00, the API returned 73 hourly rows.
A separate query for 2026-11-09 00:00 through 14:00 returned 15 rows, including
the 14:00 observation. In both samples, hydrometric_level was populated and
the other listed measurement fields were null. These are station/sample
observations only; they do not establish general parameter availability,
retention or network-wide cadence. The 14:00 result is from a historical
date-range query and does not, by itself, establish current publication
latency or that the API is near-real-time.

**Semantic caution:** hydrometric level is measured relative to the station's
hydrometric zero. It is not absolute elevation above sea level.

#### GET /pie_neve

Validated snow-height data for snow stations.

Optional query parameters:

| Parameter | Type | Meaning |
|---|---|---|
| station_code | string | Filter by station |
| date_from | string | Start date/time, described as Y-m-dTH:M |
| date_to | string | End date/time, described as Y-m-dTH:M |

No pagination parameters are listed in the OpenAPI document. Payload fields,
units, time semantics, validation metadata, station coverage and retention
remain to be inspected.

#### GET /ggd

Heating and cooling degree-day data.

Optional query parameters:

| Parameter | Type | Meaning |
|---|---|---|
| station_code | string | Filter by station |
| date_from | string | Start date/time, described as Y-m-dTH:M |
| date_to | string | End date/time, described as Y-m-dTH:M |
| page | integer, minimum 1 | Page number; default 1 |
| page_size | integer, maximum 10000 | Page size; default 100 |

Payload structure, degree-day definitions, units, station association,
aggregation period and retention remain to be inspected.

### 2.3 Known station example

- Station name: San Sebastiano Po
- Station code: S4825
- The code is a string and must be stored as such.
- Do not confuse it with other administrative/progressive identifiers.
- Coordinates and all station metadata should be taken from the current registry,
  not hardcoded in the integration.

### 2.4 Open questions for this API

- Capture representative raw responses for all five endpoints.
- Establish exact timestamp field names, timezone and whether timestamps denote
  observation time, aggregation end or publication time.
- Verify measurement units and precision for every parameter.
- Verify pagination behaviour, page termination and maximum page size.
- Resolve the three-day (OpenAPI) versus six-day (Open Data page) discrepancy.
- Establish whether date filters can retrieve data beyond the advertised recent
  window (useful for source characterization, not for integration backfill).
- Verify response ordering and publication latency; determine the narrowest
  reliable query window for obtaining only the latest observation. The
  2026-11-09 00:00–14:00 sample was gap-free at hourly intervals, but was a
  historical query and does not establish live freshness.
- Decode station type, sensor availability and threshold fields.
- Determine null/missing-value conventions and any quality flags.
- Inspect snow and degree-day payloads.
- Check API terms, licence and attribution requirements.

### 2.5 Integration consumption model — latest observations, not history

**Project requirement (confirmed 2026-11-09):** the integration is interested in
the latest available observation ("current or near-current" data), not in
historical retrieval or backfill. Home Assistant's Recorder is responsible for
retaining entity state history and providing history/statistics.

Consequences for the integration design:

- Poll each source at a cadence appropriate to its actual publication/update
  frequency; do not poll more often than useful or imply that polling makes
  source data real-time.
- Expose the newest validly timestamped observation available for each
  station/parameter. Keep the source observation timestamp distinct from the
  local retrieval/update time.
- Do not download multi-day history for Recorder, implement historical
  backfill, or maintain a parallel historical database.
- For endpoints that only accept date ranges, request a narrow recent window
  sufficient to find the newest published record (with a small overlap where
  needed to tolerate publication delays). The exact window and refresh cadence
  must be based on observed provider behaviour, not guessed.
- Handle delayed, repeated, missing and out-of-order observations without
  replacing a newer value with an older one. A null measurement is unavailable,
  not zero; retain the last known state only according to an explicit stale-data
  policy, and expose data age/availability where useful.
- Pagination should not be used to retrieve old pages when only the latest
  observation is needed. Verify whether the first page is newest-first or
  oldest-first before relying on it; if ordering is not guaranteed, inspect
  enough of the response to select the newest timestamp safely.
- Recorder retention, purge and long-term statistics are Home Assistant
  responsibilities, not integration responsibilities.

**Observed samples:** a request for S4825 covering
2026-11-06 through 2026-11-09 00:00 returned 73 records at hourly timestamps,
from 2026-11-06 00:00 through 2026-11-09 00:00 (inclusive). A second request
covering 2026-11-09 00:00 through 14:00 returned 15 hourly records, with the
latest timestamp at 14:00. The first record was at 00:00 and the last at
14:00; there were no missing hourly timestamps in that interval. The
hydrometric_level values were populated (1.17 at 00:00 and 1.22 at 14:00),
while the other listed measurement fields were null. These are historical
query samples, not evidence of an instantaneous endpoint, current publication
latency or a guaranteed network-wide hourly cadence. They confirm that
/data_pie can return timestamped time-series rows and that selecting the
maximum date identifies the latest timestamp in this sample. The endpoint's
sort order and best narrow-window query strategy still need testing.

A matching current-day query was then made for S4825 (San Sebastiano Po),
using the same 2026-11-12 00:00–09:00 (+01:00) window and pagination.
It also returned 6 records, with the newest at 05:00 (+01:00). The latest
hydrometric_level was 1.16; all meteorological fields were null. The two
stations therefore had the same latest returned timestamp (05:00) in these
paired queries, despite reporting different parameter sets. This is evidence
of a shared availability/publication boundary in this particular sample, but
does not prove a common upstream cause or distinguish telemetry, ingestion,
processing and API publication delays. Query execution times should be recorded
in future repeat tests to estimate freshness and update cadence.

A current-day query for station 446 (Torino Giardini Reali), covering
2026-11-12 00:00–09:00 (+01:00), returned 6 records. The newest record was
at 05:00 (+01:00), with air_temperature 9.4, humidity 98 and all five
cumulative-rain fields at 0.2. Wind, wind direction, gust, gust direction,
snow height and hydrometric level were null. Thus, at the time this query was
run (morning of 2026-11-12), the newest returned observation was about four
hours behind the requested end time. This is a single station/query sample:
it does not distinguish a station telemetry gap from delayed publication or
an API-side limitation, and must not be generalized as a network-wide delay.

A further query for S4825 covering the complete local day
2026-11-11 00:00–23:00 returned 24 records, one for every hour, including
the requested final timestamp at 23:00 (+01:00). The newest hydrometric_level
was 1.15; the final five hourly values were 1.16 (19:00), 1.16 (20:00),
1.15 (21:00), 1.14 (22:00) and 1.15 (23:00). All other listed measurement
fields were null. This confirms that the API can return a complete recent
calendar day for S4825, but the query was made on 2026-11-12 and therefore
does not measure live publication latency on 2026-11-11.

The separate Meteoweb historical database described below is documented here
for source distinction only. It is **not part of the current integration
consumption scope** unless that requirement changes.



A second station sample was captured for station 446 (Torino Giardini Reali,
registry type `BGHNPRST`). The request covering
2026-11-10 00:00 through 2026-11-11 11:00 returned 34 records; the first
record was timestamped 2026-11-10 00:00 and the newest was
2026-11-11 09:00 (+01:00). In the newest record, air_temperature was 8.6,
humidity was 97, and all five cumulative-rain fields (1h, 3h, 6h, 12h,
24h) were 0.0. Wind, wind direction, gust, gust direction, snow height and
hydrometric level were null. Across the returned sample, the populated
measurement fields were air_temperature, humidity and the five cumulative-rain
fields.

A repeat of the exact same request (same station, date range, page and
page size) returned the same 34 records and the same newest timestamp,
2026-11-11 09:00 (+01:00), with no 10:00 or 11:00 row. The last five records
were hourly from 05:00 through 09:00. This confirms that the repeated response
was unchanged, but the elapsed time between requests was not recorded; it
therefore does not establish a publication interval or prove that the feed is
stalled.

This is a useful contrast with S4825: the common `/data_pie` schema can
contain different populated subsets for different stations. The registry's
composite `station_type` string must not be treated as a direct guarantee
that every corresponding measurement field will be populated in every
response or time window. This sample supports an hourly-looking sequence and
a latest timestamp at 09:00, but it does not establish why no 10:00 or later
record was returned, nor the provider's publication latency. The query window
ended at 11:00, so the newest returned observation was two hours behind the
requested end time; this is an observation from one request, not a general
freshness guarantee.

## 3. Historical hydrometeorological database (out of current integration scope)

This separate source is recorded for completeness and to avoid confusing it with the realtime API. The current integration does not plan to query it: long-term state history is delegated to Home Assistant Recorder.

ARPA's Open Data page links a separate Meteoweb REST API documentation site:
https://utility.arpa.piemonte.it/docs/.

The published description says the historical database contains daily and
monthly weather/hydrological/snow records for all stations in the regional
monitoring network, from the start of operation of individual sensors. Listed
variables include temperature, precipitation, relative humidity, solar
radiation, wind speed and direction.

Do not assume this historical service shares the realtime API's routes,
schemas, identifiers, query limits or update cadence. Its documentation and
authentication/access behaviour must be inspected separately.

## 4. Air quality

### 4.1 Official landing pages

- [ARPA — observed air-quality data](https://www.arpa.piemonte.it/temi/aria/qualita-dellaria-dati-osservati)
- [ARPA — air-quality topic](https://www.arpa.piemonte.it/temi/aria)
- [Aria Piemonte WebGIS](https://webgis.arpa.piemonte.it/aria_piemonte/index.html?page=misure)
- [Aria Ambiente — data](https://aria.ambiente.piemonte.it/qualita-aria/dati)

The ARPA observed-data page describes:
- station measurements, including ozone data for the latest 30 days;
- map-based daily observations and modelled estimates for PM10, PM2.5 and NO2;
- SRRQA measured-data download;
- separate forecast/modelled products at municipal scale.

The page notes that publication/validation schedules differ by product. Some
data are validated on weekday mornings, and weekend/holiday publications may
not have been validated by ARPA technicians. Preserve validation state and
publication time if the underlying source exposes them.

### 4.2 Station metadata ArcGIS service

Service:
https://webgis.arpa.piemonte.it/ags/rest/services/aria/Sistema_rilevamento_regionale_qualita_aria/FeatureServer

Service type: ArcGIS FeatureServer. Query format: JSON. The service advertises
a maximum record count of 2000.

Layers/tables listed by the service:
- Layer 0: stations by zone.
- Layer 1: stations by type.
- Layer 2: stations by relevance.
- Layer 3: stations.
- Table 4: sensor registry.

The service description distinguishes traffic, background and industrial
stations, and urban, suburban and rural site types. It describes station
metadata and sensor registry; it is not, by itself, proof that the measurement
time series are available from this FeatureServer.

The service metadata declares Arpa Piemonte as copyright text. Reuse terms
still need checking.

### 4.3 Recent measurements and municipal modelling ArcGIS service

Service:
https://webgis.arpa.piemonte.it/ags/rest/services/aria/aria_ultimo_mese/FeatureServer

The service description identifies:
- layer 0: measurements from the monitoring network over the last month,
  including PM10-Beta, O3 and NO2;
- layer 1: model assessment and forecasts for municipalities over the last
  month.

This is a promising structured source for a first air-quality integration
candidate. Inspect layer schemas, query examples, time fields, units,
validation attributes, geometry and update cadence before implementation.

### 4.4 Historical measured data

The regional environmental report says measured SRRQA data can be downloaded
by period, pollutant and station, from 2000 to the consultation date, with a
maximum extraction period of one year. This is a download workflow and should
not yet be treated as a stable, anonymous API suitable for frequent polling.

## 5. Spatial discovery and Home Assistant location

Home Assistant has a configured home latitude/longitude. A future config flow
can use this location to rank nearby ARPA stations after downloading the
provider's station registries.

Proposed discovery principles (not yet implemented):
- Keep provider station coordinates and identifiers as the source of truth.
- Calculate distance locally from the Home Assistant home coordinates.
- Rank candidates by more than distance: domain/parameter coverage, station
  type, data freshness and whether the data are observations or model estimates
  should influence relevance.
- For municipality-level products, resolve the configured coordinates to a
  municipality using an authoritative geographic dataset or provider metadata;
  do not pretend the product belongs to a nearby physical station.
- Show the proposed services/stations and let the user confirm or adjust them.
- Allow manual search and selection when automatic matching is unavailable.
- Do not transmit the home's coordinates to ARPA unless a future source
  explicitly requires it; current station discovery can be performed locally
  after retrieving regional catalogues.
- Keep the automatic selection explainable: show station/product name, domain,
  distance or geographic association, and available parameters.

This is a design direction only. Radius, ranking rules, default services,
multi-station selection and config-flow structure remain open pending broader
coverage research.

## 6. Research log

### 2026-11-09 — Initial reconnaissance

- Identified the ARPA Open Data landing page as the main starting point for
  machine-readable meteo/hydrological products.
- Confirmed separate realtime, degree-day and historical Meteoweb API
  documentation links.
- Extracted the published OpenAPI routes and parameters for the realtime API.
- Identified the ARPA air-quality observed-data page, the SRRQA station/sensor
  FeatureServer and the recent-measurements/municipal-modelling FeatureServer.
- Identified Aria Ambiente as the regional data download portal.
- No implementation decision has been made for either data domain.

## 7. Per-endpoint investigation template

For each endpoint/layer, append or complete:

- Provider/product and official landing page.
- URL, HTTP method, parameters and pagination.
- Authentication, rate limits and availability.
- Raw response example (sanitised only if necessary).
- Response schema and stable identifiers.
- Coordinates and coordinate reference system.
- Parameter names, definitions, units and precision.
- Observation/sample time, publication time and retrieval time.
- Update frequency, retention and historical coverage.
- Validation/quality flags and missing-value conventions.
- Spatial/temporal coverage and known gaps.
- Licence, attribution and redistribution terms.
- Proposed Home Assistant representation and rationale.
- Last tested date and test method.
