# Backup manifest

This is a clean source snapshot; the original directory has no usable Git history.

Excluded:

- `.env.local`, which contains a nonempty `LOCAL_MODEL_API_KEY`; rotate it if it was ever exposed.
- `deepeval-examples/`, a nested upstream clone.
- `.venv/`, `.deepeval/`, pytest caches, and bytecode.

Credential fields in `.env.example` have been blanked. The original project remains unchanged.
