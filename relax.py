graph = {
    "employees": 4,
    "vacations": [
        {"name": "Aiko", "day": "30","month":"December"},
        {"name": "Uldana", "day": "01","month":"July"},
        {"name": "Kairat", "day": "25","month":"Novembergit"},
    ]
}
day_s=str(input("Введите день отпуска: "))
for vacation in graph["vacations"]:
    if day_s in vacation["day"]:
        print(vacation["name"],end=" ")
        
# month_s = "September"
# for vacation in graph["vacations"]:
#     if month_s in vacation["month"]:
#         print(vacation["name"], end=" ")



