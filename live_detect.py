# import the opencv library
import cv2

#Load the cascade classifier file
faceCascade = cv2.CascadeClassifier('PRO-C106-Student-Boilerplate-main/haarcascade_frontalface_default.xml')

# Define a video capture object
vid = cv2.VideoCapture(0)

while(True):
   
    # Capture the video frame by frame
    ret, frame = vid.read()

    #Convert frames to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect the faces
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    #drawing rectangles around each face
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        

    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()