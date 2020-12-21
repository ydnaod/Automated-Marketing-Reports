import ezsheets

#import velocify spreadsheet with new leads
ss2 = ezsheets.Spreadsheet('1t4fH8YRdX19Z2jcCgpPw_MOOQX6egrG9rWgJa_Jzrdg')
leads = ss2[0]
rows = leads.getRows()
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

#Creates new clean programs column
columns[10] = ['Program']

programsClean = ['Program']

validRows = totalRows - invalidRows

programs = columns[8]
cosWords = ['Cosmetology', 'cosmetology', 'Barber Training', 'All Beauty Courses', 'Cos', 'Cosmetololgy', 'Barber Workshop', 'Barber Workshops']
skinWords = ['Esthetics/Skin Care', 'Esthetics', 'esthetics', 'Esthetcs', 'ESTHETICS']
nailWords = ['Nail Technology', 'Nail', 'Nail Technician', 'Nails', 'nails', 'NAILS']
otherWords = ['Teacher Training', 'Teacher Program', 'Advanced Classes', '']
makeupWords = ['Makeup Training', 'Make-Up Artist Training', 'Makeup', 'Make-up Workshops', 'MUD only']
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