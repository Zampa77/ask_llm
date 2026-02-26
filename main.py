import requests


# %% llm functions
# function to ask question
def get_response(prmpt, model):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-type": "application/json"}
    data = {"model": model, "prompt": prmpt, "Stream": False}
    response = requests.post(url, headers=headers, data=json.dumps(data))

    while response.status_code != 200:
        response = requests.post(url, headers=headers, data=json.dumps(data))

    response_text = response.text
    data = json.loads(response_text)
    actual_response = data["response"]
    return actual_response


# function with safeguard
# check fn should return Boolean T or F
def ask_llm(prompt, model, check_fn=None, n_tries=5):
    resp = None

    if check_fn is None:
        return get_response(prmpt=prompt, model=model)

    for _ in range(n_tries):
        resp = get_response(prmpt=prompt, model=model)
        if check_fn(resp):
            return resp

    print("Max tries reached — returning None")
    return None
