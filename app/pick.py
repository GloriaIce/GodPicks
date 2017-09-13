 # -*- coding: utf-8 -*-
import random
import os

def pick_food(locations):
	locations_utf8 = []
	food_list = []
	for location in locations:
		location = location.encode("utf-8")
		locations_utf8.append(location)
		with open(os.path.join('data', '%s.txt' % location), 'rU') as f:
			for line in f:
				print line
				food_list.append(line.strip())
	for food in food_list:
		print food
	restaurant = random.choice(food_list)
	return restaurant, len(food_list)

def pick_activity():
	activities = []
	with open(os.path.join('data', 'activity.txt'), 'rU') as f:
			for line in f:
				print line
				activities.append(line.strip())
	activity = random.choice(activities)
	return activity