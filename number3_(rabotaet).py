def format(data):
    '''
    converts data into data separated by rows and elements per row.
    data = initial data
    '''
    table = []
    data = data.split("\n")
    for i in range(len(data)):
        row = data[i]
        row = row.split(";")
        if len(row)==5:
            [salary, work, size, role, company] = row
            salary = int(salary)
            work = work
            size = int(size)
            role = role
            company = str(company)
            row = [salary, work, size, role, company]
        table.append(row)

    return table

def to_csv_string(raw):
    '''
    transform arrive to csv string.
    raw = array of data in the format string
    '''
    for i in raw:
        string = ";".join(i) + "\n"
    return string

with open("vacancy.csv", "r", encoding = "utf8") as F:
    header = F.readline()
    dataset = F.read()

usable_data = format(dataset)

print("Введите название компании:")
ask = str(input())
if ask[0]== " ":
    ask = ask[1:]
while ask != "None":
    flag = 0
    for row in usable_data:
        [salary, work, size, role, company] = row
        if company == ask or company == " " + ask:
            print(f"В {company} найдена вакансия: {role}. З/п составит: {salary}")
            flag = 1
            break
    if flag == 0:
        print("К сожалению, ничего не удалось найти")
    print("Введите название компании:")
    ask = str(input())



        
