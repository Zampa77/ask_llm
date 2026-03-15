# ask_llm

`ask_llm` is a small Python package for prompting a local Ollama model from Python.

It exposes:

- `get_response(prompt, model, timeout=30)`: send one prompt and return the model response.
- `ask_llm(prompt, model, check_fn=None, n_tries=5, timeout=30)`: retry until a validation function accepts the response.

## Requirements

- Python 3.9+
- A running Ollama server at `http://localhost:11434`

## Installation

Install in your active interpreter (outside `venv` if you are not inside one):

```bash
python -m pip install .
```

Install in editable mode for development:

```bash
python -m pip install -e .
```

## Usage

```python
from ask_llm import ask_llm

response = ask_model(
    prompt="Explain recursion in one sentence.",
    model="llama3.1"
)
print(response)
```

With response validation:

```python
from ask_llm import ask_llm

def has_period(text: str) -> bool:
    return "." in text

response = ask_model(
    prompt="Answer with one sentence.",
    model="llama3.1",
    check_fn=has_period,
    n_tries=3,
)
print(response)
```
