# Mini Projects

Bu repository, öğrenme ve geliştirme sürecinde yapılan
mini projelerin paylaşıldığı bir çalışma alanıdır.

Buradaki çalışmalar, büyük ve kapsamlı uygulamalara geçmeden önce
temel konuları pekiştirmek, farklı kütüphaneleri denemek
ve terminal tabanlı uygulama mantığını öğrenmek amacıyla
geliştirilmiştir.

Zamanla bu repo, benzer nitelikte yeni mini projeler
oldukça genişletilecektir.

---

## Repo İçeriği

### dovizcevirici.py

Bu proje, Python kullanılarak geliştirilen
terminal tabanlı bir döviz çevirici uygulamasıdır.

- Fixer.io API üzerinden EUR bazlı güncel döviz kurları çekilir
- Kullanıcıdan kaynak para birimi, hedef para birimi ve miktar alınır
- Dönüşüm işlemi farklı senaryolar (EUR → EUR olmayan, EUR olmayan → EUR vb.)
dikkate alınarak hesaplanır
- API bağlantı hataları ve kullanıcı girişleri için temel hata kontrolleri yapılmıştır

Amaç, bir dış API ile çalışma, veri çekme ve bu veriyi
mantıksal işlemlerle kullanma pratiği kazanmaktır.

---

### smtp.py

Bu proje, Python kullanılarak SMTP protokolü üzerinden
e-posta gönderimini simüle eden terminal tabanlı bir çalışmadır.

- SMTP bağlantısı kurulmuştur
- TLS ile güvenli bağlantı sağlanmıştır
- MIME yapısı kullanılarak e-posta içeriği oluşturulmuştur
- Gönderim sırasında oluşabilecek hatalar için temel kontroller eklenmiştir

Amaç, SMTP mantığını öğrenmek ve Python ile
e-posta gönderim sürecini deneyimlemektir.
