from openai import OpenAI

client = OpenAI(
    api_key="anyKey"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful Virtual Assistant"},
        {
            "role": "user",
            "content": "What is coding?"
        }
    ]
)