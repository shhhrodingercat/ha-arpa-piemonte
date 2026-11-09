# Architecture and project decisions

This document records decisions that should remain explicit as the project
evolves. Update it when a decision is made or superseded.

## Accepted decisions

### 2026-11-09 — Piemonte-only initial scope

The integration targets ARPA Piemonte only. A reusable design is welcome, but
multi-region support is not a current requirement and must not drive premature
abstraction.

### 2026-11-09 — Research before implementation

Source/API reconnaissance, data semantics and terms of use must be investigated
before implementing a service. The first implementation must not be selected
solely because an endpoint is easy to call.

### 2026-11-09 — Independent service lifecycles

Different data services must be isolated at the retrieval/update level. An
outage or malformed response from one service must not stop unrelated services.

### 2026-11-09 — Preserve source semantics

Missing values are not zero. Observations are not forecasts. Raw, estimated and
validated values must not be conflated. Units, timestamps, thresholds and
quality flags must not be inferred without evidence.

### 2026-11-09 — Avoid entity sprawl

The integration will expose useful Home Assistant entities, not every raw
parameter by default. Each entity needs a clear purpose and correct platform,
device class, unit and state/statistics semantics.

### 2026-11-09 — Minimal initial configuration

The first config flow creates one provider-level config entry. It intentionally
does not yet select services or stations. The final configuration model will be
decided after source and service relationships are understood.

### 2026-11-09 — Minimal dependencies

No third-party runtime dependency is added until a concrete source or
Home Assistant requirement justifies it.

### 2026-11-09 — Location-aware initial discovery (design direction)

The config flow should use Home Assistant's configured home coordinates as the
starting point for suggesting relevant ARPA data sources. Candidate stations
should be ranked using distance together with domain/parameter coverage,
station type and data semantics. Municipality-level model products must remain
territorial products rather than being represented as measurements from a
nearby physical station. The flow should explain its suggestions and allow
the user to confirm, edit or choose manually.

The exact ranking, search radius, service defaults and configuration UI remain
open until the source inventories and geographic coverage are better known.
The home coordinates should be processed locally wherever possible and should
not be sent to ARPA merely to perform station discovery.

### 2026-11-09 — Latest observations only; Recorder owns history

The integration consumes the latest available observation for each selected
source/station/parameter, with "current" understood as the newest value
published by the provider, not necessarily a live measurement. It does not
perform historical backfill or maintain its own historical store. Home
Assistant Recorder is responsible for retaining entity states and serving
history/statistics.

Polling cadence must follow the source's actual update frequency and publication
latency. The integration must preserve source timestamps, handle delayed or
out-of-order records safely, and never turn null/missing values into zero. For
date-range APIs, use a narrow recent lookback only after response ordering and
latency have been verified.

## Open decisions

These are intentionally unresolved:

- Whether services and stations belong in the provider entry's options flow,
  config subentries, or another native Home Assistant configuration pattern.
- The canonical model and the boundary between shared fields and
  source-specific metadata.
- Coordinator ownership and update cadence for each dataset.
- Station/device identity and how multiple services at one physical station
  should appear in Home Assistant.
- Which datasets justify native sensor, binary_sensor, weather, event or
  other platforms.
- Historical backfill, retention and derived measurements.
- Minimum supported Home Assistant version.
- Per-dataset licence, attribution and redistribution requirements.

Do not treat an open decision as an implementation commitment.
