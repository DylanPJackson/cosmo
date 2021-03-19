"""
	filename
		prioritization_function_test.py

	description
		Currently just testing grounds to implement the prioritization function
		and the accompanying knapsack algorithm.

	author
		Dylan P. Jackson (original contributor)
"""

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
	

