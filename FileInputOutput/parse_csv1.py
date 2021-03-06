import csv

with open('Create-name.csv', 'r')as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open('save_names.csv', 'w')as new_file:
		fieldnames = ['id','first_name', 'last_name']

		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

		csv_writer.writeheader()

		for line in csv_reader:
			del line['email']
			csv_writer.writerow(line)