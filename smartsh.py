import openai
import os
import sys

#Get the OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")
# argcmd contains the entire command line arguments as a space separated string
argcmd = " ".join(sys.argv)

prompt = "Suggest a linux shell command to accomplish the following: " + argcmd
completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'user', 'content': prompt}
    ],
    temperature = 0
)

# print the response to stdout
print(completion['choices'][0]['message']['content'])
