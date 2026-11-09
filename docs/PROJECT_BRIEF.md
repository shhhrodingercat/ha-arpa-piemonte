# Project brief

## Purpose

Build a reliable Home Assistant custom integration for environmental data
published by **ARPA Piemonte**. The integration should make selected datasets
useful for dashboards and automations without losing the meaning, quality or
provenance of the source data.

## Scope

The current project is deliberately limited to ARPA Piemonte.

Potential areas of investigation include:

- hydrometeorological observations;
- air quality;
- pollen and aerobiology;
- weather forecasts;
- groundwater and surface water;
- snow and related bulletins;
- other environmental datasets where a structured source and a meaningful
  Home Assistant use case can be demonstrated.

The list is exploratory. Inclusion in this list does not mean that a public
API exists, that the data can be redistributed, or that the area will
necessarily be implemented.

## Out of scope for the initial project

- A generic integration for all Italian regional environmental agencies.
- Scraping web pages when a supported structured source is available.
- Automatically importing every station or every source parameter.
- Inventing thresholds, classifications, units or missing measurements.
- Implementing a service before its source, semantics and terms of use have
  been investigated.

## Product principles

1. **Source fidelity:** preserve what the provider actually publishes.
2. **Explicit provenance:** retain station/source identity and relevant
   timestamps and quality metadata.
3. **Semantic separation:** distinguish observations, forecasts, estimates,
   validated values and derived values.
4. **Fault isolation:** independent services must have independent retrieval
   and update lifecycles.
5. **Selective entities:** create entities only where they have a clear user
   or automation purpose.
6. **Native Home Assistant experience:** use config flows, devices, entities,
   diagnostics and platform conventions where they fit the data.
7. **Small dependency footprint:** use Home Assistant facilities and the
   standard library where practical.

## Development sequence

1. Establish repository conventions, documentation and automated checks.
2. Complete source/API reconnaissance for each candidate data area.
3. Define the canonical data model from the actual source characteristics.
4. Decide configuration, station selection and service lifecycle.
5. Implement one well-understood service end to end.
6. Add service-specific tests, documentation and diagnostics.
7. Expand only when the next source is sufficiently understood.

## Current status

The repository is a project skeleton. It has no data clients, coordinators,
platform entities or functioning data services yet. The initial config flow
only creates the provider entry. This is intentional: implementation follows
source research and explicit design decisions.
