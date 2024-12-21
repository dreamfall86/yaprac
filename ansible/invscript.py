import json
import os

# Шаг 1: Загрузка данных из terraform_output.json
with open('../terraform/terraform_output.json') as f:  # Путь относительно директории с Python-скриптом
    terraform_output = json.load(f)

# Шаг 2: Формирование структуры инвентаря
inventory = {
    "all": {
        "children": {
            "nginx": {
                "hosts": {}
            },
            "proxy": {
                "hosts": {}
            }
        }
    }
}

private_key = "/home/dream/.ssh/git"  # Укажите путь к приватному ключу

# Шаг 3: Заполнение данных для каждой группы
for host, ip in terraform_output.items():
    if "proxy" in host:
        inventory["all"]["children"]["proxy"]["hosts"][host] = {
            "ansible_host": ip,
            "ansible_user": "root",
            "ansible_ssh_private_key_file": private_key,
            "ansible_ssh_common_args": "-o StrictHostKeyChecking=no"

        }
    elif "nginx" in host:
        inventory["all"]["children"]["nginx"]["hosts"][host] = {
            "ansible_host": ip,
            "ansible_user": "root",
            "ansible_ssh_private_key_file": private_key,
            "ansible_ssh_common_args": "-o StrictHostKeyChecking=no"

        }

# Шаг 4: Сохранение инвентаря в файл JSON
inventory_dir = '../ansible'  # Директория, куда сохраняем инвентарь
inventory_file_path = os.path.join(inventory_dir, 'inventory.json')  # Путь к файлу

# Сохраняем инвентарь в файл
with open(inventory_file_path, 'w') as f:
    json.dump(inventory, f, indent=4)

# Выводим сообщение о завершении
print(f"Инвентарь для Ansible был успешно создан и сохранен в {inventory_file_path}")

