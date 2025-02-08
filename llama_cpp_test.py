
from llama_cpp import Llama
from langchain_core.tools import tool

llm = Llama(
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

output = llm.create_chat_completion(
  messages = [
    {
      "role": "system",
      "content": "you are a good assistant"
    },
    {
      "role": "user",
      "content": "please check current weather on seoul korea. i use celsius to describe degree"
    }
  ],
  tools=[{
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get current weather in given location with format",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "format": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"]
          }
        },
        "required": ["name", "age"]
      }
    }
  }],
  tool_choice={
    "type": "function",
    "function": {
      "name": "get_current_weather"
    }
  }
)

print(output['choices'][0]['message']['function_call'])
