from smtplib import SMTP ## kullandigimiz protoklün ismi bu

try :
    subject = "Python"
    message = input("Gönderilecek mesaji seçin: ") + "\nby ibrahimaksan :)"

    content = f"Subject : {subject}\n\n{message}"

    myadress = "yourmaailadress"
    mypassword = "your password" # guvenlik icin dosyadan cekmek daha mantıklı olablir.

    othermail = input("Diger mail adresini giriniz: ")

    Mail = SMTP(host= "smtp-mail.outlook.com", port= 587)
    Mail.ehlo() ## sunucya bağlanmak için gerekli 
    Mail.starttls() ##verilerimi sunucya şifreli bir şekilde göndermek için bu protokol lazım.

    Mail.login(myadress, mypassword)
    Mail.sendmail(myadress, othermail, content.encode("utf-8"))

    print("Mailiniz ibrahim aksan tarafından yazılan programla SMTP protokolü ile gönderildi :D")

except Exception as ex:

    print("mail gönderimi basarisiz oldu !!!")