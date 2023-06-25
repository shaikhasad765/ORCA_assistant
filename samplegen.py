import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) # creates a video capture object which is helpful to capture videos through webcam
cam.set(3, 640) # set video FrameWidth
cam.set(4, 480) # set video FrameHeight

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Haar Cascade classifier is an effective object detection approach

face_id = input("Enter a Numeric user ID here: ")
#use integer ID for every new face

print("Taking samples, Look at camera .......")
count = 0 # Initializing sampling face count

try:
    while True:

        ret, img = cam.read() #read the frames using the above created object
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #The function converts an input image from one color space to another
        faces = detector.detectMultiScale(converted_image, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) #used to draw a rectangle on any image
            count += 1

            cv2.imwrite("samples/face." + str(face_id) + '.' + str(count) + ".jpg", converted_image[y:y+h,x:x+w])
            # to capture  & save images into the datasets folder

            cv2.imshow('image', img) # used to display an image in a window

        k = cv2.waitKey(100) & 0xff # waits for a pressed key
        if k == 27: # Press 'Esc' to stop
            break
        elif count >= 100: # Take 50 sample (More sample --> More accuracy)
            break

    print("Samples taken now closing the program....")
    cam.release()
    cv2.destroyAllWindows()
except:
    print("Camera not connected please connect the camera")
pass