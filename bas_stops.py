# Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок, вывести улицу, на которой больше всего остановок

import csv
count_stops = 0
count_distinct_stop = 0
list_street = []
count_streets = {}
group_street = {}
with open('..\\data_bas_stop\\data-398-2018-05-25.csv', 'r', encoding='cp1251', newline='') as f:
    fields = ['ID','Name','Longitude_WGS84','Latitude_WGS84','Street','AdmArea','District','RouteNumbers','StationName',
              'Direction','Pavilion','OperatingOrgName','EntryState','global_id','geoData']
    reader = csv.DictReader(f, fields, delimiter=';')

    for row in reader:
        count_stops += 1
        list_street.append(row['Street'])
    for street in list_street:
        count_streets[street] = count_streets.get(street,0)+1
    group_street = {distinct_street: count for distinct_street, count in count_streets.items() if count > 1}
    dist_street = list(group_street.keys())
    count = list(group_street.values())
    count_distinct_stop = dist_street[count.index(max(count))]
    print(count_distinct_stop,count.index(max(count)))
    print('Количество остановок: ', count_stops)
