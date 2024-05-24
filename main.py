#imports
import random
import os
import json
from comparison import error_of_tolerance
from utils import delay
# all modules

os.environ['TERM'] = 'xterm'

file_path = 'biology.json'
print('Flashcard Program')
flash_card = {
    'question': '',
    'answer': '',
    'show_answer': False, # default do not show answer. clicking True shows the answer with the question.
    'show_timer': False, # default do not show timer thus unlimited time for practising,vice versa.
    'secs_to_show': 15, # 15 secs for the timer to end. links to the show_timer
    'score': 0.0 # percentage * 0.7 + (1.0 - secs_to_show * 0.05) * 0.3
}
flash_card_list = []
#
with open(file_path, 'r') as file: #r means reading, w is writing, a is append,
    flash_card_list = json.load(file)
#
while True:
    os.system('clear')
    current_card = random.choice(flash_card_list)
    print(current_card['question'])
    user_answer = input('your answer:')
    if user_answer == 'exit':
        break
    difference = error_of_tolerance(current_card['answer'], user_answer)
    print(f'wrongness: {difference}%')
    if user_answer == current_card['answer']:
        print("absolutely correct!")
    elif difference <= 5:
        print('almost 100%')
    else:
        print('wrong!')
    delay()

with open(file_path, 'w') as file:
    json.dump(obj = flash_card_list, fp = file, indent=4)