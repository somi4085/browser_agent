from openai import OpenAI
from pathlib import Path
from config import Config
import base64


class VisionAgent:
    def __init__(self):
        self.history = []
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def encode_image(self, image_path:str):
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read())
            return encoded.decode("utf-8")
        
    
    async def analyze_screenshots(self, image_path:str, task:str):
        image_data = self.encode_image(image_path)
        response = self.client.chat.completions.create(
            model=Config.MODEL,
            messages=[{
                "role":"user",
                "content":[
                    {"type":"text","text":task},
                    {"type":"image_url","image_url":{"url":f"data:image/png;base64,{image_data}","detail":"high"}}
                ]
            }]
        )
        self.history.append(response)
        return response.choices[0].message.content
