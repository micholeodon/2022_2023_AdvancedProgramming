import csv

N = int(input('How many records?\n'))

with open('movies.csv', 'w') as file:
    csvWriter = csv.writer(file, delimiter=',')

    # header
    csvWriter.writerow(['No.','Title','Rating'])
    
    # rows
    for i in range(N):
        title = input('Movie title:')
        rating = float(input('Rating (0.0 - 10.0):'))
        row = [str(i+1), title, rating]

        csvWriter.writerow(row)
