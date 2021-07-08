

## AI Chatbot



*This is a fork of the Discord AI chatbot Google Colab found here:
https://github.com/RuolinZheng08/twewy-discord-chatbot

A special thanks to [Odin](https://github.com/odinmay) for all the help creating this!*







## Create a Discord bot that talks like you!



This is a Discord AI Chatbot that uses the Microsoft DialoGPT conversational model fine-tuned on message data from your Facebook.
Using the export data function within Facebook, these scripts will train the model to speak like you do!
Be warned, using Facebook Message data can cause the bot to potentially repeat anything you've said over messenger.


The purpose of this script, was to run the training model outside of Google colab on a beefier GPU for a larger data set and larger model (I was getting GPU memory errors with my 30,000+ lines of conversation data even after lowering batch sizes)

The other intention was to completely automate this script with questions at the beginning, allow it to upload itself to Hugging Face after the scrip runs. This allows you to use a service such as vast.ai to rent a gpu while this script does everything for you so you don't waste any rented time. It also will automatically parse Facebook JSON data, and remove emojis / werid characters.

***NOTE:** This script does ask for Hugging Face login credentials to create/upload for you. All information is saved as variables for the script locally.*




## Usage:

 **Download Facebook data from Facebook**

 - Download your Facebook Data
 - Open your Facebook and go into Settings & Privacy > Settings
 - Go to Your Facebook Information > Download Your Information
 - Select the data range “All of my data”, format “JSON” and Media
   Quality “Low” (Media quality is for the pictures and not needed)
 - Select Messages
 - Click on Create File

This will create a zip file for download. This can take anywhere from minutes to a day depending on how much data you have.


## Clone AI Chatbot

    git clone https://github.com/KenGrinder/Clone-AI-Chatbot.git

    cd Clone-AI-Chatbot

Copy Facebook .zip file into Clone-AI-Chatbot directory.

Make the script executable.

    chmod +x run.sh
    
Run the script:


    ./run.sh

Follow the prompts.


To deploy your bot onto Discord, follow the instructions provided at the end of the page here:
https://www.freecodecamp.org/news/discord-ai-chatbot/ (How to Build the Chatbot section)





## TO-DO

 - Option to opt-out of uploading to Hugging Face
 - Better navigation within script / skip to sections / set more paramaters (batch size, epochs) within prompts
 - Add support for importing SMS messages
 - Fix issue where loading bars designed for Colab do not display status properly (IProgress / ipywidgets)
 - Remove all unnecessary Google Colab portions of the script

