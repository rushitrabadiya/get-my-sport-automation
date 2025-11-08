import os
import json
import datetime
import requests
import pandas as pd
from prompts import build_prompt

OUTPUT_DIR = "output/images"
EXCEL_FILE = "output/captions.xlsx"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_caption_and_prompt(content: str):
    """
    Calls Pollinations text API to generate caption, image prompt, and hashtags.
    """
    prompt = build_prompt(content)

    response = requests.get(
        f"https://text.pollinations.ai/{prompt}",
        headers={"referer": "https://pollinations.ai/"}
    )

    if response.status_code != 200:
        raise Exception(f"Error fetching caption: {response.status_code}")

    try:
        result = json.loads(response.text)
        return result["caption"], result["image_prompt"], result["hashtags"]
    except Exception as e:
        raise Exception(f"Invalid response format: {e}")


def generate_image(image_prompt: str, image_index: int):
    """
    Generates an image using Pollinations image API and saves it locally.
    """
    response = requests.get(
        f"https://image.pollinations.ai/prompt/{image_prompt}",
        params={"model": "kontext"},
        headers={"referer": "https://pollinations.ai/"},
        stream=True
    )

    image_path = os.path.join(OUTPUT_DIR, f"img{image_index}.png")

    if response.status_code == 200:
        with open(image_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return os.path.abspath(image_path)
    else:
        raise Exception(f"Error generating image: {response.status_code}")


def save_to_excel(caption: str, hashtags: list, image_path: str):
    """
    Appends generated caption & image info to an Excel sheet.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([{
        "caption": caption,
        "hashtags": " ".join(hashtags),
        "image_path": image_path,
        "created_at": now
    }])

    if os.path.exists(EXCEL_FILE):
        existing = pd.read_excel(EXCEL_FILE)
        updated = pd.concat([existing, new_data], ignore_index=True)
    else:
        updated = new_data

    updated.to_excel(EXCEL_FILE, index=False)
