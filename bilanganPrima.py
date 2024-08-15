batasBawah = int (input("Masukan batas bawah: "))
batasAtas = int (input("Masukan batas atas: "))
print("bilangan prima dalam rentang", batasBawah, "hingga", batasAtas, "adalah: ")

nilai = batasBawah

while nilai <= batasAtas :
    if nilai > 1 :
        i = 2 
        while i <= nilai // 2 :
            if nilai % i == 0 :
                break
            i += 1
        else :
            print(nilai)
    nilai += 1