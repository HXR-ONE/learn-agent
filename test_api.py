from openai import OpenAI

client = OpenAI(
    api_key="sk-4798083e0a37478697a9cc2e18936dcb",
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个有用的助手，用中文回答"},
        {"role": "user", "content": "用一句话介绍你自己"}
    ]
)

print(response.choices[0].message.content)
