import os
import requests

API_KEY = os.environ.get("DASHSCOPE_API_KEY")


url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

resp = requests.post(
    url,
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "model": "qwen-plus",
        "messages": [{"role": "user", "content": "你好，用一句话介绍你自己"}],
    },
)

print(resp.status_code)
print(resp.json()["choices"][0]["message"]["content"])
