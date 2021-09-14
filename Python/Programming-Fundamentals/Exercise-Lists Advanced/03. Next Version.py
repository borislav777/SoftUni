version = input().split(".")
version_as_num = int("".join(version)) + 1
new_version = list(str(version_as_num))
print(".".join(new_version))

