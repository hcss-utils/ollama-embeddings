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

