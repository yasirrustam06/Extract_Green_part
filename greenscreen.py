import cv2


#     Load the image....
Image = cv2.imread('image.jpg')
# resize the image....
Res_Image = cv2.resize(Image,(512,512))

#   Convert the image to HSV color space...
HSV_Image = cv2.cvtColor(Res_Image, cv2.COLOR_BGR2HSV)

# define the lower and upper ranges for green color...
lower_green = (50, 25, 25)
upper_green = (86, 255, 255)

# Create a mask of green color pixels...
mask = cv2.inRange(HSV_Image, lower_green, upper_green)

# Apply the mask to the original image to extract the green area...
result = cv2.bitwise_and(Res_Image, Res_Image, mask=mask)

# Display the result...

cv2.imshow("Original_Image",Res_Image)
cv2.imshow('Greened_Area_Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
