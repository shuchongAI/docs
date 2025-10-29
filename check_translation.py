#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

def check_file_translation(en_path, target_path, lang):
    """检查文件是否已翻译"""
    if not os.path.exists(target_path):
        return f"文件不存在: {target_path}"

    with open(en_path, 'r', encoding='utf-8') as f:
        en_content = f.read()

    with open(target_path, 'r', encoding='utf-8') as f:
        target_content = f.read()

    # 提取title
    en_title_match = re.search(r'title:\s*"([^"]+)"', en_content)
    target_title_match = re.search(r'title:\s*"([^"]+)"', target_content)

    if en_title_match and target_title_match:
        en_title = en_title_match.group(1)
        target_title = target_title_match.group(1)

        # 如果title完全相同,说明未翻译
        if en_title == target_title:
            return f"未翻译({lang}): {target_path} - title: {en_title}"

    return None

# 遍历所有英文文件
base_dir = "d:/api-doc/10.11"
untranslated = []

for root, dirs, files in os.walk(os.path.join(base_dir, "en")):
    for file in files:
        if file.endswith(".mdx"):
            en_path = os.path.join(root, file)
            rel_path = os.path.relpath(en_path, os.path.join(base_dir, "en"))

            ja_path = os.path.join(base_dir, "ja", rel_path)
            ko_path = os.path.join(base_dir, "ko", rel_path)

            # 检查日语
            result = check_file_translation(en_path, ja_path, "日语")
            if result:
                untranslated.append(result)

            # 检查韩语
            result = check_file_translation(en_path, ko_path, "韩语")
            if result:
                untranslated.append(result)

if untranslated:
    print("发现未翻译的文件:")
    for item in untranslated:
        print(item)
    print(f"\n总计: {len(untranslated)} 个文件未翻译")
else:
    print("✅ 所有文件都已翻译!")
