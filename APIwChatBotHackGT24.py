from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key='ENTER API KEY')

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "YOUR-QUERY-HERE"}
  ]
)

print(completion.choices[0].message.content)