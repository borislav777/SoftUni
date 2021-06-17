import os

directories = os.listdir()
file_report = {}
for directory in directories:
    name, file_type = os.path.splitext(directory)
    if file_type not in file_report:
        file_report[file_type] = []
    file_report[file_type].append(name)
report = ''
for file_type, names in sorted(file_report.items(), key=lambda x: x[1]):
    report += f"{file_type}\n"
    for name in names:
        report += f"--- {name}{file_type}\n"
with open(f"{os.environ['USERPROFILE']}\\Desktop\\report.txt",'w') as file:
    file.write(report)
