import xlsxwriter
from Parsing import array


def write(parametr):
    book = xlsxwriter.Workbook("C:\\Users\\user\\Desktop\\backand\\Parsing\\Table.xlsx")
    page = book.add_worksheet("товар")
    
    row = 0
    column = 0
    
    page.set_column("A:A", 20)
    page.set_column("A:B", 20)
    page.set_column("A:C", 20)
    page.set_column("A:D", 20)
    
    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column, item[2])
        page.write(row, column, item[3])
        row+=1
    book.close()

write(array)