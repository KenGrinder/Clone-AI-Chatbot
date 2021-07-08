import glob
import shutil
import json
import os




def combine_json(main_path):
    counter = 1
    try:
        os.mkdir(os.getcwd() + '/MergedJson/')
    except FileExistsError as e:
        print('File Exists already')

    for file in glob.glob('**/*.json', recursive=True):
        save_path = os.getcwd() + '/MergedJson/' + str(counter) + '.json'
        # filename = str(counter) + file[-5:]
        shutil.copy(file, save_path)
        counter += 1

#if __name__ == "main":
#    combine_json('inbox')
combine_json("inbox")
    
