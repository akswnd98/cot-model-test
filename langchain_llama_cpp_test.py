
from langchain_community.chat_models.llamacpp import ChatLlamaCpp
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.tools import tool

llm = ChatLlamaCpp(
  model_path="../deepseek-r1-distill-llama-8b/DeepSeek-R1-Distill-Llama-8B-Q4_0.gguf",
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


llm.bind_tools(
  tools=[get_current_weather, send_email],
  tool_choice={
    "type": "function",
    "function": {
      "name": "get_current_weather"
    }
  }
)

messages = [
  SystemMessage(content="You are a helpful assistant. You can call tool functions in JSON format if needed."),
  HumanMessage(content="please check current weather on seoul korea. i use celsius to describe degree.")
]

output = llm.invoke(
  messages,
  max_tokens=2048
)

print(output)
