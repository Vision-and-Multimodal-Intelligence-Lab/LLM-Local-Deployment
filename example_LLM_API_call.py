HOST = ""
PORT = 1
API_KEY = ""

import openai

class local_llm_api:
    def __init__(self, host_ip, port_num, api_key_string):
        self.client = openai.Client(base_url=f"http://{host_ip}:{port_num}/v1", api_key=api_key_string)
        self.model_name = self.client.models.list().data[0].id

        self.history = []

        # print model name when doing initialization
        print(self.model_name)

    def get_reponse(self, message):

        self.history.append({
            "role": "user",
            "content": message,
        })

        response_stream = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.history,
            temperature=0.6,
            top_p=0.95,
            stream=True,
        )

        reasoning = ""
        answer = ""
        content_start = False
        reason_start = False
        for chunk in response_stream:
            if chunk.choices[0].delta.content:
                if not content_start:
                    content_start = True
                    print("\n==== End of the reasoning ====")
                    print("\n==== Beginning of the answer ====")
                print(chunk.choices[0].delta.content, end="")
                answer += chunk.choices[0].delta.content
            elif chunk.choices[0].delta.reasoning_content:
                if not reason_start:
                    reason_start = True
                    print("\n==== Beginning of the reasoning ====")
                print(chunk.choices[0].delta.reasoning_content, end="")

        print("\n==== End of the answer ====\n")

        return answer

    def append_history(self, answer):

        self.history.append({
            "role": "assistant",
            "content": answer,
        })


# example
call_llm = local_llm_api(HOST, PORT, API_KEY)

# message = "How many 'r's are in the word 'strawberry'?"
message = "What are the top 3 most common misconceptions about large language models?"
message2 = "How can these misconceptions be addressed or corrected?"

answer = call_llm.get_reponse(message)
call_llm.append_history(answer)

call_llm.get_reponse(message2)
