from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

top_text=input("Введите верхний текст ")
bottom_text=input("Введите нижний текст ")
fon_text1=input("Введите цвет надписи для верхнего текста (на английском): ")
fon_text2=input("Введите цвет надписи для нижнего текста (на английском): ")

print("выберете картинку:")
print("1-удевлённый кот")
print("2-хмурый и недовольный кот")
print("3-крутой кот в крутых очках")
print("4-кот в очках")
print("5-кот в ресторане")

nomer=int(input("Введите номер картинки: "))

if nomer == 1:
    image_file="3f6739f257704f8dab767978ea3f8f33.jpg"
elif nomer == 2:
    image_file="d96c2fd30cceac847d9de927f917cea2.jpeg"
elif nomer == 3:
    image_file="1680553436_pushinka-top-p-avatarka-kotik-v-ochkakh-avatarka-pintere-70.jpg"
elif nomer == 4:
    image_file="Кот в очках.png"
elif nomer == 5:
    image_file="Кот в ресторане.png"

image = Image.open(image_file)
width, height = image.size
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size=100)
text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]
draw.text(((width - text_width) / 2, 10), top_text, font=font, fill=fon_text1)
text=draw.textbbox((0,0), bottom_text, font)
text_width=text[2]
text_height=text[3]
draw.text(((width - text_width) / 2, height-text_height-10), bottom_text, font=font, fill=fon_text2)
image.save("новый_мем.jpg")
