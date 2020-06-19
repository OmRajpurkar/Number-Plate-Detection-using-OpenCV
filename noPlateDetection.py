import cv2

##############################################################
frameWidth = 640
frameHeight = 480
# Import the model
noPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minArea = 500
color = (255,0,255)
count = 0
##############################################################

vid = cv2.VideoCapture(0)
vid.set(3, frameWidth)
vid.set(4, frameHeight)
vid.set(10, 100)

while True:
    success, img = vid.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Find the number plates in our image
    numberPlates = noPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    # Create bounding box around the faces that we have detected. So we need to loop through all the faces that we have detected.
    for (x, y, w, h) in numberPlates:
        area=w*h

        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 4)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow("ROI", imgRoi)


    cv2.imshow("Output", img)

    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"No. Plate Saved",(50,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("Output", img)
        cv2.waitKey(500)
        count += 1
