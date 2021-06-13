import os
import hashlib
from datetime import datetime

def hash_file(filename):
   h = hashlib.sha256()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()

def generate(file_list, name, new_name):
    for item in file_list:
        if item.startswith(name):
            os.rename('./styles/' + item, './styles/' + new_name)
    return

def insertHTML():
    return


files = os.listdir('./styles')

hash_data_file = open("./hashcode", 'r+')

current_date = datetime.date(datetime.now()).strftime("%Y-%m-%d")

old_hashes = hash_data_file.read().split('\n')
new_hashes = []

for item in files:
    if item.endswith('.css'):
        new_file_hash = hash_file('./styles/' + item)
        name = item.rstrip('.css').split('?', 1)[0]
        new_hashes.append(name + ':' + new_file_hash)

for old_item in old_hashes:
    old_items = old_item.split(':')
    for new_item in new_hashes:
        new_items = new_item.split(':')
        if old_items[0] == new_items[0]:
            if old_items[1] != new_items[1]:
                old_items[1] = new_items[1]
                new_file_name = old_items[0] + '?' + current_date + '.css'
                generate(files, old_items[0], new_file_name)
                insertHTML()

hash_data_file.seek(0, 0)
for item in new_hashes:
    hash_data_file.write(item)
    if new_hashes.index(item) == len(new_hashes) - 1:
        break
    else:
        hash_data_file.write('\n')

hash_data_file.close()
print(old_hashes)
print(new_hashes)

