smartsh.py is a simple python script that I wrote which can take a task description (any string) as argument and query OpenAPI's API to tell you how to accomplish the given task using a shell command. Yes, chatgpt from command line (sort of).  But let me tell you a simple trick that you can use to supercharge your bash with it!

bash (I think starting from 4.0) conveniently provides a  handler for situations when a command that the user entered is invalid.

You just need to provide a function named command_not_found_handle ()  and point it to the action to be taken on, yes, when a command is not found :-)

In this case, you need to add the following to your .bashrc for the magic to work:

```
export OPENAI_API_KEY="your_api_key"

export SMARTSH_PATH="path_where_you_checked_out_smartsh"

command_not_found_handle () {
    echo "Let's get help from OpenAI API!"
    python3 $SMARTSH_PATH/smartsh.py "$@"
}

```


Some examples:

```
bash$ Show the most recent file in the present working directory
Let's get help from OpenAI API!
ls -t | head -n1
```

```
bash$ Kill all Google chrome renderer processes
Let's get help from OpenAI API!
The command to accomplish this task is:

pkill -f "chrome.*renderer"


This command uses the `pkill` command to send a signal to all processes whose name matches the regular expression `chrome.*renderer`. This will effectively kill all Google Chrome renderer processes.
```

You can set the following additional environment variables which smartsh can make use of:

`OPENAI_MODEL_ID`: The model to use: Supported models are "text-davinci-003", "gpt-3.5-turbo"
    If the variable is not set, we use "gpt-3.5-turbo" by default

`SMARTSH_DEBUG` : Will print additional debug info when running smartsh
