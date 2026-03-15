from __future__ import annotations

from typing import Callable

import requests


OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"


def get_response(prompt: str, model: str, timeout: float = 30) -> str:
    """Send a single prompt to Ollama and return the model response."""
    payload = {"model": model, "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_GENERATE_URL, json=payload, timeout=timeout)
    response.raise_for_status()
    return response.json()["response"]


def ask_llm(
    prompt: str,
    model: str,
    check_fn: Callable[[str], bool] | None = None,
    n_tries: int = 5,
    timeout: float = 30,
) -> str | None:
    """Retry prompting until check_fn accepts the response or attempts run out."""
    for _ in range(n_tries):
        try:
            resp = get_response(prompt=prompt, model=model, timeout=timeout)
        except requests.RequestException:
            continue

        if check_fn is None or check_fn(resp):
            return resp

    return None


def ask_model(
    prompt: str,
    model: str,
    check_fn: Callable[[str], bool] | None = None,
    n_tries: int = 5,
    timeout: float = 30,
) -> str | None:
    """Backward-compatible alias for ask_llm."""
    return ask_llm(
        prompt=prompt,
        model=model,
        check_fn=check_fn,
        n_tries=n_tries,
        timeout=timeout,
    )
