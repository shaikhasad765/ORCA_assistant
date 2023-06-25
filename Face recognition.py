import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
recognizer.read('trainer/trainer.yml') # load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath) # initializing haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX # denotes the font type

id = 2 # number of persons you want to recognize

names = ['','Asad Shaikh'] # names, leave first empty because counter starts from 0

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) # cv2.CAP_DSHOW to remove warning
cam.set(3, 640) #set video FrameWidth
cam.set(4, 480) #set video FrameHeight

#define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read() # read the frames using the above created object

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # the function converts an input image from one color space to another

    faces = faceCascade.detectMultiScale(
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
    )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) # to predict on every single image

        # check if accuracy is less than 100 ==> "0" is perfect match
        if (accuracy < 100):
            id = names[id]
            accuracy = "   {0}%".format(round(100 - accuracy))

        else:
            id = "Face Not Recognized"
            accuracy = "   {0}%".format(round(100 - accuracy))

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)

    cv2.imshow('LBPH face recognition system', img)

    k = cv2.waitKey(10) & 0xff # press 'Ese' to exit video
    if k==27:
        break

print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()