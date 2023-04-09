You need to add the following to your .bashrc

```
export OPENAI_API_KEY="your_api_key"

export SMARTSH_PATH="path_to_dir_with_smartsh.py"
command_not_found_handle () {
    echo "Let's get help from OpenAI API!"
    python3 $SMARTSH_PATH/smartsh.py "$@"
}
```
