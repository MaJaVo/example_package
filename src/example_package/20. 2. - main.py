
import sys

class Person:
    def __init__(self, name:str, salary:float):
        self.__name = name
        self.__salary = salary

def load_data_file(filepath: str, wanted_year: int, limit):
    #print("ahoj")
    data = []
    with open(filepath, "r", encoding="utf8") as fd:

        for i,line in enumerate(fd):
            if i == 0:
                continue
            #'id;pohlaví;jméno;přijmení;adresa;město;stát;narození;věk;krevní skupina;váha;výška;rok;odvětví;průměrný plat\n'

            if i==limit:
                break
            
            fields = line.split(";")

            year = fields[12]
            if year != str(wanted_year):
                continue

            name = fields[2]
            salary = fields[14]

            p = Person(name, float(salary))
            data.append(p)

    return data

def count_average_salary(data: list[Person]):
    sum = 0
    for p in data: #for each
        sum += p.salary
    return sum / len(data)

def get_value(p:Person):
    return p.salary

def count_median_salary(data: list[Person]):
    sorted_data = sorted(data, key=get_value)
    return sorted_data[len(sorted_data)/2]
    


def main(input_path: str):
    print("nacitame data z {input_path}")
    data_2014 = load_data_file(input_path, 2014, 1000)
    data_2015 = load_data_file(input_path, 2015, 1000)

    print(f"nacetli jsme {len(data_2014)} zaznamu") #f umožňuje {len(data)}

    #print(data_2014[:3]) #[:3] vytiskne pouze první tři záznamy

    data14 = count_average_salary(data_2014)
    print(f"prumerny plat v datech 2014: {data14}")

    data15 = count_average_salary(data_2015)
    print(f"prumerny plat v datech 2014: {data15}")

    print(f"rozdil je: {data15-data14}")

    # data15 = count_average_salary(load_data_file(input_path, 2015))
    # print(data14, data15)

    
    year = None
    data = None
    avg = count_average_salary(data)
    print(f"Průměrný plat v roce {year}  je  {avg}")

    median = count_median_salary(data)
    #print(f"Medián v roce {year}  je  {median}")


if __name__ == '__main__':
    #data_path = None
    sys.argv = ["main.py", "C:/Program Files (x86)/Škola/FAV - škola/Python/ADT/soubory/data-salaries-years-11M.csv"]
    data_path = "C:/Program Files (x86)/Škola/FAV - škola/Python/ADT/soubory/data-salaries-years-11M.csv"
    main(data_path)
