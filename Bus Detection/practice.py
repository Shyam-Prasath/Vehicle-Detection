from PIL import Image
import cv2
import numpy as np
import requests
from io import BytesIO  # Import BytesIO class from io module

# Reading image from URL
response = requests.get('https://a57.foxnews.com/media.foxbusiness.com/BrightCove/854081161001/201805/2879/931/524/854081161001_5782482890001_5782477388001-vs.jpg')
image = Image.open(BytesIO(response.content))
image = image.resize((450, 250))
image_arr = np.array(image)

grey = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)
Image.fromarray(grey)

blur = cv2.GaussianBlur(grey, (5, 5), 0)
Image.fromarray(blur)

dilated = cv2.dilate(blur, np.ones((3, 3)))
Image.fromarray(dilated)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
Image.fromarray(closing)

car_cascade_src = r'./cars.xml'
car_cascade = cv2.CascadeClassifier(car_cascade_src)
cars = car_cascade.detectMultiScale(closing, 1.1, 1)

for (x, y, w, h) in cars:
    cv2.rectangle(image_arr, (x, y), (x + w, y + h), (255, 0, 0), 2)

print(len(cars), "cars found")
Image.fromarray(image_arr).show()

cv2.destroyAllWindows()