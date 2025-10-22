#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新API文档中的model参数格式
"""

import os
import re
from pathlib import Path

# 定义各个模型的配置
MODEL_CONFIGS = {
    # 图像生成模型
    'gpt-4o-image': {
        'default': 'gpt-4o-image',
        'desc_cn': '图像生成模型名称',
        'desc_en': 'Image generation model name',
        'desc_ja': '画像生成モデル名',
        'desc_ko': '이미지 생성 모델 이름',
    },
    'qwen': {
        'default': 'qwen',
        'desc_cn': '图像生成模型名称',
        'desc_en': 'Image generation model name',
        'desc_ja': '画像生成モデル名',
        'desc_ko': '이미지 생성 모델 이름',
    },
    'seedream-4.0': {
        'default': 'seedream-4.0',
        'desc_cn': '图像生成模型名称',
        'desc_en': 'Image generation model name',
        'desc_ja': '画像生成モデル名',
        'desc_ko': '이미지 생성 모델 이름',
    },
    'gemini-2.5-flash-image': {
        'default': 'gemini-2.5-flash-image',
        'desc_cn': '图像生成模型名称',
        'desc_en': 'Image generation model name',
        'desc_ja': '画像生成モデル名',
        'desc_ko': '이미지 생성 모델 이름',
    },
    'wan2-5-image': {
        'default': 'wan2-5-image',
        'desc_cn': '图像生成模型名称',
        'desc_en': 'Image generation model name',
        'desc_ja': '画像生成モデル名',
        'desc_ko': '이미지 생성 모델 이름',
    },
    # 视频生成模型
    'sora-2': {
        'default': 'sora-2',
        'desc_cn': '视频生成模型名称',
        'desc_en': 'Video generation model name',
        'desc_ja': 'ビデオ生成モデル名',
        'desc_ko': '비디오 생성 모델 이름',
    },
    'veo3': {
        'default': 'veo3',
        'desc_cn': '视频生成模型名称',
        'desc_en': 'Video generation model name',
        'desc_ja': 'ビデオ生成モデル名',
        'desc_ko': '비디오 생성 모델 이름',
    },
    'wan2-5-video': {
        'default': 'wan2-5-video',
        'desc_cn': '视频生成模型名称',
        'desc_en': 'Video generation model name',
        'desc_ja': 'ビデオ生成モデル名',
        'desc_ko': '비디오 생성 모델 이름',
    },
}

def get_language_from_path(file_path):
    """从文件路径获取语言代码"""
    parts = Path(file_path).parts
    if 'cn' in parts:
        return 'cn'
    elif 'en' in parts:
        return 'en'
    elif 'ja' in parts:
        return 'ja'
    elif 'ko' in parts:
        return 'ko'
    return 'cn'  # 默认中文

def detect_model_from_file(file_path, content):
    """从文件路径或内容中检测模型名称"""
    # 从路径检测
    path_str = str(file_path).lower()
    for model in MODEL_CONFIGS.keys():
        if model.replace('.', '-') in path_str or model in path_str:
            return model
    
    # 从内容检测
    model_match = re.search(r'"model":\s*"([^"]+)"', content)
    if model_match:
        model_name = model_match.group(1)
        if model_name in MODEL_CONFIGS:
            return model_name
    
    return None

def update_model_param(content, model_name, language):
    """更新model参数的格式"""
    if model_name not in MODEL_CONFIGS:
        return content
    
    config = MODEL_CONFIGS[model_name]
    desc_key = f'desc_{language}'
    description = config.get(desc_key, config['desc_cn'])
    default_value = config['default']
    
    # 构建新的ParamField
    new_param = f'''<ParamField body="model" type="string" default="{default_value}" required>
  {description}

  Example: `"{default_value}"`
</ParamField>'''
    
    # 匹配旧的model ParamField（多行匹配）
    # 匹配从 <ParamField body="model" 到 </ParamField>
    pattern = r'<ParamField body="model"[^>]*>.*?</ParamField>'
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_param, content, flags=re.DOTALL)
        return content
    
    return content

def process_file(file_path):
    """处理单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检测模型
        model = detect_model_from_file(file_path, content)
        if not model:
            print(f"⚠️  跳过 {file_path}: 无法检测模型")
            return False
        
        # 检测语言
        language = get_language_from_path(file_path)
        
        # 更新内容
        new_content = update_model_param(content, model, language)
        
        # 如果内容有变化，写入文件
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ 已更新 {file_path} (model: {model}, lang: {language})")
            return True
        else:
            print(f"ℹ️  跳过 {file_path}: 已是最新格式")
            return False
    
    except Exception as e:
        print(f"❌ 处理 {file_path} 时出错: {e}")
        return False

def main():
    """主函数"""
    base_dir = Path('.')
    
    # 查找所有需要处理的文件
    patterns = [
        '**/api-reference/images/**/generation.mdx',
        '**/api-reference/images/**/editing.mdx',
        '**/api-reference/videos/**/generation.mdx',
        '**/api-reference/videos/**/image-to-video.mdx',
    ]
    
    files_to_process = set()
    for pattern in patterns:
        files_to_process.update(base_dir.glob(pattern))
    
    print(f"找到 {len(files_to_process)} 个文件待处理\n")
    
    updated_count = 0
    for file_path in sorted(files_to_process):
        if process_file(file_path):
            updated_count += 1
    
    print(f"\n完成！共更新了 {updated_count} 个文件。")

if __name__ == '__main__':
    main()

