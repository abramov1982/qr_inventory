import subprocess
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont
import silent_print

inventory = []
with open('inv_numbers.txt', 'r') as f:
    for i in f.readlines():
        inventory.append(i.strip('\n'))
def serial():
    qr = qrcode.QRCode()
    serial_num = input('Enter serial number - ')
    #serial_num = serial_num[12:]
    print(serial_num)
    inv_num = inventory[0]
    with open("inv_data.txt", "a") as f:
        f.write(f'{serial_num}\t{inv_num}\n')
    del inventory[0]
    with open("inv_numbers.txt", "w") as f:
        for i in inventory:
            f.write(i+'\n')
    qr.add_data(f's/n: {serial_num}\nИнв: {inv_num}')
    img = qr.make_image()
    font = ImageFont.truetype("arial.ttf", 35)
    background = Image.new('RGB', (740, 370), (255, 255, 255, 255))
    background.paste(img)
    drawer = ImageDraw.Draw(background)
    drawer.text((370, 100), f's/n: {serial_num}', font=font, fill='black')
    drawer.text((370, 220), f'Инв: {inv_num}', font=font, fill='black')
    dir = os.curdir + "\qrcodes"
    inv_num = inv_num.replace('/', '_')
    filename = f'{dir}\{serial_num}_{inv_num}.pdf'
    background.save(filename)
    path_to_pdf = (filename)
    path_to_acrobat = os.path.abspath('c:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe')
    #subprocess.Popen([path_to_acrobat, '/A', 'page=1', path_to_pdf], shell=False, stdout=subprocess.PIPE)
    #more = input('Press "Enter" for one more number')
    silent_pint.main(path_to_acrobat, filename, 'ZDesigner QLn320')
    serial()

serial()