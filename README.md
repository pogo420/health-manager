# health-manager
REST API for managing health.

## What it does?
- Provides endpoints to update steps and weight.
- Provides endpoints to get reports generated via ML engines.

## Techstack:

|Component|Tech|
|---|---|
|Webframework | FastApi |
|Ut framework | Pytest |
|DB | Sqlite |
|Recommendation Engines | AI/ML/Neural|

## Current dev:
- Current plan [docs](./docs/v1/plan_v1.md)

## Dev setup:
- First time:
   - python -m venv .venv
   - pip install poetry
   - poetry intall
- To start server: `./run_server.sh`

## Roadmap/TODO:
- Security features.
- Rate limiting.
- Profiling and telemetry.
