kalori = 0

lari = input("Apakah kamu melakukan olahraga lari?  ")
if (lari == "ya"):
    menit = int(input("Berapa menit? "))
    kalori += menit * (60 / 5)

pushUp = input("Apakah kamu melakukan olahraga push-up?")
if (pushUp == "ya"):
    menit = int(input("Berapa menit? "))
    kalori += menit * (200 / 30)
    
plank = input("Apakah kamu melakukan olahraga plank?")
if (plank == "ya"):
    menit = int(input("Berapa menit? "))
    kalori += menit * 5

kalori = int(kalori)

if (kalori > 0):
    print(f"\nKalori yang terbakar dari tubuhmu adalah {kalori} kalori")
else:
    print("\nTidak ada kalori yang terbakar, kamu tidak berolahraga :")