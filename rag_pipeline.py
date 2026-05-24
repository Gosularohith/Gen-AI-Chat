from vector_store import VectorStore
from openai import OpenAI

class RAGAssistant:
    def __init__(self):
        self.vs = VectorStore()
        self.llm = OpenAI(api_key="YOUR_API_KEY")
        self.history = []

    def answer(self, question: str):
        # Step 1: Retrieve relevant docs
        docs = self.vs.search(question, top_k=3)

        # Step 2: Build context
        context = "\n".join([d["text"] for d in docs])

        # Step 3: Inject into LLM prompt
        prompt = f"Answer based on context:\n{context}\n\nQuestion: {question}"

        response = self.llm.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}]
        )

        # Step 4: Maintain short history
        self.history.append({"q": question, "a": response.choices[0].message.content})
        self.history = self.history[-5:]

        return response.choices[0].message.content
