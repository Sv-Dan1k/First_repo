def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_salary = 0 
            for line in lines:
                current_salary = line.split(",")[1]
                total_salary += int(current_salary)
            average_salary = total_salary // len(lines)
            return total_salary, average_salary
    except FileNotFoundError:
        print (f'File {path} not found')
    except Exception:
        print ('Error')

total, average = total_salary ("C:\\Users\\Danik\\Desktop\\python\\goit-algo-hw-04\\general\\salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")