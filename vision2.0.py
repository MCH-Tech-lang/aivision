import cv2
class vision_camera:
    def __init__(self):
        self.cap=cv2.VideoCapture(0)
        self.cascad=cv2.CascadeClassifier(r"C:\Users\263\OneDrive\Desktop\vision\haarcascade_frontalface_default.xml")
        self._cascad_profile=cv2.CascadeClassifier(r"C:\Users\263\OneDrive\Desktop\vision\haarcascade_profileface.xml")
        self.Father=1
        self.Mother=1
        self.Grandma=1
        self.Pasha=1
        self.Misha=1
        self.Mediana=1
        self.previous_frame=None
    def video_capture(self):
        
        while True:
            success,frame=self.cap.read()
            key=cv2.waitKeyEx(1)&0xFF
            
            gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            if self.previous_frame is None:
                self.previous_frame=gray_frame
                continue
           
            diff_frame=cv2.absdiff(self.previous_frame,gray_frame)
            summ_frame=diff_frame.sum()
            if summ_frame>2000000:
                print("[WARNING]Motion detected!")    
            self.faces=self.cascad.detectMultiScale(gray_frame,1.1,4)
            if len(self.faces)==0:
                self.faces=self._cascad_profile.detectMultiScale(gray_frame,1.1,4)
            for(x,y,w,h) in self.faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.rectangle(gray_frame,(x,y),(x+w,y+h),(0,255,0),2)
        
            if key==ord("P"):
                cv2.imwrite(f"father_{self.Father}.jpg",frame)
                print(f" фото номер {self.Father} Отца сохранен")
                self.Father+=1
            if key==ord("M"):
                cv2.imwrite(f"mother_{self.Mother}.jpg",frame)
                print(f"фото номер {self.Mother} Мамы есть")
                self.Mother+=1
            if key==ord("b"):
                cv2.imwrite(f"babushka_{self.Grandma}.jpg",frame)
                print(f"фото номер {self.Grandma} бабушки есть")
                self.Grandma+=1
            if key==ord("p"):
                cv2.imwrite(f"pasha_{self.Pasha}.jpg",frame)
                print(f"фото номер {self.Pasha} Паши есть")
                self.Pasha+=1
            if key==ord("m"):
                cv2.imwrite(f"Misha_{self.Misha}.jpg",frame)
                print(f"Фото номер {self.Misha} Миши сохранен")
                self.Misha+=1
            if key==ord("d"):
                cv2.imwrite(f"mediana_{self.Mediana}.jpg",frame)
                print(f"фото номер {self.Mediana} Медианы сохранен")
                self.Mediana+=1
            if key==ord("q"):
                break
            self.previous_frame=gray_frame
            cv2.imshow("Мое видео",frame)
            cv2.imshow("Видео для нейросети",gray_frame)
                      
if __name__=="__main__":
    my_camera=vision_camera()
    my_camera.video_capture()
