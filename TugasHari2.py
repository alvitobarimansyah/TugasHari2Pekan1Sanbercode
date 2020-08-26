# soal no 1

print(help(len))

# soal no 2

Apa itu built-in Function? built-in Function adalah fungsi bawaan dari python

Sebutkan 3 built-in Function di pyhon!
-len
-min
-max

word = 'saya adalah budi'

print(len(word))

angka = [20,15,8,30,40]

print(min(angka))

number = [20,15,8,30,40]

print(max(number))

# soal no 3

Apa perbedaan method dan function?
Method adalah sebuah fungsi yang dapat di pasang dalam sebuah class, sedangkan Function adalah sebuah fungsi yang tidak berada dalam class tetap

# soal no 4

kalimat = "Corona cepat selesai"

# uppercase
print(kalimat.upper())

# menghitung banyaknya jumlah e
print(str(kalimat.count('e')))

# soal no 5

obj_list = [11.25, 18.0, 20.0, 10.75, 9.50]
def mean_list(inp_list):
    obj_list = inp_list
    mean = sum(inp_list)/len(inp_list)
    return mean
    
print(mean_list(obj_list))

# soal no 6

obj_list = [2, 4, 5, 6]
obj_penambah = [1, 2, 3]

def kali_list(argumen1, argumen2):
    obj_list = argumen1
    obj_penambah = argumen2
    unite = argumen1 + argumen2
    return unite
    
print(kali_list(obj_list, obj_penambah))