#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量翻译API文档的脚本
"""

import re
import os

# 日语翻译映射
JA_TRANSLATIONS = {
    # 标题和描述
    "Wan2.5 Video Generation": "Wan2.5 動画生成",
    "Wan2.5 Image-to-Video": "Wan2.5 画像から動画へ",
    "Wan2.5-Video": "Wan2.5-Video",

    # 描述文本
    "Asynchronous processing mode, returns task ID for subsequent queries": "非同期処理モードで、後続のクエリ用にタスクIDを返します",
    "Supports multiple generation modes including text-to-video and image-to-video": "テキストから動画、画像から動画などの複数の生成モードをサポートしています",
    "Generated video links are valid for 24 hours, please save them promptly": "生成された動画のリンクは24時間有効です。速やかに保存してください",
    "Generate dynamic videos from static images with intelligent interpolation": "インテリジェントな補間により静止画像から動的な動画を生成します",
    "Use the Wan2.5-Video model for video generation": "Wan2.5-Videoモデルを使用して動画を生成します",
    "Use the Wan2.5-Video model for high‑quality video generation.": "Wan2.5-Videoモデルを使用して高品質な動画を生成します。",

    # Prompt示例
    "City traffic at night": "夜の都市交通",
    "Make the person in the picture smile and wave": "写真の中の人を笑顔にして手を振らせる",

    # 错误消息
    "Invalid request parameters": "無効なリクエストパラメータです",
    "Invalid authentication credentials": "認証情報が無効です",
    "Insufficient balance. Please top up your account": "残高が不足しています。アカウントにチャージしてください",
    "Access forbidden. You don't have permission to access this resource": "アクセスが禁止されています。このリソースへのアクセス権限がありません",
    "Rate limit exceeded. Please try again later": "レート制限を超過しました。後でもう一度お試しください",
    "Internal server error. Please try again later": "内部サーバーエラーが発生しました。後でもう一度お試しください",
    "Bad gateway. The server is temporarily unavailable": "不正なゲートウェイです。サーバーが一時的に利用できません",

    # 文档说明
    "## Authorizations": "## 認証",
    "All API endpoints require Bearer Token authentication": "全てのAPIエンドポイントでBearer Token認証が必要です",
    "Get your API Key:": "APIキーの取得方法:",
    "Visit the [API Key Management Page](https://evolink.ai/console/token) to get your API Key": "[APIキー管理ページ](https://evolink.ai/console/token) にアクセスしてAPIキーを取得してください",
    "Add it to the request header:": "リクエストヘッダーに追加:",

    "## Body": "## Body",
    "Model name, must be `wan2.5-video`": "モデル名、`wan2.5-video`である必要があります",
    "Text description for video generation": "動画生成のためのテキスト説明",
    "Maximum 1000 characters": "最大1000文字",
    "Video duration in seconds": "動画の長さ (秒)",
    "Range: 5-30 seconds": "範囲: 5-30秒",
    "Range: 3-15 seconds": "範囲: 3-15秒",
    "Video aspect_ratio": "動画解像度",
    "Supported formats:": "サポートされている形式:",
    "Reference image URL for image-to-video generation": "画像から動画への生成のための参照画像URL",
    "Input image URL for video generation": "動画生成のための入力画像URL",
    "Action description for video generation": "動画生成のためのアクション説明",
    "- Must be a valid image URL": "- 有効な画像URLである必要があります",
    "- Supported formats: .jpeg, .jpg, .png, .webp": "- サポートされている形式: .jpeg, .jpg, .png, .webp",
    "- Maximum file size: 10MB": "- 最大ファイルサイズ: 10MB",

    "## Response": "## Response",
    "Task creation timestamp": "タスク作成タイムスタンプ",
    "Unique task identifier": "一意のタスク識別子",
    "The actual model name used": "実際に使用されたモデル名",
    "Object type, fixed as `video.generation.task`": "オブジェクトタイプ、`video.generation.task`で固定",
    "Object type, fixed as `video.image-to-video.task`": "オブジェクトタイプ、`video.image-to-video.task`で固定",
    "Task completion progress percentage (0-100)": "タスク完了進捗率 (0-100)",
    "Task status": "タスクステータス",
    "Possible values:": "可能な値:",
    "- `pending` - Waiting for processing": "- `pending` - 処理待ち",
    "- `processing` - In progress": "- `processing` - 処理中",
    "- `completed` - Completed": "- `completed` - 完了",
    "- `failed` - Failed": "- `failed` - 失敗",
    "Task details": "タスク詳細",
    "Whether the task can be cancelled": "タスクがキャンセル可能かどうか",
    "Estimated completion time (seconds)": "推定完了時間 (秒)",
    "Output type, fixed as `video`": "出力タイプ、`video`で固定",
    "Billing information": "課金情報",
    "Total tokens consumed": "消費された合計トークン数",

    # Highlights section
    "# Wan2.5-Video Generation": "# Wan2.5-Video 動画生成",
    "## Highlights": "## ハイライト",
    "- Asynchronous processing: returns a task ID for subsequent queries": "- 非同期処理: 後続のクエリ用にタスクIDを返します",
    "- Multiple modes: text-to-video, image-to-video": "- 複数のモード: テキストから動画、画像から動画",
    "- Expiring links: generated video links are valid for 24 hours": "- リンクの有効期限: 生成された動画のリンクは24時間有効です",
    "## Request example": "## リクエスト例",
    "## Parameters": "## パラメータ",
    'Model name. Use "wan2.5-video".': 'モデル名。"wan2.5-video"を使用してください。',
    "Text description for video generation.": "動画生成のためのテキスト説明。",
    "Video duration (seconds). Default: 12.": "動画の長さ (秒)。デフォルト: 12。",
    'Video aspect_ratio. Supported: "1920x1080", "1280x720".': '動画解像度。サポート: "1920x1080", "1280x720"。',
}

# 韩语翻译映射
KO_TRANSLATIONS = {
    # 标题和描述
    "Wan2.5 Image Generation": "Wan2.5 이미지 생성",
    "Wan2.5 Image Editing": "Wan2.5 이미지 편집",
    "Wan2.5 Video Generation": "Wan2.5 비디오 생성",
    "Wan2.5 Image-to-Video": "Wan2.5 이미지-투-비디오",
    "Wan2.5-Video": "Wan2.5-Video",
    "Wan2.5-Image": "Wan2.5-Image",

    # 描述文本
    "Asynchronous processing mode, returns task ID for subsequent queries": "비동기 처리 모드로 후속 쿼리를 위한 작업 ID를 반환합니다",
    "Supports multiple generation modes including text-to-image, image-to-image, and image editing": "텍스트에서 이미지, 이미지에서 이미지, 이미지 편집 등 다양한 생성 모드를 지원합니다",
    "Generated image links are valid for 24 hours, please save them promptly": "생성된 이미지 링크는 24시간 동안 유효하니 신속하게 저장하세요",
    "Intelligent editing based on text instructions while maintaining style consistency": "스타일 일관성을 유지하면서 텍스트 지시에 기반한 지능형 편집을 제공합니다",
    "Supports multiple generation modes including text-to-video and image-to-video": "텍스트에서 비디오, 이미지에서 비디오 등 다양한 생성 모드를 지원합니다",
    "Generated video links are valid for 24 hours, please save them promptly": "생성된 비디오 링크는 24시간 동안 유효하니 신속하게 저장하세요",
    "Generate dynamic videos from static images with intelligent interpolation": "지능형 보간을 통해 정적 이미지에서 동적 비디오를 생성합니다",
    "Use the Wan2.5-Video model for video generation": "비디오 생성을 위해 Wan2.5-Video 모델을 사용합니다",
    "Use the Wan2.5-Video model for high‑quality video generation.": "고품질 비디오 생성을 위해 Wan2.5-Video 모델을 사용합니다.",

    # Prompt示例
    "A futuristic city in sci-fi style": "SF 스타일의 미래 도시",
    "Change the background to a sunset beach": "배경을 석양 해변으로 변경",
    "City traffic at night": "밤의 도시 교통",
    "Make the person in the picture smile and wave": "사진 속 인물이 미소 짓고 손을 흔들게 하기",

    # 错误消息
    "Invalid request parameters": "잘못된 요청 매개변수입니다",
    "Invalid authentication credentials": "인증 정보가 유효하지 않습니다",
    "Insufficient balance. Please top up your account": "잔액이 부족합니다. 계정에 충전해주세요",
    "Access forbidden. You don't have permission to access this resource": "접근이 금지되었습니다. 이 리소스에 대한 권한이 없습니다",
    "Rate limit exceeded. Please try again later": "요청 한도를 초과했습니다. 나중에 다시 시도해주세요",
    "Internal server error. Please try again later": "내부 서버 오류가 발생했습니다. 나중에 다시 시도해주세요",
    "Bad gateway. The server is temporarily unavailable": "불량 게이트웨이입니다. 서버가 일시적으로 사용할 수 없습니다",

    # 文档说明
    "## Authorizations": "## 인증",
    "All API endpoints require Bearer Token authentication": "모든 API 엔드포인트에는 Bearer Token 인증이 필요합니다",
    "Get your API Key:": "API 키 받기:",
    "Visit the [API Key Management Page](https://evolink.ai/console/token) to get your API Key": "[API 키 관리 페이지](https://evolink.ai/console/token)를 방문하여 API 키를 받으세요",
    "Add it to the request header:": "요청 헤더에 추가:",

    "## Body": "## Body",
    "Model name, must be `wan2.5-image`": "모델 이름은 `wan2.5-image`이어야 합니다",
    "Model name, must be `wan2.5-video`": "모델 이름은 `wan2.5-video`이어야 합니다",
    "Text description for image generation": "이미지 생성을 위한 텍스트 설명",
    "Text description for video generation": "비디오 생성을 위한 텍스트 설명",
    "Maximum 1000 characters": "최대 1000자",
    "Image generation size": "이미지 생성 크기",
    "Output image size": "출력 이미지 크기",
    "Video duration in seconds": "비디오 길이 (초)",
    "Range: 5-30 seconds": "범위: 5-30초",
    "Range: 3-15 seconds": "범위: 3-15초",
    "Video aspect_ratio": "비디오 해상도",
    "Supported formats:": "지원되는 형식:",
    "- Ratios: `1:1`, `2:3`, `3:2`": "- 비율: `1:1`, `2:3`, `3:2`",
    "- Pixels: `1024x1024`, `1024x1536`, `1536x1024`": "- 픽셀: `1024x1024`, `1024x1536`, `1536x1024`",
    "Number of images to generate": "생성할 이미지 수",
    "Supports 1, 2, 4. Charges will be pre-deducted based on the number": "1, 2, 4를 지원합니다. 수량에 따라 요금이 사전 차감됩니다",
    "Reference image URL list for image-to-image or image editing": "이미지 간 변환 또는 이미지 편집을 위한 참조 이미지 URL 목록",
    "Reference image URL for image-to-video generation": "이미지에서 비디오로의 생성을 위한 참조 이미지 URL",
    "Input image URL for video generation": "비디오 생성을 위한 입력 이미지 URL",
    "Original image URL for editing": "편집할 원본 이미지 URL",
    "Text instructions for image editing": "이미지 편집을 위한 텍스트 지시",
    "Action description for video generation": "비디오 생성을 위한 액션 설명",
    "Mask image URL for precise editing": "정밀한 편집을 위한 마스크 이미지 URL",
    "- Maximum 5 images": "- 최대 5개 이미지",
    "- Each image should not exceed 10MB": "- 각 이미지는 10MB를 초과하지 않아야 합니다",
    "- Must be a valid image URL": "- 유효한 이미지 URL이어야 합니다",
    "- Supported formats: .jpeg, .jpg, .png, .webp": "- 지원되는 형식: .jpeg, .jpg, .png, .webp",
    "- Maximum file size: 10MB": "- 최대 파일 크기: 10MB",
    "- Must be PNG format": "- PNG 형식이어야 합니다",
    "- Size must match the original image": "- 크기가 원본 이미지와 일치해야 합니다",
    "- Maximum file size: 4MB": "- 최대 파일 크기: 4MB",

    "## Response": "## Response",
    "Task creation timestamp": "작업 생성 타임스탬프",
    "Unique task identifier": "고유한 작업 식별자",
    "The actual model name used": "실제로 사용된 모델 이름",
    "Object type, fixed as `image.generation.task`": "객체 유형, `image.generation.task`로 고정",
    "Object type, fixed as `image.editing.task`": "객체 유형, `image.editing.task`로 고정",
    "Object type, fixed as `video.generation.task`": "객체 유형, `video.generation.task`로 고정",
    "Object type, fixed as `video.image-to-video.task`": "객체 유형, `video.image-to-video.task`로 고정",
    "Task completion progress percentage (0-100)": "작업 완료 진행률 (0-100)",
    "Task status": "작업 상태",
    "Possible values:": "가능한 값:",
    "- `pending` - Waiting for processing": "- `pending` - 처리 대기 중",
    "- `processing` - In progress": "- `processing` - 진행 중",
    "- `completed` - Completed": "- `completed` - 완료됨",
    "- `failed` - Failed": "- `failed` - 실패",
    "Task details": "작업 세부 정보",
    "Whether the task can be cancelled": "작업을 취소할 수 있는지 여부",
    "Estimated completion time (seconds)": "예상 완료 시간 (초)",
    "Output type, fixed as `image`": "출력 유형, `image`로 고정",
    "Output type, fixed as `video`": "출력 유형, `video`로 고정",
    "Billing information": "청구 정보",
    "Total tokens consumed": "소비된 총 토큰 수",
    
    # 更多翻译
    "Image generation size": "이미지 생성 크기",
    "- Ratios: `1:1`, `2:3`, `3:2`": "- 비율: `1:1`, `2:3`, `3:2`",
    "- Pixels: `1024x1024`, `1024x1536`, `1536x1024`": "- 픽셀: `1024x1024`, `1024x1536`, `1536x1024`",
    "Reference image URL list for image-to-image or image editing": "이미지 간 변환 또는 이미지 편집을 위한 참조 이미지 URL 목록",
    "- Each image should not exceed 10MB": "- 각 이미지는 10MB를 초과하지 않아야 합니다",

    # Highlights section
    "# Wan2.5-Video Generation": "# Wan2.5-Video 비디오 생성",
    "## Highlights": "## 주요 기능",
    "- Asynchronous processing: returns a task ID for subsequent queries": "- 비동기 처리: 후속 쿼리를 위한 작업 ID 반환",
    "- Multiple modes: text-to-video, image-to-video": "- 다중 모드: 텍스트-투-비디오, 이미지-투-비디오",
    "- Expiring links: generated video links are valid for 24 hours": "- 링크 만료: 생성된 비디오 링크는 24시간 동안 유효",
    "## Request example": "## 요청 예시",
    "## Parameters": "## 매개변수",
    'Model name. Use "wan2.5-video".': '모델 이름. "wan2.5-video"를 사용하세요.',
    "Text description for video generation.": "비디오 생성을 위한 텍스트 설명.",
    "Video duration (seconds). Default: 12.": "비디오 길이 (초). 기본값: 12.",
    'Video aspect_ratio. Supported: "1920x1080", "1280x720".': '비디오 해상도. 지원: "1920x1080", "1280x720".',
}

def translate_file(source_path, target_path, translations):
    """翻译文件内容"""
    if not os.path.exists(source_path):
        print(f"源文件不存在: {source_path}")
        return False

    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 应用所有翻译
    for english, translated in translations.items():
        content = content.replace(english, translated)

    # 确保目标目录存在
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"已翻译: {target_path}")
    return True

# 主执行
if __name__ == "__main__":
    base_dir = "d:/api-doc/10.11"

    # 日语文件列表
    ja_files = [
        ("en/api-reference/videos/wan2-5-video/generation.mdx", "ja/api-reference/videos/wan2-5-video/generation.mdx"),
        ("en/api-reference/videos/wan2-5-video/image-to-video.mdx", "ja/api-reference/videos/wan2-5-video/image-to-video.mdx"),
        ("en/api-reference/videos/wan2-5-video.mdx", "ja/api-reference/videos/wan2-5-video.mdx"),
    ]

    # 韩语文件列表
    ko_files = [
        ("en/api-reference/images/wan2-5-image/generation.mdx", "ko/api-reference/images/wan2-5-image/generation.mdx"),
        ("en/api-reference/images/wan2-5-image/editing.mdx", "ko/api-reference/images/wan2-5-image/editing.mdx"),
        ("en/api-reference/videos/wan2-5-video/generation.mdx", "ko/api-reference/videos/wan2-5-video/generation.mdx"),
        ("en/api-reference/videos/wan2-5-video/image-to-video.mdx", "ko/api-reference/videos/wan2-5-video/image-to-video.mdx"),
        ("en/api-reference/videos/wan2-5-video.mdx", "ko/api-reference/videos/wan2-5-video.mdx"),
    ]

    print("开始翻译日语文件...")
    ja_success = 0
    for src, dst in ja_files:
        if translate_file(os.path.join(base_dir, src), os.path.join(base_dir, dst), JA_TRANSLATIONS):
            ja_success += 1

    print(f"\n日语文件翻译完成: {ja_success}/{len(ja_files)}")

    print("\n开始翻译韩语文件...")
    ko_success = 0
    for src, dst in ko_files:
        if translate_file(os.path.join(base_dir, src), os.path.join(base_dir, dst), KO_TRANSLATIONS):
            ko_success += 1

    print(f"\n韩语文件翻译完成: {ko_success}/{len(ko_files)}")

    print(f"\n总计翻译完成: {ja_success + ko_success}/{len(ja_files) + len(ko_files)}")
