from get_data import get_child
from api_settings import api_key

def get_table_child():
    data = get_child('http://api.data.mos.ru/v1/datasets/2009/rows?API_KEY={}'.format(api_key))
    result = '''
                <b>Сведения о наиболее популярных женских именах среди новорожденных</b>
                <table>
                    <tr>
                         <th> ID </th>
                         <th> Имя </th>
                         <th> Кол - во человек </th>
                         <th> Год </th>
                         <th> Месяц </th>
                    </tr>'''
    for row in data:
        number = row['Number']
        name = row['Cells']['Name']
        cnt = row['Cells']['NumberOfPersons']
        year = row['Cells']['Year']
        month = row['Cells']['Month']
        result += '''
                <tr>
                    <td>{Number}</td>
                    <td>{Name}</td>
                    <td>{NumberOfPersons}</td>
                    <td>{Year}</td>
                    <td>{Month}</td>
                 </tr>

            '''.format(Number=number, Name=name, NumberOfPersons=cnt, Year=year, Month=month)
    result += '</table>'
    return result