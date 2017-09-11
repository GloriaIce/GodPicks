import random

def pick_food(locations):
	locations_utf8 = []
	food_list = []
	for location in locations:
		location = location.encode("utf-8")
		locations_utf8.append(location)
		food_list += [line.strip() for line in open(("data/" + location + ".txt"), 'r')]
	print food_list
	restaurant = food_list[random.randint(0, len(food_list) - 1)]
	return restaurant, len(food_list)

def pick_activity():
	activities = [line.strip() for line in open(("data/activity.txt"), 'r')]
	activity = activities[random.randint(0, len(activities) - 1)]
	return activity