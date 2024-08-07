from tkinter import Tk, Label, Frame, Button , LEFT , RIGHT
import gpiozero as gp
from time import sleep
import requests

class AlarmSystem:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.geometry("480x300")
        self.fenetre.resizable(width=False, height=False)
        self.defaultbg = self.fenetre.cget("bg")
        self.base_url = "http://127.0.0.1:5000"

        self.titre_app = Label(self.fenetre, text="PI Security GUI", font='bold')
        self.titre_app.pack()

        self.leftContainer = Frame(self.fenetre, width=170, height=240, border=10, borderwidth=2, relief="solid")
        self.leftContainer.pack(side=LEFT, padx=30, ipadx=10)

        self.frame_zone_1 = Frame(self.leftContainer, width=40, height=40, border=10, borderwidth=2, relief="solid")
        self.frame_zone_1.place(x=50, y=30)
        self.lbl_zone_1 = Label(self.frame_zone_1, text="Z1", font="bold")
        self.lbl_zone_1.pack()

        self.frame_zone_2 = Frame(self.leftContainer, width=40, height=40, border=10, borderwidth=2, relief="solid")
        self.frame_zone_2.place(x=100, y=30)
        self.lbl_zone_2 = Label(self.frame_zone_2, text="Z2", font="bold")
        self.lbl_zone_2.pack()

        self.frame_zone_3 = Frame(self.leftContainer, width=40, height=40, border=10, borderwidth=2, relief="solid")
        self.frame_zone_3.place(x=50, y=80)
        self.lbl_zone_3 = Label(self.frame_zone_3, text="Z3", font="bold")
        self.lbl_zone_3.pack()

        self.frame_zone_4 = Frame(self.leftContainer, width=40, height=40, border=10, borderwidth=2, relief="solid")
        self.frame_zone_4.place(x=100, y=80)
        self.lbl_zone_4 = Label(self.frame_zone_4, text="Z4", font="bold")
        self.lbl_zone_4.pack()


        self.frame_zone_on = Frame(self.leftContainer, width=40, height=40, border=10, borderwidth=2, relief="solid")
        self.frame_zone_on.place(x=50, y=160)
        self.lbl_zone_on = Label(self.frame_zone_on, text="ON", font="bold")
        self.lbl_zone_on.pack()

        self.frame_zone_off = Frame(self.leftContainer, width=40, height=40, border=10, borderwidth=2, relief="solid")
        self.frame_zone_off.place(x=100, y=160)
        self.lbl_zone_off = Label(self.frame_zone_off, text="OFF", font="bold")
        self.lbl_zone_off.pack()

        self.rigthContainer = Frame(self.fenetre, width=170, height=240, border=10, borderwidth=2, relief="solid")
        self.rigthContainer.pack(side=RIGHT, padx=30)

        self.btnActivateAlarm = Button(self.rigthContainer, text="Activate",command=self.activer, background="orange")
        self.btnActivateAlarm.place(x=10, y=60)

        self.btnDeactivateAlarm = Button(self.rigthContainer, text="Deactivate",command=self.desactiver, background="orange")
        self.btnDeactivateAlarm.place(x=10, y=110)

        self.btnResetAlarm = Button(self.rigthContainer, text="Reset",command=self.reinitialiser, background="orange")
        self.btnResetAlarm.place(x=10, y=160)


        
        self.sega = gp.LED(8)
        self.segb = gp.LED(9)
        self.segc = gp.LED(10)
        self.segd = gp.LED(11)
        self.sege = gp.LED(12)
        self.segf = gp.LED(17)
        self.segg = gp.LED(13)

        self.led_verte = gp.LED(21)

        self.btn = gp.Button(27)

        self.zone1 = gp.Button(22)
        self.zone2 = gp.Button(5)
        self.zone3 = gp.Button(6)
        self.zone4 = gp.Button(19)

        self.systemStatus = 0

        self.btn.when_pressed = self.activerdesactiver
        self.zone1.when_pressed = self.btnclick
        self.zone2.when_pressed = self.btnclick
        self.zone3.when_pressed = self.btnclick
        self.zone4.when_pressed = self.btnclick

        self.show0()

        self.fenetre.mainloop()

    def show0(self):
        # 0
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.off()
        self.sege.off()
        self.segf.off()
        self.segg.on()

    def show1(self):
        #1
        self.sega.on()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.on()
        self.segg.on()


    def show2(self):
        #2
        self.sega.off()
        self.segb.off()
        self.segc.on()
        self.segd.off()
        self.sege.off()
        self.segf.on()
        self.segg.off()  
        

    def show3(self):
        #3
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.off()
        self.sege.on()
        self.segf.on()
        self.segg.off() 


    def show4(self):
        #4
        self.sega.on()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.off()
        self.segg.off() 


    def show5(self):
        #5
        self.sega.off()
        self.segb.on()
        self.segc.off()
        self.segd.off()
        self.sege.on()
        self.segf.off()
        self.segg.off()  
    


    def show6(self):
        #6
        self.sega.off()
        self.segb.on()
        self.segc.off()
        self.segd.off()
        self.sege.off()
        self.segf.off()
        self.segg.off() 


    def show7(self):
        #7
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.on()
        self.segg.on()     



    def show8(self):
        #8
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.off()
        self.sege.off()
        self.segf.off()
        self.segg.off()  


    def show9(self):
        #9
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.off()
        self.segg.off()    



    def showA(self):
        #A
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.off()
        self.segf.off()
        self.segg.off()


    def cout_up(self):
        # 0
        self.show0()
        sleep(1)

        # 1
        self.show1()
        sleep(1)

        # 2
        self.show2()
        sleep(1)

        # 3
        self.show3()
        sleep(1)

        # 4
        self.show4()
        sleep(1)

        # 5
        self.show5()
        sleep(1)

        # 6
        self.show6()
        sleep(1)

        # 7
        self.show7()
        sleep(1)

        # 8
        self.show8()
        sleep(1)

        # 9
        self.show9()
        sleep(1)



    def cout_down(self):
        #9
        self.show9()    
        sleep(1)

        #8
        self.show8()  
        sleep(1)

        #7
        self.show7()   
        sleep(1)

        #6
        self.show6()  
        sleep(1)

        #5
        self.show5() 
        sleep(1)

        #4
        self.show4()  
        sleep(1)

        #3
        self.show3()    
        sleep(1)

        #2
        self.show2()  
        sleep(1)

        #1
        self.show1()    
        sleep(1)
        
        #0
        self.show0()
        sleep(1)



    
    

    def activer(self):
        response = requests.post(f"{self.base_url}/activer")
        if response.status_code == 200:
            self.systemStatus = response.json().get("status")
            if self.systemStatus == 1:
                self.cout_up()
                self.showA()
                self.led_verte.on()
                self.lbl_zone_on.configure(bg="green")
                self.lbl_zone_off.configure(bg=self.defaultbg)

    def activerdesactiver(self):
        response = requests.post(f"{self.base_url}/activerdesactiver")
        if response.status_code == 200:
            self.systemStatus = response.json().get("status")
            if self.systemStatus == 1:
                self.cout_up()
                self.showA()
                self.led_verte.on()
                self.lbl_zone_on.configure(bg="green")
                self.lbl_zone_off.configure(bg=self.defaultbg)
            elif self.systemStatus == 0:
                self.cout_down()
                self.show0()
                self.led_verte.off()
                self.lbl_zone_on.configure(bg=self.defaultbg)
                self.lbl_zone_off.configure(bg="red")

    def reinitialiser(self):
        response = requests.post(f"{self.base_url}/reinitialiser")
        if response.status_code == 200:
            self.systemStatus = response.json().get("status")
            if self.systemStatus == 1:
                self.showA()
                self.led_verte.on()
                self.lbl_zone_1.configure(bg=self.defaultbg)
                self.lbl_zone_2.configure(bg=self.defaultbg)
                self.lbl_zone_3.configure(bg=self.defaultbg)
                self.lbl_zone_4.configure(bg=self.defaultbg)
                self.lbl_zone_off.configure(bg=self.defaultbg)
                self.lbl_zone_on.configure(bg="green")

    def btnclick(self, button_id):
        response = requests.post(f"{self.base_url}/btnclick", json={"button_id": button_id})
        if response.status_code == 200:
            button_state = response.json().get("state")
            button_name = response.json().get("button")
            if self.systemStatus == 1:
                if button_id == 1:
                    self.show1()
                    self.lbl_zone_1.configure(bg="green")
                    self.led_verte.blink(on_time=0.2, off_time=0.2)
                elif button_id == 2:
                    self.show2()
                    self.lbl_zone_2.configure(bg="green")
                    self.led_verte.blink(on_time=0.2, off_time=0.2)
                elif button_id == 3:
                    self.show3()
                    self.lbl_zone_3.configure(bg="green")
                    self.led_verte.blink(on_time=0.2, off_time=0.2)
                elif button_id == 4:
                    self.show4()
                    self.lbl_zone_4.configure(bg="green")
                    self.led_verte.blink(on_time=0.2, off_time=0.2)

    def desactiver(self):
        response = requests.post(f"{self.base_url}/desactiver")
        if response.status_code == 200:
            self.systemStatus = response.json().get("status")
            if self.systemStatus == 0:
                self.cout_down()
                self.show0()
                self.led_verte.off()
                self.lbl_zone_on.configure(bg=self.defaultbg)
                self.lbl_zone_off.configure(bg="red")



alarm_system = AlarmSystem()
