import cv2
class VisionApp:
    def __init__(self):
        self.cascad=cv2.CascadeClassifier(r"C:\Users\263\OneDrive\Desktop\vision\haarcascade_frontalface_default.xml")
        self.profile_cascad=cv2.CascadeClassifier(r"C:\Users\263\OneDrive\Desktop\vision\haarcascade_profileface.xml")
        self.cap=cv2.VideoCapture(0)
        
        self.Father=1
        self.Mother=1
        self.Grandma=1
        self.Misha=1
        self.Mediana=1
        self.Pasha=1
    def video_capture(self):
            while True:
                success,frame=self.cap.read()
                if success==False:
                     print("не удается запустить камеру")
                     break
               
                key=cv2.waitKey(1)&0xFF
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
                    self.Pasha+=1

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
                cv2.imshow("Мой видеопоток",frame)
                cv2.waitKey(1)
            cv2.destroyAllWindows()   
                    
                    
             

if __name__=="__main__":
    app=VisionApp()
    app.video_capture()
