import cv2
from cvzone.HandTrackingModule import HandDetector
import boto3

from flask import Flask
app=Flask(__name__)

@app.route("/rotate")
def rotateVideo():
    cap=cv2.VideoCapture(0)
    while(True):
        status,photo=cap.read()
        photo=photo[::-1,::-1] 
        cv2.imshow("",photo)
        index_line=0
        if cv2.waitKey(100)==13:
            break
    cv2.destroyAllWindows()
    
@app.route("/emojiOnFace")
def emoji():
    cap = cv2.VideoCapture(0)
    while (True):
        status,photo = cap.read()
        crown_img = cv2.imread("crown.png", cv2.IMREAD_UNCHANGED)
        resized_crown = cv2.resize(crown_img, None, fx=0.3, fy=0.2, interpolation=cv2.INTER_AREA)

        photo[50:197,200:540] = resized_crown[0:147,0:340]
        #print(f"photo Shape:{photo.shape}")
        if cv2.waitKey(100)==13:
            break
        cv2.imshow("Main",photo)
    cv2.destroyAllWindows()


@app.route("/fingerOSlaunch")
def finger():
    #task 4
    cap = cv2.VideoCapture(0)

    status,photo = cap.read()
    cv2.imshow("myphoto" , photo)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    cap.release()

    detector = HandDetector()
    myhand = detector.findHands(photo)
    mylmlist = myhand[0][0]
    myfinger = detector.fingersUp(mylmlist)

    myec2=boto3.resource(service_name="service_name",
                        aws_access_key_id="access_key",
                        aws_secret_access_key="secret_access_key",
                        region_name="ap-south-1")

    def osLaunch():
        myec2.create_instances(InstanceType = "t2.micro",
                            ImageId = "ami-0ec0e125bb6c6e8ec",
                            MinCount = 1,
                            MaxCount =1)
    if myfinger == [0,1,1,0,0]:
        osLaunch()
        osLaunch()
        
    elif myfinger == [1,1,1,1,1]:
        osLaunch()
        osLaunch()
        osLaunch()
        osLaunch()
        osLaunch()
    else:
        print("idk")
        

        
app.run()
    