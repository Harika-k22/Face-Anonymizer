import cv2

# load face detector
'''  This XML file is a pre-trained face detection model
It comes from OpenCV (trained using Haar features)
What it contains:
Mathematical rules to identify human faces
Patterns like:
Eyes region
Nose bridge
Face shape  
Haar Cascade Classifier=A classic (fast, lightweight) algorithm for object detection '''

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def blur_faces(frame):
    #convert to grayscale
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # blur faces
    for(x,y,w,h)in faces:
        face=frame[y:y+h,x:x+w]# extracting face region
        face=cv2.GaussianBlur(face,(99,99),30)
        frame[y:y+h,x:x+w]=face # putting blurred face back
    return frame


#choice
print("1.Image")
print("2.Video")
print("3.webcam")

choice=int(input("Enter choice:"))

#Image- runs function once

if choice==1:
    img_path = "/Users/harikak/PyCharmMiscProject/random_pic.png"
    img=cv2.imread(img_path)

    if img is None:
        print("image not found")
    else:
        res=blur_faces(img)
        cv2.imshow("res",res)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#Video- runs function on each frame in a loop

elif choice==2:
    vid_path="/Users/harikak/PyCharmMiscProject/random_vid.mov"

    cap=cv2.VideoCapture(vid_path)
    width=int(cap.get(3))
    height=int(cap.get(4))
    fps=int(cap.get(cv2.CAP_PROP_FPS))

    out=cv2.VideoWriter("output.mp4",cv2.VideoWriter_fourcc(*'mp4v'),fps,(width,height))

    while True:
        ret,frame=cap.read();
        if not ret:
            break
        frame=blur_faces(frame)
        out.write(frame)
        cv2.imshow("vid_blur",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

#Webcam- runs continuously in real-time

elif choice==3:
    cap=cv2.VideoCapture(0)

    while(True):
        ret,frame=cap.read()
        if not ret:
            break
        frame=blur_faces(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        frame=blur_faces(frame)
        cv2.imshow("webcam_blur",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print("Invalid choice")
