'''
Buatlah sebuah return function dengan 1 argumen yang akan menerima inputan bilangan integer(Seconds). Dan akan menghasilkan output string dengan format waktu ("HH:MM:SS").

HH : Hours, 2 digits, range: 00 - 99

MM : Minutes, 2 digits, range: 00 - 59

SS : Seconds, 2 digits, range: 00 - 59

Case Flow: Saat dieksekusi, program akan mencetak nilai return function.
'''


print('~'*20, "1. Time Converter", '~'*20)


def timeConverter():
    try:
        time = int(input("Masukkan waktu yang akan dikonversi (dalam detik) : "))
        if time < 0:
            return "Maaf, tidak menerima input negatif"
        elif time <= 359999:
            jam = time // 3600
            menit = (time % 3600) // 60
            detik = (time % 3600) % 60
            if jam < 10 and menit < 10 and detik < 10:
                return f"0{jam} : 0{menit} : 0{detik}"
            elif jam < 10 and menit < 10:
                return f"0{jam} : 0{menit} : {detik}"
            elif menit < 10 and detik < 10:
                return f"{jam} : 0{menit} : 0{detik}"
            elif jam < 10:
                return f"0{jam} : {menit} : {detik}"
            else:
                return f"{jam} : {menit} : {detik}"
        else:
            return "Maaf, maksimal 359999"
    except:
        return "Maaf, tidak menerima selain integer"


print(timeConverter())
