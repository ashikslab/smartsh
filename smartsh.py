import openai
import os
import sys

#Get the OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")
# check if the API key is set
if openai.api_key is None:
    print("Please set the OPENAI_API_KEY environment variable")
    sys.exit(1)

api_model = os.environ.get("OPENAI_MODEL_ID")
if api_model is None:
    api_model = "gpt-3.5-turbo"
    print("Warning: OPENAI_MODEL_ID not set. Supported models are text-davinci-003, gpt-3.5-turbo")
    print("Using default model " + api_model)

smarsh_debug_mode = os.environ.get("SMARTSH_DEBUG")

if smarsh_debug_mode == "1" or smarsh_debug_mode == "true":
    print("Debug mode enabled")
    print("OpenAI API key: " + openai.api_key)
    print("OpenAI model: " + api_model)

# argcmd contains the entire command line arguments as a space separated string
argcmd = " ".join(sys.argv)

prompttxt = "Suggest a linux shell command to accomplish the following: " + argcmd
completion = None
if api_model == "text-davinci-003":
    print("Using model " + api_model)
    # Get the completion from OpenAI
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompttxt,
        temperature=0,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    # print the output from davinci model to stdout
    print(completion['choices'][0]['text'].strip())
elif api_model == "gpt-3.5-turbo":
    completion = openai.ChatCompletion.create(
    model = api_model,
    messages = [
        {'role': 'user', 'content': prompttxt}
    ],
    temperature = 0
    )
    # print the response to stdout
    print(completion['choices'][0]['message']['content'])

