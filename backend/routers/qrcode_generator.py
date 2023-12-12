import qrcode
import io
from PIL import Image
from fastapi import APIRouter, Response
from pydantic import BaseModel


router = APIRouter(
    prefix='/api',
    tags=["QRCode Generator"],
)

class QRCodeModel(BaseModel):
    text: str

@router.post('/generate-qrcode')
async def generate_qrcode(qrcode_data: QRCodeModel, colour:str = "black"):
    """Create a QRCode code from the text provided"""
    qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=1)
    qr.add_data(qrcode_data.text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=colour, back_color="white")


    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='PNG')

    # Create PIL image from the byte stream
    pil_img = Image.open(img_byte_array)

    # Convert PIL image to byte stream
    buffered = io.BytesIO()
    pil_img.save(buffered, format="PNG")
    img_data = buffered.getvalue()

    # Return the image as a response
    return Response(content=img_data, media_type="image/png")
