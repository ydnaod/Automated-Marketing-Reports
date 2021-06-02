import ezsheets

#import velocify spreadsheet with new leads
ss2 = ezsheets.Spreadsheet('1Kge5EN5QRJiPswN9pyGzY3dBNbWQJn2rcVX41_T3jpQ')
leads = ss2[0]
rows = leads.getRows()
columns = leads.getColumns()

#Deletes bad leads
for row in rows:
    for number in row:    
        if rows[rows.index(row)][4] == 'Bad Lead' or rows[rows.index(row)][4] == 'Duplicate' or rows[rows.index(row)][4] == 'Test Lead' or rows[rows.index(row)][4] == 'Salon Services':
            #print(row)
            num = rows.index(row)
            rows.pop(num)
            rows.insert(num, [])
            break

#Updates rows
leads.updateRows(rows)
columns = leads.getColumns()
#Clears blank rows
for row in rows:
    if rows[rows.index(row)][0] == '':
        num = rows.index(row)
        rows.pop(num)

#Updates rows
leads.updateRows(rows)
columns = leads.getColumns()
