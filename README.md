# yaprac
ansible+terraform

- Для начала работы необходимо запустить скрипт startscript в директории terraform, он развернёт инфраструктуру и запустит скрипт для создания inventory файла ansible.

- Развертывание окружение и практическая работа - автоматизированы. Выполняется скрипт starscript из папки terraform, который разворачивает окружение в яндекс облаке. Скрипт в директории ansible/invscript.py создаёт inventory файл с необходимыми данными

- Можно запускать плейбук через:

```
 ansible-playbook -i inventory.json playbook.yaml

```
