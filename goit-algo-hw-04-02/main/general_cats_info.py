def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(",")
                cat_info = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
                cats_info.append(cat_info)
    except FileNotFoundError:
        print (f'File {path} not found')
    except Exception as e:
        print(f"Error: {e}")

    return cats_info


cats_info = get_cats_info("C:\\Users\\Danik\\Desktop\\python\\goit-algo-hw-04-02\\main\\cats_info.txt")
print(cats_info)


