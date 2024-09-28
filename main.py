

from io import BytesIO
from barcode import generate
import barcode
from barcode.writer import ImageWriter


barCode128 = '46003380099881'


EAN = barcode.get_barcode_class('code128')
my_ean = EAN(barCode128, writer=ImageWriter())

fullname = my_ean.save('code128_barcode')


fp = BytesIO()
my_ean.write(fp)



with open("fileBarCode", "wb") as f:
    my_ean.write(f)  # Pillow (ImageWriter) produces RAW format here


name = generate('CODE128', barCode128, output='barcode_svg')

fp = BytesIO()
generate('CODE128', barCode128, writer=ImageWriter(), output=fp)
