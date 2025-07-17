from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import csv
import speech_recognition
import wave

class Mainclass:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('1280x800+150+12')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        self.loginPage()
    
   
    def loginPage(self):
        self.mainframe = Frame(self.root, bg='white')
        self.mainframe.place(x=-2,y=-2)
        self.img1 = PhotoImage(file="images/loginPage.png")
        Label(self.mainframe, image=self.img1, bg='white').pack()

        self.user1 = Entry(self.mainframe, width=25, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.user1.place(x=530, y=325)
        self.user1.insert(0, 'Username')
        self.user1.bind('<FocusIn>', self.on_enter)
        self.user1.bind('<FocusOut>', self.on_leaveuser)

        self.code1 = Entry(self.mainframe, width=19, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.code1.place(x=530, y=403)
        self.code1.insert(0, 'Password')
        self.code1.bind('<FocusOut>', self.on_leavepas)
        self.code1.bind('<FocusIn>', self.on_enterpas)

        self.hide_image = PhotoImage(file='images\\show.png')
        self.show_image = PhotoImage(file='images\\hide.png')

        self.show_button = Button(self.mainframe, image=self.show_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=785, y=407)
        
        self.tombol = Button(self.mainframe, width=19, pady=7, text='Get Started', bg='#004AAD', fg='white', border=0,font=('Poppins', 14),cursor='hand2',activebackground='#004AAD',command=self.signin).place(x=531, y=483)
        
        self.sign_up_button = Button(self.mainframe, width=13, text='Create Account',font=('Poppins', 12), border=0, bg='#737373', cursor='hand2', fg='white', activebackground='#737373',command=self.RegisterPage)
        self.sign_up_button.place(x=456, y=553)
        
        self.need_help = Button(self.mainframe, width=9, text='Need Help?',font=('Poppins', 11), border=0, bg='#737373', cursor='hand2', fg='white', activebackground='#737373', command= self.help)
        self.need_help.place(x=728, y=553)

        self.exit_button = Button(self.mainframe, width=6, text='Exit', border=1, fg='#57a1f8', bg='white', cursor='hand2',command=self.root.destroy).place(x=1200, y=20)

    def RegisterPage(self):
        self.second_frame = Frame(self.root,width=1280,height=800, bg='white').place(x=-2,y=-2)
        self.img2 = PhotoImage(file="images/registerPage.png")
        Label(self.second_frame, image=self.img2, bg='white').place(x=-2,y=-2)


        self.user2 = Entry(self.second_frame, width=25, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.user2.place(x=530, y=280)
        self.user2.insert(0, 'Username')
        self.user2.bind('<FocusIn>', self.on_enter)
        self.user2.bind('<FocusOut>', self.on_leaveuser)

        self.code2 = Entry(self.second_frame, width=19, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.code2.place(x=530, y=360)
        self.code2.insert(0, 'Password')
        self.code2.bind('<FocusOut>', self.on_leavepas)
        self.code2.bind('<FocusIn>', self.on_enterpas)
        
        self.retype_code = Entry(self.second_frame, width=19, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.retype_code.place(x=530, y=440)
        self.retype_code.insert(0, 'Re-type Password')
        self.retype_code.bind('<FocusOut>', self.retype)
        self.retype_code.bind('<FocusIn>', self.on_enter)

        self.hide_image2 = PhotoImage(file='images\\show.png')
        self.show_image2 = PhotoImage(file='images\\hide.png')

        self.show_button2 = Button(self.second_frame, image=self.show_image2, command=self.show2, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button2.place(x=785, y=363)
        
        self.retype2 = Button(self.second_frame, image=self.show_image2, command=self.showRetype2, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.retype2.place(x=785, y=443)

        self.tombol2 = Button(self.second_frame, width=19, pady=7, text='Register', bg='#004AAD', fg='white', border=0,font=('Poppins', 14),cursor='hand2',activebackground='#004AAD',command=self.signup)
        self.tombol2.place(x=531, y=510)
        
        self.login2_button = Button(self.second_frame, width=4, text='Login',font=('Poppins', 11), border=0, bg='#737373', cursor='hand2', fg='white', activebackground='#737373',command=self.loginPage)
        self.login2_button.place(x=465, y=580)
        self.need_help2 = Button(self.second_frame, width=9, text='Need Help?',font=('Poppins', 11), border=0, bg='#737373', cursor='hand2', fg='white', activebackground='#737373', command= self.help)
        self.need_help2.place(x=730, y=580)

        self.exit_button = Button(self.second_frame, width=6, text='Exit', border=1, fg='#57a1f8', bg='white', cursor='hand2', command=self.root.destroy).place(x=1200, y=20)

    def Entree(self):
        self.entreeFrame = Frame(self.root,width=1280,height=800, bg='white').place(x=-2,y=-2)
        self.img3 = PhotoImage(file="images/entreePage.png")
        Label(self.entreeFrame, image=self.img3, bg='white').place(x=-2,y=-2)

        self.nama = Entry(self.entreeFrame, width=22, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.nama.place(x=162,y=235)
        
        self.NIM = Entry(self.entreeFrame, width=22, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.NIM.place(x=162,y=370)

        self.Kelas = Entry(self.entreeFrame, width=22, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.Kelas.place(x=162,y=505)
        
        self.JudulSeminar = Entry(self.entreeFrame, width=22, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.JudulSeminar.place(x=525,y=235)

        self.Pembicara = Entry(self.entreeFrame, width=22, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.Pembicara.place(x=525,y=370)
        
        self.HariTanggal = Entry(self.entreeFrame, width=22, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.HariTanggal.place(x=525,y=505)

        self.Pukul1 = Entry(self.entreeFrame, width=8, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.Pukul1.place(x=887,y=235)
        
        self.pukul2 = Entry(self.entreeFrame, width=8, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.pukul2.place(x=1050,y=235)

        self.Tempat = Entry(self.entreeFrame, width=22, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.Tempat.place(x=887,y=370)

        self.submitButton = Button(text='Submit',bg='#004AAD',activebackground='#004AAD',fg='White',border=0,font=('Poppins', 14),width=30,cursor='hand2',command=self.mainPage)
        self.submitButton.place(x=480,y=615)

        self.exit_button = Button(self.entreeFrame, width=6, text='Exit', border=1, fg='#57a1f8', bg='white', cursor='hand2', command=self.root.destroy).place(x=1200, y=20)
        self.logout_button = Button(self.entreeFrame, width=6, text='Log Out', border=1, fg='#57a1f8', bg='white', cursor='hand2', command=self.logout).place(x=20, y=20)


    
    def mainPage(self):
        self.third_frame = Frame(self.root, width=1280, height=800, bg='white').place(x=-2, y=-2)
        self.img2 = PhotoImage(file="images/mainPage.png")
        Label(self.third_frame, image=self.img2, bg='white').place(x=-2, y=-2)

        self.teks = Text(self.third_frame, height=29, width=90, wrap="word", font=('Poppins', 12), bg='#F0F0F0', fg='#333333')
        self.teks.place(x=130,y=150)
        self.teks.insert("end", 'Nama : '+ self.nama.get() + '\n' + 'NIM : ' + self.NIM.get() + '\n' + 'Kelas : ' + self.Kelas.get() + '\n\n' + 'Judul Seminar : ' + self.JudulSeminar.get() + '\n' + 'Pembicara : ' + self.Pembicara.get() + '\n' + 'Hari/Tanggal : ' + self.HariTanggal.get() + '\n' + 'Pukul : ' + self.Pukul1.get()+ ' ' + '-' + ' ' + self.pukul2.get() +'\n' + 'Tempat : ' + self.Tempat.get() + '\n\n')

        self.namaFile = Entry(self.entreeFrame, width=17, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.namaFile.place(x=1000,y=198)
        self.namaFile.insert(0, 'Masukkan Nama File')
        self.namaFile.bind('<FocusIn>', self.on_enter)
        self.namaFile.bind('<FocusOut>', self.on_leaveFileName)

        self.Speech_button = Button(text='Record',bg='#004AAD',activebackground='#004AAD',fg='white',border=0,font=('Poppins', 14),width=12,cursor='hand2',command=self.UpdateTampilan)
        self.Speech_button.place(x=1025,y=275)

        self.saveButton = Button(text='Save to File',bg='#004AAD',activebackground='#004AAD',fg='white',border=0,font=('Poppins', 14),width=12,cursor='hand2',command=self.saveFile)
        self.saveButton.place(x=1025,y=355)
        
        self.dropdown_var = StringVar(root)
        options = ["Indonesia", "Inggris"]

        self.MasukkanBahasa = Label(text="Masukkan Bahasa").place(x=1035,y=430) 
        self.dropdown_menu = ttk.Combobox(root, textvariable=self.dropdown_var, values=options)
        self.dropdown_menu.place(x=1035,y=450) 

        self.exit_button = Button(self.third_frame, width=6, text='Exit', border=1, fg='#57a1f8', bg='white', cursor='hand2', command=self.root.destroy).place(x=1200, y=20)
        self.backButton = Button(self.third_frame, width=6, text='Back', border=1, fg='#57a1f8', bg='white', cursor='hand2', command=self.Entree).place(x=20, y=20)

        
    
    def saveFile(self):
        if self.namaFile.get() == 0 or self.namaFile.get() == 'Masukkan Nama File':
            showerror('Error','Silahkan Isi Nama File yang anda inginkan (tanpa format dokumen)')
        else:
            filename = f'database\{self.user1.get()}\{self.namaFile.get()}.txt'
            with open(filename,'w') as file:
                file.write(self.teks.get("1.0", "end-1c"))
                showinfo('Succses','File berhasil dibuat')
            
        
    def logout(self):   
        sure = askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.loginPage()

    def help(self):
        showinfo('coba','ini coba')

    def on_leaveFileName(self,e):
        widget = e.widget
        text = widget.get()
        if text == '':
            widget.insert(0, 'Masukkan Nama File')

    def on_enter(self, e):
        widget = e.widget
        widget.delete(0, 'end')

    def on_leaveuser(self, e):
        widget = e.widget
        text = widget.get()
        if text == '':
            widget.insert(0, 'Username')
    
    def on_enterpas(self, e):
        widget = e.widget
        widget.delete(0, 'end')

    def on_leavepas(self, e):
        widget = e.widget
        text = widget.get()
        if text == '':
            widget.insert(0, 'Password')

    def retype(self, e):
        widget = e.widget
        text = widget.get()
        if text == '':
            widget.insert(0, 'Re-type Password')

    def show(self):
        self.hide_button = Button(self.mainframe, image=self.hide_image, command=self.hide, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=785, y=407)
        self.code1.config(show='*')
 
    def hide(self):
        self.show_button1 = Button(self.mainframe, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button1.place(x=785, y=407)
        self.code1.config(show='')   


    def show2(self):
        self.hide_button2 = Button(self.second_frame, image=self.hide_image2, command=self.hide2, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button2.place(x=785, y=363)
        self.code2.config(show='*')

    def hide2(self):
        self.show_button2 = Button(self.second_frame, image=self.show_image2, command=self.show2, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button2.place(x=785, y=363)
        self.code2.config(show='')  

    def showRetype2(self):
        self.hide_retype2 = Button(self.second_frame, image=self.hide_image2, command=self.hideRetype2, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_retype2.place(x=785, y=443)
        self.retype_code.config(show='*')


    def hideRetype2(self):
        self.show_button2 = Button(self.second_frame, image=self.show_image, command=self.showRetype2, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button2.place(x=785, y=443)
        self.retype_code.config(show='')   
   
    def signin(self):
        with open("./database/Login.csv", mode="r") as f:
            reader = csv.reader(f, delimiter=",")
            if self.user1.get() == 0 or self.user1.get() == 'Username':
                showerror('Error','Username belum diisi')
            else:
                for i in reader:
                    if i == [self.user1.get(), self.code1.get()]:
                        showinfo(title="Login Success", message="You Successfully Login")
                        self.Entree()
                        return
                showinfo(title="Error", message="Invalid Password")

    def username_check(self, username):
        with open('./database/Login.csv', 'r') as file:
            reader = csv.reader(file)
            data_lower = [row for row in reader]

            for row in data_lower:
                if row[0].lower() == username.lower():
                    return True
        return False

    def signup(self):
        username = self.user2.get()
        password = self.code2.get()
        confirm_password = self.retype_code.get()

        if username == 0 or username == 'Username' or password == 0 or password == 'Password' or confirm_password == 0 or confirm_password == 'Re-type Password':
            showerror('Error','Semua kolom wajib diisi')
        elif self.username_check(username):
            showerror("Peringatan", "Akun sudah pernah dibuat")
        else:
            if username == 'Username' or username == 0:
                showerror("Invalid", "Username dont exist")
            elif password == 'Password' or password == 0:
                showerror("Invalid", "Password dont exist")
            elif password != confirm_password:
                showerror("Invalid", "Both Password shouldn't match")
            else:
                with open('./database/Login.csv', 'a+', newline='') as f:
                    template = [username, password]
                    write = csv.writer(f, template)
                    write.writerow(template)
                    showinfo('Sign Up', 'Successfully sign up')

    def Speech(self):
        self.recognizer = speech_recognition.Recognizer()

        try:
            if self.dropdown_menu.get() == 'Indonesia':
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                    self.audio_data = self.recognizer.listen(mic)  # Record the entire file
                    self.hasilSpeech = self.recognizer.recognize_google(self.audio_data, language='id')
                
                tanya = askyesno("Save", "Apakah anda ingin menyimpan hasil suara")
                if tanya == True:
                    wave_file_path = "database/hasil_rekaman.wav"
                    with wave.open(wave_file_path, 'w') as wave_file:
                        wave_file.setnchannels(1)
                        wave_file.setsampwidth(2) 
                        wave_file.setframerate(44100) 
                        wave_file.writeframes(self.audio_data.frame_data)
                        showinfo('Sucsess','File telah disimpan')
                else:
                    pass

            elif self.dropdown_menu.get() == 'Inggris':
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                    self.audio_data = self.recognizer.listen(mic) 
                    self.hasilSpeech = self.recognizer.recognize_google(self.audio_data, language='en')
                
                tanya = askyesno("Save", "Apakah anda ingin menyimpan hasil suara")
                if tanya == True:
                    wave_file_path = "database/hasil_rekaman.wav"
                    with wave.open(wave_file_path, 'w') as wave_file:
                        wave_file.setnchannels(1) 
                        wave_file.setsampwidth(2)  
                        wave_file.setframerate(44100) 
                        wave_file.writeframes(self.audio_data.frame_data)
                        showinfo('Sucsess','File telah disimpan')
                else:
                    pass
            else:
                showerror('Error','masukkan bahasa yang anda inginkan')


        except:
            showerror('Error','Something wrong')
            self.Mulailabel.place_forget()

    def UpdateTampilan(self):
        Label(self.third_frame,text=f"Speech Recognition berbahasa {self.dropdown_menu.get()}",width=40, fg='#737373', border=0, bg='white',font=('Poppins', 14)).place(x=300,y=650)
        self.Mulailabel = Label(self.third_frame, text='Recording',width=15, fg='#737373', border=0, bg='white',font=('Poppins', 14))
        self.Mulailabel.place(x=1035,y=500)  
        self.Mulailabel.update() 
        self.Mulailabel.after(1000, self.processSpeech) 

    def processSpeech(self):
        self.Speech()
        hasilText = self.hasilSpeech
        self.teks.insert("end", "\n" + hasilText)
        self.Mulailabel.place_forget()
    

if __name__ == "__main__":
    root = Tk()
    app = Mainclass(root)
    root.mainloop()


