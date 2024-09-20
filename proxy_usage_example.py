import json
import requests

headers = {
    "Authorization": f'Bearer {os.environ["FASTAPI_TOKEN"]}',
    "Content-Type": "application/x-www-form-urlencoded",
}

text = "The sky is blue because of Rayleigh scattering"

data = json.dumps({"model": "nomic-embed-text", "prompt": text})
response = requests.post("http://<IP>:11435/api/embeddings", headers=headers, data=data)
print(response.json()["embedding"])
