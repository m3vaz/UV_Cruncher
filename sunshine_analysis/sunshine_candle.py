import csv
import warnings

# if we're not running this as a script and importing it, we want the debug features
if __name__ != '__main__':
	debug_mode = True
else:
	debug_mode = False

# The university names are not consistent, so we need to normalize them so we can
# do the comparison between years
# This is the conversion chart. It also includes federated colleges as
# their overarching university (Trinity College -> University of Toronto)		
name_rep = {
	'Brock University': 'Brock University',
	'Carleton University': 'Carleton University',
	'Lakehead University': 'Lakehead University',
	'Laurentian University': 'Laurentian University',
	'McMaster University': 'McMaster University',
	'Nipissing University': 'Nipissing University',
	'Queen\'s University at Kingston' : 'Queen\'s University',
	'Ryerson Polytechnic University': 'Ryerson University',
	'The University of Western Ontario': 'University of Western Ontario',
	'Trent University': 'Trent University',
	'University of Guelph': 'University of Guelph',
	'University of Ottawa': 'University of Ottawa',
	'University of St. Jerome\'s College': 'University of Waterloo',
	'University of Toronto': 'University of Toronto',
	'University of Waterloo': 'University of Waterloo',
	'University of Windsor': 'University of Windsor',
	'Wilfrid Laurier University': 'Wilfrid Laurier University',
	'York University': 'York University',
	'Algoma Univ. College': 'Algoma University',
	'Brock': 'Brock University',
	'Carleton': 'Carleton University',
	'Guelph': 'University of Guelph',
	'Lakehead':'Lakehead University',
	'Laurentian': 'Laurentian University',
	'McMaster': 'McMaster University',
	'Nipissing': 'Nipissing University',
	'Ont. College of Art & Design': 'Ontario College of Art & Design',
	'Ottawa': 'University of Ottawa',
	'Queen\'s': 'Queen\'s University',
	'Ryerson Polytechnic': 'Ryerson University',
	'Toronto': 'University of Toronto',
	'Trent': 'Trent University',
	'Waterloo': 'University of Waterloo',
	'Western Ont.': 'University of Western Ontario',
	'Wilfrid Laurier': 'Wilfrid Laurier University',
	'Windsor': 'University of Windsor',
	'York': 'York University',
	'Ontario College of Art & Design': 'Ontario College of Art & Design',
	'Queen\'s University': 'Queen\'s University',
	'University of Western Ontario': 'University of Western Ontario',
	'Huntington University': 'Laurentian University',
	'King\'s College': 'University of Western Ontario',
	'Ont.Coll.of Arts & Design': 'Ontario College of Art & Design',
	'Trinity College': 'University of Toronto',
	'Victoria University': 'University of Toronto',
	'Algoma University':'Algoma University',
	'Algoma University College':'Algoma University',
	'Contact North/Contact Nord': 'Contact North',
	'Ontario College for Art & Design': 'Ontario College of Art & Design',
	'Ryerson University': 'Ryerson University',
	'Brescia University College': 'University of Western Ontario',
	'University of Ontario Institute of Technology': 'University of Ontario Institute of Technology',
	'King\'s University College': 'University of Western Ontario',
	'Universit\xe9 de Hearst':'Universit\xe9 de Hearst',
	'University of Ontario Inst. ofTech.': 'University of Ontario Institute of Technology',
	"Northern Ontario School of Medicine":"Northern Ontario School of Medicine",
	'St. Michael\'s College': 'University of Toronto',
	'University of Ontario\xa0Inst.\xa0ofTech.': 'University of Ontario Institute of Technology',
	'Queen\'s Theo. Col. at Queen\'s Univ.': 'Queen\'s University',
	"University of Ontario Institute of Tech.": 'University of Ontario Institute of Technology',
	"University of St. Michael's College": "University of Toronto",
	'Queen\'s Theological College, Queen\'s University': 'Queen\'s University',
	'Huron University College': 'University of Western Ontario',
	'Laurentian University of Sudbury': 'Laurentian University',
	'Queen\'s Theological College': 'Queen\'s University',
	'University of Sudbury': 'Laurentian University',
	'Ontario College of Art & Design University': 'Ontario College of Art & Design',
	'Queen\'s School of Religion': 'Queen\'s University',
	'Coll\xe8ge de Hearst': 'Universit\xe9 de Hearst',
	'McMaster Divinity College':'McMaster University',
	'St. Peter\'s Seminary':'University of Western Ontario',
	'Thorneloe University':'Laurentian University',
	'Universit\xe9 d\'Ottawa / University of Ottawa': 'University of Ottawa',
	'Universit\xe9 Saint-Paul / Saint Paul University': 'University of Ottawa',
	'Saint Paul University / Universit\xe9 Saint-Paul': 'University of Ottawa'
}


lines = []

if debug_mode:
	school_names = []
	new_school_names = []
	
for year in range(1996, 2015):
	with open('originals/'+str(year)+'-sunshine.csv', 'rb') as file, open(str(year)+'-sunshine.csv', 'wb') as fixed_file:
	
		reader = csv.reader(file)
		writer = csv.writer(fixed_file)
		lines = []
		
		for row in reader:
			lines.append(row)
		
		for row in lines:
			# skip over blank rows
			if row[0] == '' or row[0].isspace():
				continue
				
			if debug_mode and school_names.count(row[0]) == 0:
				school_names.append(row[0])
				
			if name_rep.has_key(row[0]):
				row[0] = name_rep[row[0]]
				
			if debug_mode and new_school_names.count(row[0]) == 0:
				new_school_names.append(row[0])
				
			writer.writerow(row)
			
			
		file.close()
		fixed_file.close()
		

# School names normalized
# We want to track the progress of people in a single school over the years

