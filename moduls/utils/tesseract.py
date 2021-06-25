import cv2
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'c:\\tesseract_orc\\tesseract.exe'


img = cv2.imread('111222.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, lang='rus', config=custom_config))

cv2.imshow('Result', img)
cv2.waitKey(0)
