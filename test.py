import json
import re
import random
from pymongo import MongoClient

pattern = '(=.*(look|hiring|hire|seek|search|(?=.*(has|hav|had))(?=.*(position|opening|gig))))(?=.*(engineer|dev|specialist|designer))'


def read_json(path):
    with open(path, 'r') as json_file:
        data_for_loading = json.load(json_file)
        return data_for_loading


def write_json(data_for_saving, path):
    with open(path, 'w') as json_file:
        json.dump(data_for_saving, json_file)

# def read_mongo():
#     db = MongoClient('127.0.0.1', 27018)['lgt_analytics']
#     cursor = db['filtered_messages'].find().skip(2200).limit(100)
#     items = []
#     for item in cursor:
#         items.append({'text': item['text'], 'label': ""})
#     return items


def clean_text(text: str):
    text = re.sub('[^\\w\\d]', ' ', text)
    text = re.sub('\\s+', ' ', text)
    return text.strip().lower()


general = list()
for i in range(1, 10):
    filtered = read_json(f'general.json')
    general.extend(filtered)


pre_tokenized = list()

for item in general:
    pre_tokenized.append({'data': clean_text(item['data']), 'label': item['label']})

success = 0
for item in pre_tokenized:
    if re.match(pattern, item['data'], re.IGNORECASE) and item['label'] == '1':
        success += 1

print(f'Total: {len(pre_tokenized)}\n'
      f'Successed: {success}\n'
      f'Unsuccessed: {len(pre_tokenized) - success}')


# client = MongoClient("mongodb://localhost:27017/")
# db = client["dataset"]
# collection = db["training"]
# collection_ = db['validation']
#
# general = read_json('general.json')
# validation = list()
# for item in general:
#     r = random.randint(1, 10)
#     if r == 2 or r == 3:
#         collection_.insert_one(item)
#     else:
#         collection.insert_one(item)
