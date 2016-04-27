import jsonpickle

skills_table = None

def get():
	global skills_table
	if skills_table == None:
		with open('../resources/skills.json', 'r') as f: #TODO path resolve
			json_str = f.read()
			skills_table = jsonpickle.decode(json_str)   
		
	return skills_table

def save():
	if skills_table != None:
		with open('../resources/skills.json', mode='w') as f: #TODO path resolve
			jsonpickle.set_encoder_options('json', sort_keys=True, indent=2)
			json_str = jsonpickle.encode(skills_table)
			f.write(json_str)

def add_skill(skill):
	global skills_table

	if skills_table == None:
		skills_table = {}
	
	skills_table[skill.name] = skill
	
class Skill(object):
	def __init__(self, name):
		self.name = name
		self.requirments = {}
		add_skill(self)