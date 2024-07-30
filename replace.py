import re

# Difined Dict
translation_dict = {

}

# counter
replacement_count = {key: 0 for key in translation_dict}

# count the usuage
def replace_text_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for chinese, english in translation_dict.items():
        count = len(re.findall(chinese, content))
        replacement_count[chinese] += count
        content = content.replace(chinese, english)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# file path
file_path = r'C:\Users\User\Desktop\TheFiles\CameraConfigPro\Galaxy general config V1(Specialized for black screen).agc'

# excute it
replace_text_in_file(file_path)

# counter back
for chinese, count in replacement_count.items():
    print(f"'{chinese}' replaced {count} times.")
