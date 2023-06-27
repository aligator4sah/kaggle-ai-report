import json
import random
import sys

def sample_from_dict(d, sample=10):
    keys = random.sample(list(d), sample)
    values = [d[k] for k in keys]
    return dict(zip(keys, values))


def sample_from_list(d, sample=10):
    keys = random.sample(d, sample)
    values = [d[k] for k in keys]
    return dict(zip(keys, values))


data = [json.loads(line)
        for line in open('arxiv_metadata_20230510.json', 'r', encoding='utf-8')]
chunkSize = 4550
for i in range(0, len(data), chunkSize):
    with open("split" + '_' + str(i//chunkSize) + '.json', 'w') as outfile:
        json.dump(data[i:i+chunkSize], outfile)

