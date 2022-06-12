dict_print = {
    'склад': 
        {'HP LaserJet': ['100', 'принтер', 'high', 'сетевой'], 'Xerox WorkCentre': ['200', 'ксерокс', 'medium', 'А4']}, 
    'адм': 
        {'Xerox WorkCentre': ['300', 'ксерокс', 'medium', 'А4'], 'HP ScanJet': ['400', 'сканер', 'medium', '600dpi']}, 
    'отдел': 
        {'HP LaserJet': ['500', 'принтер', 'high', 'сетевой']}, 'Xerox WorkCentre': ['600', 'ксерокс', 'medium', 'А4']
    }

j = 0
for i in dict_print:
    j+=1
    print(f"{j}-я итерация:")
    print("i = ", i)
    print(f"dict_print.get({i}) = ", dict_print.get(i))

