import random
print('Flashcard Program')
flash_card = {
    'question': '',
    'answer': '',
    'show_answer': False,
    'show_timer': False,
    'secs_to_show': False,
    'score': 0.0 # percentage * 0.7 + (1.0 - secs_to_show * 0.05) * 0.3
}
flash_card_list = [flash_card.copy(), flash_card.copy(), flash_card.copy()]
flash_card_list[-1]['question'] = 'why everything change?'
for c in flash_card_list:
    print(c)
    print(id(c))