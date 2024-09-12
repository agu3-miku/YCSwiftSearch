import os
import difflib

def read_data(file_path):
    # 读取文件内容并解析为数据列表
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('，', maxsplit=1)  # 假设名称和位置之间以'，'分隔
            if len(parts) == 2:
                data.append({'name': parts[0], 'location': parts[1]})
    return data

def write_data(file_path, data):
    # 将数据列表写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item['name']}，{item['location']}\n")

def add_data(data, name, location):
    # 向数据列表中添加新数据
    data.append({'name': name, 'location': location})

def update_data(data, name, new_location):
    # 更新数据列表中指定名称的位置信息
    for item in data:
        if item['name'].lower() == name.lower():  # 不区分大小写
            item['location'] = new_location
            return True
    return False

def find_data(data, name):
    # 查找数据列表中指定名称的数据
    for item in data:
        if item['name'].lower() == name.lower():  # 不区分大小写
            return item
    return None

def delete_data(data, name):
    # 删除数据列表中指定名称的数据
    for item in data:
        if item['name'].lower() == name.lower():  # 不区分大小写
            data.remove(item)
            return True
    return False

def export_data(file_path, data):
    # 导出数据到指定文件
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item['name']}，{item['location']}\n")

def import_data(file_path):
    # 从指定文件导入数据
    return read_data(file_path)

def find_similar_names(data, name):
    # 查找与输入名称相似的名称
    names = [item['name'] for item in data]
    close_matches = difflib.get_close_matches(name, names, n=3, cutoff=0.6)
    return close_matches

def main():
    # 主函数，处理用户输入并执行相应操作
    file_path = r"C:\\YCSS\\data.txt"  # 使用原始字符串避免转义字符问题
    export_path = r"C:\\YCSS\\export.txt"

    # 读取数据
    data = read_data(file_path)
    print("数据读取完成")

    # 修改、添加、查找、删除或导出数据
    while True:
        action = input("请输入操作（add/update/find/delete/export/import/save/exit）：")
        if action == 'exit':
            break

        if action == 'add':
            name = input("请输入名称：")
            location = input("请输入位置：")
            add_data(data, name, location)
            print("数据已添加")

        elif action == 'update':
            name = input("请输入要更新的名称：")
            new_location = input("请输入新的位置：")
            if update_data(data, name, new_location):
                print("数据已更新")
            else:
                print("未找到相关数据")

        elif action == 'find':
            name = input("请输入要查找的名称：")
            found_item = find_data(data, name)
            if found_item:
                print(f"找到数据：名称={found_item['name']}, 位置={found_item['location']}")
            else:
                similar_names = find_similar_names(data, name)
                if similar_names:
                    print("没有该物品或物品未纳入数据库，但找到以下类似名称：")
                    for similar_name in similar_names:
                        print(similar_name)
                else:
                    print("没有该物品或物品未纳入数据库")

        elif action == 'delete':
            name = input("请输入要删除的名称：")
            if delete_data(data, name):
                print("数据已删除")
            else:
                print("未找到相关数据")

        elif action == 'export':
            export_data(export_path, data)
            print("数据已导出到export.txt")

        elif action == 'import':
            imported_data = import_data(export_path)
            print("导入的数据如下：")
            for item in imported_data:
                print(f"名称={item['name']}, 位置={item['location']}")
            confirm = input("确认无误后输入'confirm'以保存到data.txt：")
            if confirm == 'confirm':
                data = imported_data  # 将导入的数据赋值给data
                write_data(file_path, data)
                print("数据已保存到data.txt")
            else:
                print("导入操作已取消")

        elif action == 'save':
            write_data(file_path, data)
            print("数据已保存")

    # 写入数据
    write_data(file_path, data)
    print("数据已更新并保存")

if __name__ == "__main__":
    main()
