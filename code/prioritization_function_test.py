import numpy as np

class Reminder:
	"""
		Basic class to encapsulate the data for a Reminder as it is stored 
		in the universe database
	"""
	def __init__(self, description, expiration, complete_time, creation_date):
		self.description = description
		self.expiration = expiration
		self.complete_time = complete_time
		self.creation_date = creation_date

def prioritize(num_r, exp_dates, cre_dates):
	"""
		Generates value for each reminder based off of their expiration and
		creation dates

		Parameters
		----------
		num_r : int
			The number of reminders at the moment
		exp_dates : list<(id, datetime)>
			The expiration dates associated with each reminder
		cre_dates : list<(id, datetime)>
			The creation dates associated with each reminder
		
		Returns
		-------
		list<(id, int)>
			The prioritized value of each reminder
	"""
