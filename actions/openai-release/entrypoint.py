import openai
import os
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = os.getenv("PROMPT")
log_file = os.getenv("LOG_FILE")

try:
    with open(log_file, 'r') as f:
        logs = f.read()
except FileNotFoundError:
    print(f"Error: Log file '{log_file}' not found.")
    sys.exit(1)

response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": f"{prompt}\n{logs}"}]
)

print(response.choices[0].message['content'])
