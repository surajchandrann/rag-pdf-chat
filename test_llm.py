from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1",api_key="ollama")
r=client.chat.completions.create(
    model="llama3.2:3b",
    messages=[{"role":"user","content":"Explain RAG in one sentence."}],)
print(r.choices[0].message.content)