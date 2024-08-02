import re

# Difined Dict
translation_dict = {
    "夜视仪": "Night Vision PRO",
    "徕卡灵动": "Leica Vivid",
    "徕卡柔和": "Leica Soft",
    "徕卡鲜艳": "Leica Spirited",
    "复古胶片": "Vintage Film",
    "自然人像": "Natural Portrait",
    "电影叙事": "Cinematic Filter",
    "极致青橙": "Cyan and Orange",
    "哈苏自然": "Hasselblad Natural",
    "富士模式": "Fuji Mode",
    "黑白人文": "Black and White Humanistic",
    "印象怀旧": "Nostalgic Impression",
    "酷灰质感": "Cool Gray Texture"
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
file_path = r'C:\Users\User\Desktop\TheFiles\CameraConfigPro\oppo series phone\oppo FindX6 Pro.agc'

# excute it
replace_text_in_file(file_path)

# counter back
for chinese, count in replacement_count.items():
    print(f"'{chinese}' replaced {count} times.")
