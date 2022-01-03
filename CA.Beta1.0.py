import cv2
import numpy as np
import pyautogui
import time
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    #capture the area to detech gray
    g1 = pyautogui.screenshot(region=(1616,764,4,4))
    g2 = pyautogui.screenshot(region=(1811,764,4,4))
    g3 = pyautogui.screenshot(region=(1843,867,4,4))
    #convert to numpy
    gc1 = np.array(g1)
    gc2 = np.array(g2)
    gc3 = np.array(g3)
    #convert from RGB to HSV
    hsv1 = cv2.cvtColor(gc1, cv2.COLOR_RGB2HSV)
    hsv2 = cv2.cvtColor(gc2, cv2.COLOR_RGB2HSV)
    hsv3 = cv2.cvtColor(gc3, cv2.COLOR_RGB2HSV)
    #setting the range of the color
    lowergray = np.array([0, 20, 75])
    uppergray = np.array([255, 25, 85])
    #detechto gray color from the area that selected
    dg1 = cv2.inRange(hsv1,lowergray,uppergray)
    dg2 = cv2.inRange(hsv2,lowergray,uppergray)
    dg3 = cv2.inRange(hsv3,lowergray,uppergray)
    #count the gray pixel that can detected
    count1 = np.sum(np.nonzero(dg1))
    count2 = np.sum(np.nonzero(dg2))
    count3 = np.sum(np.nonzero(dg3))

    picdiffstate = ('Not detect')
    face_detectstate = ('No face!!')
    picdiffstate = ('Not detect yet') 
    
    #write the loop
    if count1 == 0 and count2 == 0 and count3 == 0 :
        
        #img = pyautogui.screenshot()
        Color_detectionstete = ('Not gray')
        img = pyautogui.screenshot(region=(1585, 735, 295, 165))
        time.sleep(0.5)
        img2 = pyautogui.screenshot(region=(1585, 735, 295, 165))
        previous_frame= np.array(img)
        current_frame= np.array(img2)

        current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        previous_frame_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
    # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
    # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        faces = face_cascade.detectMultiScale(frame, 1.1, 4)
        
          
        for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                frame_diff = cv2.absdiff(current_frame_gray,previous_frame_gray)
                count4 = np.sum(np.nonzero(frame_diff))
                face_detectstate = ('there face!!')
                if count4 == 0:
                    picdiffstate = ('same')
                    time.sleep(1)
                    break
                    
                else:
                    picdiffstate = ('not same')
                    time.sleep(1)
                    break
                    
        
                
                
    else:
        Color_detectionstete = ('it gray')
        time.sleep(1)
       
    # write the frame
    
    
     # show the frame
    cv2.imshow("screenshot", frame)
    with open('readme.txt', 'w') as f:
        f.write('Color detect =',Color_detectionstete,'/','face detection =',face_detectstate,'/','frame difference =',picdiffstate)
    time.sleep(2)
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
