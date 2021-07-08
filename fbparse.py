#!/usr/bin/env python
from __future__ import print_function
import io
import os
import json
import re
import csv
import sys

fbname = sys.argv[1]
def read_json():
    with open('combined.txt', 'w', encoding='utf-8') as masterf:
        for file in os.listdir(os.getcwd()):
            if file.endswith('.json'):
                with open(file, 'r', encoding='utf-8') as jsonf:
                    json_data = json.loads(jsonf.read())

                    for item in json_data['messages']:
                        try:
                            if item['sender_name'] == fbname:
                                print('Match')
                                if len(item['content']) > 1:
                                    masterf.write(item['content'] + '\n')

                        except KeyError as e:
                            print(f'Your error is this -    {e}')


def clean_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        with open('preinput.csv', 'w', encoding='utf-8') as newf:
            csv_writer = csv.DictWriter(newf, delimiter=',', fieldnames=['line'])
            csv_writer.writeheader()
            file_lines = f.readlines()
            for line in file_lines:
                word = re.sub(r'^https?:\/\/.*[\r\n]*', '', line)
                word1 = re.sub(r'You added \w+ \w+ on Messenger.', '', word)
                word2 = re.sub(
                    r'You can now message and call each other and see info like Active Status and when you\'ve read messages.',
                    '', word1)
                word3 = re.sub(
                    r'Please follow local guidelines about physical distancing and staying home during COVID-19. Learn More\(https://www.facebook.com/marketplace/commerce-education/\)',
                    '', word2)
                word4 = re.sub(r'You changed the group photo.', '', word3)
                word5 = re.sub(r'You named the group .+', '', word4)
                word6 = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', word5)
                word7 = re.sub(
                    r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
                    '', word6)
                word8 = word7.replace('\n', '')

                if len(word8) > 1:
                    if len(word8) >= 200:
                        print('Sentence exceeded 200 chars, skipping')
                    else:
                        csv_writer.writerow({'line': word8})
                        # newf.write(word + '\n')


read_json()
clean_file('combined.txt')
with io.open('preinput.csv', 'r', encoding='utf-8', errors='ignore') as infile, \
        io.open('input.csv', 'w', encoding='ascii', errors='ignore') as outfile:
    for line in infile:
        print(*line.split(), file=outfile)
