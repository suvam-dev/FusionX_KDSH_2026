from openai import OpenAI
client = OpenAI(api_key=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)

def call_llm(prompt):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return resp.choices[0].message.content

