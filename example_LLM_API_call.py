HOST = ""
PORT = 1
API_KEY = ""

import openai

client = openai.Client(base_url=f"http://{HOST}:{PORT}/v1", api_key=API_KEY)
model_name = client.models.list().data[0].id

print(model_name)

# message = "How many 'r's are in the word 'strawberry'?"
message = "What are the top 3 most common misconceptions about large language models?"
message2 = "How can these misconceptions be addressed or corrected?"

history = [
    {
        "role": "user",
        "content": message,
    }
]

response_stream = client.chat.completions.create(
    model=model_name,
    messages=history,
    temperature=0.6,
    top_p=0.95,
    stream=True,  # Non-streaming
    # extra_body={"separate_reasoning": True},
)

reasoning = ""
answer = ""
content_start = False
for chunk in response_stream:
    if chunk.choices[0].delta.content:
        if not content_start:
            content_start = True
            print("\n==== Text ====")
        print(chunk.choices[0].delta.content, end="")
        answer += chunk.choices[0].delta.content
    elif chunk.choices[0].delta.reasoning_content:
        print(chunk.choices[0].delta.reasoning_content, end="")

print("\n==== End of the answer ====")

history.append({
    "role": "assistant",
    "content": answer,
})

# New question
history.append({
    "role": "user",
    "content": message2,
})

# Send out new request
response_stream = client.chat.completions.create(
    model=model_name,
    messages=history,
    temperature=0.6,
    top_p=0.95,
    stream=True,  # Non-streaming
    # extra_body={"separate_reasoning": True},
)

reasoning = ""
answer = ""
content_start = False
for chunk in response_stream:
    if chunk.choices[0].delta.content:
        if not content_start:
            content_start = True
            print("\n==== Text ====")
        print(chunk.choices[0].delta.content, end="")
        answer += chunk.choices[0].delta.content
    elif chunk.choices[0].delta.reasoning_content:
        print(chunk.choices[0].delta.reasoning_content, end="")
