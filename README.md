# DeepEval tutorial

Small Python example project for tracing and testing LLM evaluations with DeepEval. `main.py` is the entry point, `trace.py` demonstrates tracing, and `test_example.py` contains an evaluation example.

## Setup

```bash
uv sync
cp .env.example .env
```

Set the required provider credentials in `.env`, then run:

```bash
uv run python main.py
uv run pytest
```

The separate `deepeval-examples/` checkout is an upstream project and is not bundled here.
