from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import io

app = FastAPI()

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image: Image.Image) -> str:
    """Generates a caption for a given image using BLIP model."""
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

@app.post("/caption")
async def caption_image(file: UploadFile = File(...)):
    """API endpoint to generate captions for an uploaded image."""
    try:
        image = Image.open(io.BytesIO(await file.read())).convert("RGB")
        caption = generate_caption(image)
        return JSONResponse(content={"filename": file.filename, "caption": caption})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500) 