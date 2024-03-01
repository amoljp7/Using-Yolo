import cv2
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
class ImageDetect:
    thres=0.5
    root=Tk()
    root.title('Image View')
    root.iconbitmap('D:/Study Material/TY/Sem 2/Mini-Project/YOLOV3/')
    root.filename = filedialog.askopenfilename(initialdir="/YOLOV3/",title="select a file", filetypes =(("png files","*.png"),("all files","*.*")))
    my_label=Label(root,text=root.filename).pack()
    root.destroy()
    #my_image=ImageTk.PhotoImage(Image.open(root.filename))
    #my_image_label= Label(image=my_image).pack()
    #root.mainloop()
    img=cv2.imread(filedialog.askopenfilename(initialdir="/YOLOV3/",title="select a file", filetypes =(("png files","*.png"),("all files","*.*"))))
    classNames=[]
    classFiles='coco.names'
    with open(classFiles,'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')
    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'
    net = cv2.dnn_DetectionModel(weightsPath,configPath)
    net.setInputSize(320,320)
    net.setInputScale(1.0/127.5)
    net.setInputMean((127.5,127.5,127.5))
    net.setInputSwapRB(True)
    classIds, confs, bbox= net.detect(img,confThreshold=thres)
    print(classIds, bbox)
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox) :
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0],box[1]-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow("Output",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    root.destroy()
root = Tk()
obj =ImageDetect()
#root.mainloop()


