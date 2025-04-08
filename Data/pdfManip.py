import tabula

f = tabula.read_pdf(r'D:\Cerc Info\teme python\LMI Import Tool\Data\LMI2015.pdf', pages = 'all')[0]

f.to_csv('data')