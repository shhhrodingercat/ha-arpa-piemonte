# Contributing

Thanks for taking an interest in ARPA Piemonte for Home Assistant.

The project is in its foundation phase. At this stage, the most useful
contributions are source/API research, documentation improvements and reviews
of the proposed semantics. Please open an issue before starting a substantial
implementation so that the scope and source assumptions can be discussed.

## Development environment

Use Python 3.13 and create a virtual environment:

~~~bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements_test.txt
~~~

Run the repository checks before opening a pull request:

~~~bash
ruff check .
ruff format --check .
pytest
~~~

## Working principles

- Prefer official ARPA Piemonte sources and structured interfaces.
- Record the source URL, access method, retrieval date and applicable licence
  or terms for every dataset investigated.
- Do not infer units, thresholds, validation states or sampling frequencies.
- Keep observations, forecasts, estimates and derived values distinct.
- Preserve missing values as missing; never silently substitute zero.
- Avoid adding dependencies unless there is a clear technical need.
- Do not add entities solely because a source exposes a field. Each entity
  needs a documented use and correct Home Assistant semantics.
- Keep independent data services isolated so that a source failure does not
  affect unrelated services.

## Pull requests

Please include a concise description of the change, its rationale and the
checks performed. Changes that introduce a data source should also update the
source inventory and document licensing and attribution findings.
