
from llama_cpp import Llama
# from langchain_community.chat_models.llamacpp import ChatLlamaCpp
from langchain_core.tools import tool

#llm = ChatLlamaCpp(
#  model_path="./DeepSeek-R1-Distill-Llama-8B-Q4_0.gguf",
#  n_ctx=4096
#)

llm = Llama(
  model_path="./DeepSeek-R1-Distill-Llama-8B-Q4_0.gguf",
  n_ctx=4096
)

@tool
def get_current_weather (location: str, format: str):
  """
Get the current weather

Args:
  location: The city and state, e.g. San Francisco, CA
  format: The temperature unit to use. Infer this from the users location. (choices: ["celsius", "fahrenheit"])
"""

  return "38 degree"

@tool
def send_email (address: str, subject: str, body: str):
  """
send email

Args:
  address: target email address.
  subject: title of this email.
  body: main detail of this email.
"""

  return "email sent successfully"


#llm.bind_tools(tools=[get_current_weather, send_email])

#output = llm.invoke(
#  "please tell me current weather in celsius",
#  max_tokens=1024
#)

#print(output)

print('hello: ' + llm.metadata['tokenizer.chat_template'])
