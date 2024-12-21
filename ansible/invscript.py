import json
import os

# Шаг 1: Загрузка данных из terraform_output.json
with open('~rep/yaprac/terraform/terraform_output.json') as f:  # Путь относительно директории с Python-скриптом
    terraform_output = json.load(f)

inventory = {
    "all": {
        "hosts": list(terraform_output.keys()),
        "vars": {}
    },
    "_meta": {
        "hostvars": {
            vm: {
                "ansible_host": ip,
                "ansible_user": "root" 
            } for vm, ip in terraform_output.items()
        }
    }
}

# Шаг 3: Сохранение инвентаря в файл JSON для Ansible
inventory_file_path = os.path.join(os.getcwd(), 'inventory.json')  # Путь будет внутри директории с Ansible-скриптом

with open(inventory_file_path, 'w') as f:
    json.dump(inventory, f, indent=4)

print(f"Инвентарь для Ansible был успешно создан и сохранен в {inventory_file_path}")

