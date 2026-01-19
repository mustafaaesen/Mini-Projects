import requests
import sys
#fixer io üzerinden euro bazlı döviz kurlarını çekip döviz çevirici yapan programdır.

#kullanıcıdan aldığı çevirilecek para birimi ve hedef para birimini euro kuru üzerinden çeşitli işlemler
#ile çevirip kullanıcıya sonucu gösterir.

"""
Kullanıcıdan alınan para birimine göre 3 yolla yaklaşım mevcuttur

kaynak ve hedef para birimi de euro değilse:
    miktar/kaynak kuru ile hedef kur değerinin çarpımı

kaynak euro ise:
     miktar ile hedef kurun çarpımı

hedef euro ise:
    miktar ile kaynak kurun bölümü
"""


ACCESS_KEY = "fixer.io hesabı oluşturup edindiğiniz access keyiniz"
url = f"http://data.fixer.io/api/latest?access_key={ACCESS_KEY}"
#siteden döviz bilgisi çekilmesi


try:
    response=requests.get(url, timeout=10) # bağlantıdaki biglilerin alındığı response değişkeni
    response.raise_for_status()#HTTP hataları için

except requests.exceptions.RequestException as e:
    sys.exit(f"Ağ İstek Hatası: {e}")


try:
    json_veri=response.json()#çekilen bilginin json formatına dönüştürme

except ValueError:
    sys.exit("HATA: Sunucudan JSON formatında veri alınamadı.")



#apı isteği başarılı olsa da key yanlışlığı gibi durumlarda değerler boş dönebilir
#bu durumun kontorlü için

if not json_veri.get("success", True):
    err=json_veri.get("error", {})
    sys.exit(f"Fixer API hatası (code={err.get('code')} type={err.get('type')}): {err.get('info','')}")

rates=json_veri.get("rates", {}) # kurların sözlüğe alınması

if not isinstance(rates,dict) or not rates:
    sys.exit("HATA: 'rates' verisi bulunamadı") #kurların kotnrolü

rates["EUR"]=1.0 # granti için euro yu 1 e ayarlama



#para birimlerinin olup olmadığının kotnrolü

def menu():
    print("\n=== KULLANIM ===")
    print("• Kaynak/Hedef para birimini ISO koduyla gir (örn. TRY, USD, EUR).")
    print("• Miktarı sayı olarak gir (örn. 100 veya 99.5).")
    print("• '?' → bu menüyü gösterir, boş/ 'q' → çıkış.\n")
    # örnek olması için ilk 25 kodu yazalım
    print("Desteklenen para birimlerinden örnekler:")
    for i, code in enumerate(sorted(rates.keys())):
        print(" ", code, end="")
        if i >= 24:
            print(f" ... (toplam {len(rates)} birim)")
            break
    print("\n")


def cevir(amount:float,src:str, dst:str, rates:dict)->float:#fonksiyon parametreleri döndüreceği veri tipi
    """src birimden dst birimine amount değerini çevirip geri döndürür"""

    if src==dst:
        return float(amount)
    
    if src=="EUR":

        return float(amount) * float(rates[dst])# kaynak para birimi euro ise miktar ve değerin çarpımı
    
    if dst=="EUR":
        if float(rates[src])==0.0: # kur 0 olma ihtimali
            raise ZeroDivisionError(f"{src} kuru 0 olamaz")
        return float(amount) / float(rates[src]) # hedef kur euro ise bölme
    
    if float(rates[src])==0.0: # iki kurun da eoru olmadığında 0 kontrolü

        raise ZeroDivisionError(f"{src} kuru 0 olamaz")
    return (float(amount) / float(rates[src])) * float(rates[dst]) # iki kurun da euro dışı olduğu durumlar

print("💱 Döviz Dönüştürücü (Fixer.io / Taban Kur=EUR)")
menu()

while True:
    doviz1=input("Çevirilecek Döviz Kurunu Seçiniz (ör.TRY, '?'-->menü, boş/q-->çıkış)").strip()

    if not doviz1 or doviz1.lower()=="q":
        print("Güle Güle...")
        break
    if doviz1 == "?":
        menu()
        continue
    #ilk değişkene q veya menye gitme girdisi yapılmışsa

    doviz1=doviz1.upper()#girilen karakteri büyük harfe çevirme

    doviz2=input("Çevirileceği Hedef Kuru Seçiniz (ör.USD, '?'-->menü, boş/q-->çıkış)").strip()

    if not doviz2 or doviz2.lower()=="q":
        print("Güle Güle...")
        break
    if doviz2== "?":
        menu()
        continue

    doviz2=doviz2.upper()

    #Girilen pra birimlerinin desteklenip desteklenmediğinin kontrolü

    if doviz1 not in rates:
        print(f"HATA: Desteklenmeyen Kaynak Para Birimi: {doviz1}\n")
        continue

    if doviz2 not in rates:
        print(f"HATA: Desteklenmeyen Hedef Para Birimi {doviz2}\n")
        continue
    

    miktar_str=input("Çevirilecek Miktarı Giriniz (ör.100, '?'-->menü, boş/q-->çıkış)").strip()

    if not miktar_str or miktar_str.lower()=="q":
        print("Güle Güle...")
        break
    if miktar_str=="?":
        menu()
        continue
    
    miktar_str=miktar_str.replace(",",".")

    try:
        miktar=float(miktar_str)# str den integer a dönüş
    
    except ValueError:
        print("HATA: Sayısal Bir Miktar Giriniz ör.100 veya 99.5\n")
        continue

    #hesaplama işlemleri ve çıktı

    try:
        sonuc=cevir(miktar,doviz1,doviz2,rates)#çevir fonksiyonu ile hesaplama
    
    except Exception as e:
        print("Dönüşüm Hatası: {e}\n")
        continue

    print(f"\n{miktar} {doviz1} ≈ {sonuc:.4f} {doviz2}\n")


        


