#!/bin/bash

# Display a warning to the user 
echo "WARNING: This script will change .bashrc "
echo "You need to have openai api key ready "
echo "Do you wish to proceed? (y/n)"
read confirm

if grep -q "# smartsh configuration" ~/.bashrc; then
  echo "ERROR: the script was previosly  run"
  echo "Aborting script."
  exit 1
fi

# If the user confirms by entering "y", proceed with asking for their details and appending them to the file
if [[ "$confirm" == "y" ]]; then

  # Ask the user for the folder in which the input.txt file is located
  echo "Please enter to continue with home folder"
  echo "or type in full path to download location"
  read folder_path

  # If the user did not provide a folder path, set the folder path to the home folder
  if [[ -z "$folder_path" ]]; then
    folder_path="$HOME"
  fi

  #go to specified path or home folder and clone git
  cd $folder_path
  git clone https://git.ashik.se/ashikk/smartsh.git


  # Ask the user for their api key and store it in a variable
  echo "What is your openid apikey?"
  read apikey

  #if they didnt enter api key then exit script
  if [[ -z "$apikey" ]]; then
    echo "api key not entered : exiting"
    exit 1
  fi

   # start editing .bashrc enter apikey and folder path
  echo "# smartsh configuration" >> ~/.bashrc
  echo "export OPENAI_API_KEY=\"$apikey\"" >> ~/.bashrc
  echo "export SMARTSH_PATH=\"$folder_path/smartsh\"" >> ~/.bashrc

  # use smartsh.py to handle command not found  
  echo "command_not_found_handle () { "  >> ~/.bashrc
  echo "  echo \"Let's get help from OpenAI API!\" "  >> ~/.bashrc
  echo "  python3 \$SMARTSH_PATH/smartsh.py \"\$@\" "  >> ~/.bashrc
  echo "} "  >> ~/.bashrc
  echo "# end of smartsh configuration" >> ~/.bashrc
  echo "Installation completed"  


else
  # If the user does not confirm by entering "y", display a message indicating that the script has been cancelled
  echo "Script cancelled. No changes have been made "
fi
