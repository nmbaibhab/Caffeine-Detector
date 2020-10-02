import cv2
import numpy as np
import requests
import io
import json

def caffeine(text_detected):
    x = text_detected.lower()
    if "caffeine present" or "contains caffeine" in x:
        print("\nCaffeine : Present")
    else:
        print("\nCaffeine : Absent")


#reading the required image
img = cv2.imread("filename.jpg")

height ,width , x = img.shape
edit_img = img[0:height,0:width]
'''
#to edit image's height width if required

#print(img.shape)
height ,width , x =img.shape
edit_img = img[0:height,0:width-value]
cv2.imshow("filename",edit_img)

'''

#OCR part 
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg" , edit_img , [1,90])
file_bytes = io.BytesIO(compressedimage)
fetch_result = requests.post(url_api,
                    files={"filename.jpg" : file_bytes},
                    data={"apikey":" *PUT YOUR API KEY HERE* "})

result = fetch_result.content.decode()
result = json.loads(result)
#print(result)
text_detected = result.get("ParsedResults")[0].get("ParsedText")
print("\n\nLabel detected:\n\n")
print(text_detected)
#print(type(text_detected))


#caffeine detection in text
caffeine(text_detected)


cv2.imshow("filename",edit_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

