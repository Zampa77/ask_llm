# %%
import requests


# %%
def get_response(prmpt, model, timeout=100):
    url = "http://localhost:11434/api/generate"
    payload = {"model": model, "prompt": prmpt, "stream": False}
    response = requests.post(url, json=payload, timeout=timeout)
    response.raise_for_status()
    return response.json()["response"]


def ask_model(prompt, model, check_fn=None, n_tries=5, timeout=30):
    for _ in range(n_tries):
        try:
            resp = get_response(prmpt=prompt, model=model, timeout=timeout)
        except requests.RequestException:
            continue

        if check_fn is None or check_fn(resp):
            return resp

    print("Max tries reached — returning None")
    return None
