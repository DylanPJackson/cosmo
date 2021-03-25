"""
	filename
		prioritization_function_test.py

	description
		Currently just testing grounds to implement the prioritization function
		and the accompanying knapsack algorithm.

	author
		Dylan P. Jackson (original contributor)
"""
import numpy as np

class Reminder:
	"""
		Basic class to encapsulate the data for a Reminder as it is stored 
		in the universe database
	"""
	def __init__(self, r_id, description, expiration, complete_time, creation_date):
		self.r_id = r_id
		self.description = description
		self.expiration = expiration
		self.complete_time = complete_time
		self.creation_date = creation_date
	
def prioritize(reminders):
	"""
		Generates value for each reminder based off of their expiration and
		creation dates

		Parameters
		----------
		reminders : list<Reminder>
		
		Returns
		-------
		dict<int (r_id) : int (priority)>
			Dictionary mapping reminder_id to their priority
	"""
	
	"""
		What we're actually going to do
		- Take in a list of reminders as input, and that's it
		- Make hash table which maps reminder ID to priority value
		- Make two lists, each with Reminder ID and creation date / expiration date respectively
		- Sort those two lists based off of the dates
		- Calculate the priority based off of these sorted values
		- Put priorities into hash table, associated with ID's
		- Return hash table?
	"""
	# Dictionary mapping reminder_id's to their priorities
	priorities = {}
	# 2d list of reminder_id and expiration date 
	expirations = []
	# 2d list of reminder_id and creation date 
	creations = []
	
	# Initialize each data structure
	for reminder in reminders:
		r_id = reminder.r_id
		exp = reminder.expiration
		cre = reminder.creation_date

		priorities[r_id] = 0
		expirations += [[r_id, exp]]
		creations += [[r_id, cre]]

	# Sort expiration and creation lists by their exp and cre dates 
	expirations.sort(key = lambda x:x[1], reverse = True)
	print("Expirations : " + str(expirations))
	creations.sort(key = lambda x:x[1])
	print("Creations: " + str(creations))
	
	# Calculate priorities
	num_priorities = len(expirations)
	for i in range(1, num_priorities + 1):
		# Get expiration / creation ID's
		exp_id = expirations[i-1][0]
		cre_id = creations[i-1][0]
		# Calculate weight for each
		exp_value = .8 * i
		cre_value = .2 * i
		# Update weight for that ReminderID
		priorities[exp_id] = priorities[exp_id] + exp_value
		priorities[cre_id] = priorities[cre_id] + cre_value
	
	return priorities

def main():
	# Lets create some reminders
	reminder_1 = Reminder(1, "dog", 2, 6, 1)
	reminder_2 = Reminder(2, "cat", 8, 4, 3)
	reminder_3 = Reminder(3, "wolf",1, 12, 2)
	reminder_4 = Reminder(4, "shark", 9, 4, 10)
	reminders = [reminder_1, reminder_2, reminder_3, reminder_4]
	p = prioritize(reminders)
	print(p)



main()
