from PIL import Image
import cv2
import numpy as np
import requests
from io import BytesIO  # Import BytesIO class from io module

# Load and process the second image
response2 = requests.get('https://images.livemint.com/rf/Image-621x414/LiveMint/Period2/2018/01/25/Photos/Processed/byd-k13F--621x414@LiveMint.jpg')
image2 = Image.open(BytesIO(response2.content))
image2 = image2.resize((450, 250))
image_arr2 = np.array(image2)

grey2 = cv2.cvtColor(image_arr2, cv2.COLOR_BGR2GRAY)
Image.fromarray(grey2)

bus_cascade_src = r'./folder/bus.xml'
bus_cascade = cv2.CascadeClassifier(bus_cascade_src)
bus = bus_cascade.detectMultiScale(grey2, 1.1, 1)

for (x, y, w, h) in bus:
    cv2.rectangle(image_arr2, (x, y), (x + w, y + h), (255, 0, 0), 2)

print(len(bus), "buses found")
Image.fromarray(image_arr2).show()

cv2.destroyAllWindows()