import cv2

solar = cv2.imread("solar-system.jpg")

cv2.putText(solar, "sun", (100,80), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
cv2.putText(solar, "mecury", (120,100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
cv2.putText(solar, "venus", (200,80), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
cv2.putText(solar, "earth", (300,80), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
cv2.putText(solar, "mars", (400,80), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
cv2.putText(solar, "jupiter", (500,90), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
cv2.putText(solar, "saturn", (700,105), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
cv2.putText(solar, "uranus", (950,105), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
cv2.putText(solar, "neptune", (1050,105), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))

cv2.imwrite("solar_system_labelled.jpg", solar)
cv2.imshow("solar", solar)
cv2.waitKey(0)