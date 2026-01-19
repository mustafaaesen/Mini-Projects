import smtplib
from email.mime.multipart import MIMEMultipart# mesaj göbdesii için
from email.mime.text import MIMEText#mesaj göbdesi içerği için
import sys# ekrandaki hata mesajları


#mail yapısı oluşturma

mesaj=MIMEMultipart() # mimemultipart sınıfından mesaj oluşturma

mesaj["From"]="mailhesabiniz@mail.com"# mailin geleceği e posta adresi

mesaj["To"]="mailhesabiniz@mail.com"# mailin gideceği e posta adresi

mesaj["Subject"]="SMTP Mail Deneme"#mailin konusu

yazi="""

SMTP ile MAİL GÖNDERİMİ

MUSTAFA ESEN

"""#mesajın içerği

mesaj_govdesi=MIMEText(yazi,"plain")#mesaj gövdesi 

mesaj.attach(mesaj_govdesi)#mesaj gövdesini tetikleyen fonksiyon

#Maili göndermek için gmail bağlantıları ve bu bağlantılarda oluşabilecek hatalar için try except blokları

try:
    mail=smtplib.SMTP("smtp.gmail.com",587)# nereye bağlanacağımızı ve hangi portu kullancağımızı parametre olarak verdik

    mail.ehlo()#smtp bağlantısı ve tanıtımı

    mail.starttls()# mailin encrypt edilerek göndrimi

    mail.login("mailtohesabiniz@gmail.com","google uygulama şifreniz")#mail adresi ve şifre bilgisi
    #google hesabından 2FA açık şekilde uygulama şifresi oluşturup giriş yapılmalı. Mail şifresi
    #artık kabul edilmiyor

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())#mail gönderme bilgileri

    print("Mail Gönderimi Başarılı")

    mail.close()#smtp server bağlantı kesimi


except:
    sys.stderr.write("Bir Sorun Oluştu")
    sys.stderr.flush()
