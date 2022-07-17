import os.path
import xlwt


# title 标题[{name:'', title:''}]
# data: 导出的数据[{},{}]
def export(title=[], data=[], filePath=''):

    ws = xlwt.Workbook(encoding='utf8')
    sheet1 = ws.add_sheet('sheet1')

    title_len = len(title)
    for i in range(title_len):
        t_i = title[i]
        sheet1.write(0, i, t_i['title'])

    row_index = 1
    for row in data:
        for col_index in range(title_len):
            key = title[col_index]['name']
            sheet1.write(row_index, col_index, row[key])
        row_index += 1

    if not filePath.endswith('.xls'):
        filePath += '.xls'

    exists = os.path.exists(filePath)
    if exists:
        os.remove(filePath)

    ws.save(filePath)

