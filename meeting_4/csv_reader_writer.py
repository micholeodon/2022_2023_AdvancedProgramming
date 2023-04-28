import csv

# The script creates a new file with the data from data.csb file, but
# expanded with a new column containing areas of the rectange with sides a and b.

with open('data.csv','r') as csvinput:
    with open('data_out.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        newData = []
        row = next(reader)
        row.append('P') # adds header of the column
        newData.append(row) 

        # reads subsequent rows and adds new element at the end then writes to the file
        for row in reader:
            a = float(row[0])
            b = float(row[1])
            P = a*b
            row.append(P)  
            newData.append(row)

        writer.writerows(newData)
