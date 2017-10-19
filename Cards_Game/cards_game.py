# -*- coding:utf-8 -*-
#2017/10/19 10:00
#version1.0

'''
    cards game
'''
import random

sample = random.sample

cards_color = ['红桃','方片','黑桃','梅花']
cards_number = ['3', '4', '5', '6', '7', '8', '9','10','J','Q','K','A','2']
cards_privilege = ['大王','小王']
all_cards = []

for color in cards_color:
    for number in cards_number:
        all_cards.append(color + number)
for privilege in cards_privilege:
    all_cards.append(privilege)

user1 = sample(all_cards,17)
print(sorted(user1))

for cards in user1:
    all_cards.remove(cards)
all_cards_left1 = all_cards
user2 = sample(all_cards_left1,17)
print(sorted(user2))

for cards in user2:
    all_cards_left1.remove(cards)
all_cards_left2 = all_cards_left1
user3 = sample(all_cards_left2,17)
print(sorted(user3))






