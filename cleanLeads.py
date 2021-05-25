import ezsheets

#import Lead Report Sheer (test)
leadReport = ezsheets.Spreadsheet('1YjeVMNeHdolHye-RBU3tgzEYBRRbMTXPPGAoydumWVg')

#import velocify spreadsheet with new leads
ss2 = ezsheets.Spreadsheet('17it5xHPb_-mQn8XeuZ-dZJ7Vvox4i8G0NMhPklL4j20')
leads = ss2[0]
rows = leads.getRows()

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

#Moves columns over by 1
zip = columns[13]
phone2 = columns[12]
phone1 = columns[11]
email = columns[10]

leads.updateColumn(15, zip)
leads.updateColumn(14, phone2)
leads.updateColumn(13, phone1)
leads.updateColumn(12, email)
columns = leads.getColumns()

#trims rows
invalidRows = 0
for row in rows:
    if rows[rows.index(row)][0] == '':
        invalidRows += 1

totalRows = leads.rowCount
leads.rowCount = totalRows - invalidRows

#inserts placeholder text so it doesn't get deleted
columns[10] = ['Program']

#clears blank columns
for column in columns:
    if columns[columns.index(column)][0] == '':
        num = columns.index(column)
        columns.pop(num)

#trims columns
invalidColumns = 0
for column in columns:
    if columns[columns.index(column)][0] == '':
        invalidColumns += 1

totalColumns = leads.columnCount
leads.columnCount = totalColumns - invalidColumns

#Creates new clean programs column
columns[10] = ['Program']

programsClean = ['Program']

validRows = totalRows - invalidRows

programs = columns[8]
cosWords = ['Cosmetology', 'cosmetology', 'Barber Training', 'All Beauty Courses', 'Cos', 'Cosmetololgy', 'Barber Workshop', 'Barber Workshops', 'Barbering', 'cosmetlogy']
skinWords = ['Esthetics/Skin Care', 'Esthetics', 'esthetics', 'Esthetcs', 'ESTHETICS', 'esthetic']
nailWords = ['Nail Technology', 'Nail', 'Nail Technician', 'Nails', 'nails', 'NAILS', 'nail', 'nail tech']
otherWords = ['Teacher Training', 'Teacher Program', 'Advanced Classes', "Teacher's Program", "Cosmetology Teacher", '']
makeupWords = ['Makeup Training', 'Make-Up Artist Training', 'Makeup', 'Make-up Workshops', 'MUD only', 'makeup', 'MUD']
i=0
for entry in programs:
    if i < validRows:
        for x in cosWords:
            if entry == x:
                programsClean.append('Cosmetology')
        for x in skinWords:
            if entry == x:
                programsClean.append('Esthetics')
        for x in nailWords:
            if entry == x:
                programsClean.append('Nails')
        for x in otherWords:
            if entry == x:
                programsClean.append('Other')
        for x in makeupWords:
            if entry == x:
                programsClean.append('Makeup')
        i += 1   

columns[10] = programsClean

#Updates columns
leads.updateColumns(columns)


#moves Last week to 2 Week compressor
leadReport = ezsheets.Spreadsheet('1tCZLsVJ-tEz-5XF6SUpVGq--_SfGTSMvhHTFXlxAOpU')
lastWeekCompressor = leadReport[5]
twoWeekCompressor = leadReport[6]

lastWeekColumns = lastWeekCompressor.getColumns()
date = lastWeekColumns[16]


twoWeekColumns = twoWeekCompressor.getColumns()
