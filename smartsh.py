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
smarsh_dont_warn = os.environ.get("SMARTSH_DONT_WARN") == "1"
if api_model is None:
    api_model = "gpt-3.5-turbo"
    if smarsh_dont_warn != True:
        print("Warning: OPENAI_MODEL_ID not set. Supported models are text-davinci-003, gpt-3.5-turbo")
        print("Using default model " + api_model)

smarsh_debug_mode = os.environ.get("SMARTSH_DEBUG")

is_in_teacher_mode = False
smartsh_teacher_mode = os.environ.get("SMARTSH_TEACHER_MODE")
if smartsh_teacher_mode == "1" or smartsh_teacher_mode == "true":
    if smarsh_dont_warn != True:
        print("Teacher mode enabled")
    is_in_teacher_mode = True


if smarsh_debug_mode == "1" or smarsh_debug_mode == "true":
    print("Debug mode enabled")
    print("OpenAI API key: " + openai.api_key)
    print("OpenAI model: " + api_model)

# argcmd contains the entire command line arguments as a space separated string
argcmd = " ".join(sys.argv)
prompttxt  = ""
if is_in_teacher_mode:
    prompttxt = "You suggest a valid shell command to accomplish the following, together with an explanation: " + argcmd
else:
    prompttxt = "You suggest a valid and correct {os.environ.get('SHELL')} command to accomplish the following, without any further explanation or additional text: " + argcmd
completion = None
apioutput = None
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
    apioutput = completion['choices'][0]['text'].strip()
elif api_model == "gpt-3.5-turbo":
    completion = openai.ChatCompletion.create(
    model = api_model,
    messages = [
        {'role': 'system', 'content': prompttxt}
    ],
    temperature = 0
    )
    # print the response to stdout
    apioutput = completion['choices'][0]['message']['content'].strip()

# Ask the user if the suggested command shall be executed
if is_in_teacher_mode == False and apioutput is not None:
    print("Suggested command: " + apioutput)
    print("Do you want to execute this command? (y/n)")
    user_input = input()
    if user_input == 'y':
        print("Executing command: " + apioutput)
        os.system(apioutput)
    else:
        print("Command not executed")
else:
    print(apioutput) 
