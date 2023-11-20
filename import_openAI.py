import openai

# open ai에서 발급받은 api key를 등록합니다
OPENAI_YOUR_KEY = "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"
openai.api_key = OPENAI_YOUR_KEY

# 사용 모델을 설정합니다. chat GPT는 gpt-3.5-turbo를 사용합니다.
model = "gpt-3.5-turbo"
query = "오늘 저녁 메뉴 추천해 줘."

messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": query}
]

response = openai.ChatCompletion.create(
    model=model,
    messages=messages
)

answer = response['choices'][0]['message']['content']
print(f'ChatGPT: {answer}')
messages.append({"role":"assistant", "content":answer})