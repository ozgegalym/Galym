# пример словаря country_rivers
country_rivers = {
    "Казахстан": ["Жайык", "Есил", "Ертис"],
    "США": ["Миссисипи", "Колорадо"],
    "Китай": ["Желтая", "Янцзы", "Меконг"],
    "Бразилия": ["Амазонка", "Сан-Франсиско"],
    "Канада": ["Маккензи", "Сен-Лоуренс"],
}

# # # список названий рек для проверки и добавления
# river_names = ["Есил", "Днепр", "Жайык"]

# # 1. для каждой реки указать, в какой стране она протекает
# for river in river_names:
#     found = False
#     for country, rivers in country_rivers.items():
#         if river in rivers:
#             print(f"Река {river} протекает в стране {country}")
#             found = True
#     if not found:
#         print(f"Река {river} не найдена в словаре.")

# # 2. проверить, есть ли введенное название реки в словаре
# for river in river_names:
#     found = False
#     for rivers in country_rivers.values():
#         if river in rivers:
#             found = True
#             break
#     if found:
#         print(f"Река {river} найдена в словаре.")
#     else:
#         print(f"Река {river} не найдена в словаре.")

# 3. добавить новую пару страна-река в словарь
# country_rivers["Украина"] = ["Днепр"]
# print(country_rivers)
