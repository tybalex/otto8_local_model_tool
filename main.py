import openai
import os

local = "http://127.0.0.1:1234/v1/"
mac_docker_host = "host.docker.internal:1234/v1/"
client = openai.OpenAI(api_key="sk-", base_url=mac_docker_host)

def get_oai_response(model, functions, msgs):
  
  try:
    completion = client.chat.completions.create(
      model=model,
      temperature=0.1,
      messages=msgs,
    #   tools=functions,
    #   tool_choice="auto",
      stream=False,
    )
    return completion.choices[0]
  except Exception as e:
    print("Error in get_oai_response")
    print(e)


def main():
    user_query = os.getenv("MESSAGE")
    if not user_query or user_query == "":
        print("MESSAGE environment variable is not set or empty.")
        return
    system_prompt = "You are a helpful assistant."
    msgs = [{"role": "system", "content":system_prompt} ,{"role": "user", "content": user_query}]
    model = "Llama-3-8b-function-calling-alpha-v1.gguf"
    res = get_oai_response(model=model, functions=[], msgs=msgs)
    print(res)

if __name__ == "__main__":
    main()