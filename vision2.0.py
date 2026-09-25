import cv2
class Video_source:
    def __init__(self):
        self.cap=cv2.VideoCapture(0)
    def frame(self):
            success,frame=self.cap.read()
            self.video=cv2.VideoWriter_fourcc('m','p','4','v')
            return success,frame
    def exit(self):
          self.cap.release()
class securityanalyzer:
    def __init__(self):
        self.cascad=cv2.CascadeClassifier(r"C:\Users\263\OneDrive\Desktop\vision\haarcascade_frontalface_default.xml")          
        self.cascad_profile=cv2.CascadeClassifier(r"C:\Users\263\OneDrive\Desktop\vision\haarcascade_profileface.xml")
        self.previous_frame=None
    def video_capture(self,frame):
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        if self.previous_frame is None:
            self.previous_frame=gray_frame
            return frame,gray_frame,0
        diff_frame=cv2.absdiff(self.previous_frame,gray_frame)
        summ_frame=diff_frame.sum()
       
        self.faces=self.cascad.detectMultiScale(gray_frame,1.1,4)
        if len(self.faces)==0:
            self.faces=self.cascad_profile.detectMultiScale(gray_frame,1.1,4)
        for(x,y,w,h) in self.faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.rectangle(gray_frame,(x,y),(x+w,y+h),(0,255,0),2)
        self.previous_frame=gray_frame
        return frame,gray_frame,summ_frame

        
        
class Visionapp:
    def __init__(self):
        self.source=Video_source()
        self.analyzer=securityanalyzer()
        self.is_recording=False
        self.frame_counter=0
        self.video_writer=None
        self.sh=1
        self.fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
    def run(self):
        while True:
            success,frame=self.source.frame()
            if success==False:
                break 
            procframe,gray,motion_score=self.analyzer.video_capture(frame)
            if motion_score>2000000 and self.is_recording==False:
                print("warning,motion detected")
                self.is_recording=True
                self.frame_counter=0
                self.video_writer=cv2.VideoWriter(f"alert_{self.sh}.mp4",self.fourcc,30.0,(640,480))
               
            if self.is_recording==True:
                self.video_writer.write(procframe)
                self.frame_counter+=1
                if self.frame_counter>=150:
                    self.is_recording=False
                    self.video_writer.release()
                    self.sh+=1
            
           
            cv2.imshow("моя вебка",procframe)
            cv2.imshow("для нейросети",gray)
            if cv2.waitKey(1)&0xFF==ord("q"):
                break 
        self.source.exit()
        cv2.destroyAllWindows()
if __name__=="__main__":
    app=Visionapp()
    app.run()
    
          
            
              
