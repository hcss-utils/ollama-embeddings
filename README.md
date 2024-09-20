# ollama-embeddings
This repository contains a Dockerfile for running an embeddings model using Ollama on a local server.

Original README below:

---

How to run this:

1. build the Docker image from the Dockerfile:
```console
docker build -t ollama-image
```

2. run a container from the image (exposes API to the world):
```console
docker run -p 11434:11434 --name ollama-embeddings ollama-image
```

2.1 run a container from the image, accessible only from the server itself:
```console
docker run -d -p 127.0.0.1:11434:11434 --name ollama-embeddings ollama-image
```

3. usage example (from within the server):
- curl:
```console
curl http://127.0.0.1:11434/api/embeddings -d '{
  "model": "nomic-embed-text",
  "prompt": "The sky is blue because of Rayleigh scattering"
}'
```

- python:
```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

def get_embedding(text: str, model: str = "nomic-embed-text") -> list[float]:
    return client.embeddings.create(input=[text], model=model).data[0].embedding

if __name__ == "__main__":
    text = "The sky is blue because of Rayleigh scattering"
    embedding = get_embedding(text)
    print(embedding)
```

4. (the simplest) usage example (with FastAPI):
4.1. start a new tmux session:
```console
tmux new -s uvicorn_session
```

4.2 then run the following command (set a token in the [app.py](app.py)):
```console
uvicorn app:app --reload --host 0.0.0.0 --port 11435
```

4.3 dettach from the session:
```
Ctrl + B, then D
```

4.4 reattach later:
```console
tmux attach -t uvicorn_session
```