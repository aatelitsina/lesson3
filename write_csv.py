import csv

ans=[{"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"},{"что задали": "Не знаю", "кто знает": "Рома", "спасибо": "Пжл"}]
fields = list()
ians=0
while ians < len(ans):
    for key in ans[ians].keys():
            fields.append(key)
    ians+=1
with open('question_answer.csv', 'w', encoding='utf-8') as f:
    write = csv.DictWriter(f, fields, delimiter=';')
    write.writeheader()
    for itr in ans:
        write.writerow(itr)
