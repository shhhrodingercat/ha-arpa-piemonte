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
