clear
read -r -p "Would you like to import Facebook Data? [y/N] " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
	then read -r -p "Have you copied your Facebook JSON zip to the root of this folder? [y/N] " response
	if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
	then
    		echo What is your Facebook Name? .. Enter name EXACTLY as it appears on your Facebook
			read fbname
    		unzip -qq *.zip -d "temp"
			cp -r temp/messages/inbox inbox
			rm -rf temp
			echo Combing JSON files into one folder / Exporting master input.csv file. Will not overwrite existing input.csv
    		python3 combine.py
		cp fbparse.py MergedJson/
		cd MergedJson/
    		python3 fbparse.py "$fbname"
    		cd ..
			mkdir CozyPlace
    		cp -n MergedJson/input.csv CozyPlace/input.csv
    		echo 
	else
    		echo Please Re-Run Script with JSON zip in correct location
    		exit
fi
else
    echo Skipping...
fi

rm -rf MergedJson
rm -rf inbox
echo You will have to enter your Hugging Face credentials
echo What is your Hugging Face username?
read username
echo What is your Hugging Face password?..... Will be sent via HTTPS, change password if it contains special characters.
read -s password
echo What is your model name?
read model
echo Would you like to use the small, medium, or large
read modelsize


read -r -p "Have you already created your model on Hugging Face? [y/N] " response
	if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
	then
    		echo Skipping...
	else
    		echo Sign into Hugging Face to create your model.
    		transformers-cli login
    		transformers-cli repo create $model
fi

sleep 5


pip install -r requirements.txt
python3 modeltrain.py "microsoft/DialoGPT-$modelsize"

#Bottom of script to send finished model to Hugging Face
git lfs install
git config --global credential.helper store
git clone https://$username:$password@huggingface.co/$username/$model
ls
cp -r CozyPlace/output/*.* $model/
cd $model
git add . && git commit -m "Model and Tokenizer push from $USER"
git push
