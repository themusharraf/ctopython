# C dan Python ga

![DALL·E 2024-11-16 20 45 58 - A creative and visually appealing illustration showing an integration of C_C++ and Python  On the left, a blue box labeled 'C_C++' with a modern tech ](https://github.com/user-attachments/assets/77f41974-016d-4cb1-a3b0-232b1989044c)



### Commonds
- C codeni compilyatsiya qilib beradi
```shell
gcc main.c -o main
./main
```
--- 
- Python code ishga tushuradi
```shell
python3 main.py
```
---
- C da yozilgan code ni `.so` ga o'tkazib beradi
```shell
gcc -shared -o main.so -fPIC main.c
```
- `gcc`: Bu GNU Compiler Collection, C va boshqa tillar uchun keng qo'llaniladigan kompilyator.
- `-shared`: Bu parametr kompilyatorga umumiy kutubxona (yoki dinamik kutubxona) yaratishni aytadi. Umumiy kutubxona — bu kompilyatsiyadan o'tgan funksiya va ma'lumotlar to'plami bo'lib, ularni turli dasturlar ishlatishlari mumkin. Linux tizimlarida ushbu parametr odatda `.so` kengaytmasiga ega fayl yaratadi.
- `-o main.so`: Bu parametr chiqish fayl nomini belgilaydi. `-o` opsiyasi kompilyatorga chiqish faylini `main.so` deb nomlashni aytadi. Siz `main` o‘rniga kutubxonangiz uchun istalgan nomni qo‘yishingiz mumkin.
- `-fPIC`: Bu "Position-Independent Code" (Manzilga Bog'liq Bo'lmagan Kod) degan ma'noni anglatadi. Bu parametr kompilyatorga xotirada yuklangan aniq manzildan mustaqil bo'lgan mashina kodi yaratishni aytadi. Bu umumiy kutubxonalar uchun zarur, chunki ularni turli dasturlar tomonidan xotiraning turli manzillariga yuklash mumkin.
- `main.c`: Bu umumiy kutubxonaga kompilyatsiya qilinadigan manba fayl. `main.c` fayli siz yaratmoqchi bo'lgan umumiy kutubxona uchun kodni o'z ichiga oladi.
### Buyruq nima qiladi?
- Ushbu buyruq `main.c` faylini umumiy kutubxona `main.so` ga kompilyatsiya qiladi va manzilga bog'liq bo'lmagan kod yaratadi.

### Qachon ishlatiladi?
- Bu buyruqdan mustaqil bajariladigan dasturdan ko'ra, umumiy kutubxona yaratmoqchi bo'lganingizda foydalaniladi. Umumiy kutubxonalar turli dasturlar tomonidan ishlatilishi mumkin bo'lgan qayta ishlatiladigan kod yaratishda foydalidir, bu esa takrorlanishni kamaytiradi va yangilanishlarni osonlashtiradi.

### Example 1
```shell
// main.c
#include <stdio.h>

int main(){
    printf("Hi Python\n");
    return 0;
}
```
- Yuqoridagi C code ni Python code ga chaqirish
```python
# main.py
import ctypes

code = ctypes.CDLL("./main_1.so")

code.main()
```
- ishga tushurish 
```shell
gcc -shared -o main.so -fPIC main.c
python3 main.py
```
---

### Example 4

- C da `fibonacci` n-darajasini aniqlash funksiyasi
```shell
// main_4.c

int fib(int n) {
    if (n <= 1)
        return n;
    return fib(n-1) + fib(n-2);
}
```
- Bu Python da `fibonacci` n-darajasini aniqlash funksiyasi va C da yozilgan `fibonacci` func code ni chaqirib ishlatib farqini ko'ramiz
```python
import time

import ctypes

code = ctypes.CDLL('./main_4.so')

code.fib.argtypes = (ctypes.c_int,)
code.fib.restype = ctypes.c_int

n = 35  # N-ni aniqlash # noqa


# Fibonacci sonini Python'da hisoblash # noqa
def python_fib(n):
    if n <= 1:
        return n
    return python_fib(n - 1) + python_fib(n - 2)


# 1. Python kodini sinash # noqa
start_time = time.time()
python_result = python_fib(n)
python_time = time.time() - start_time
print(f"Python'da vaqt: {python_time:.6f} soniya, Natija: {python_result}")  # noqa

# 2. C kodini sinash # noqa
start_time = time.time()
c_result = code.fib(n)
c_time = time.time() - start_time
print(f"C'da vaqt: {c_time:.6f} soniya, Natija: {c_result}")  # noqa

# Vaqt farqini chiqaramiz # noqa
print(f"C kodining tezligi Python'dan {python_time / c_time:.2f} marta tezroq")  # noqa
```
- ishga tushurish 
```shell
gcc -shared -o main_4.so -fPIC main_4.c
python3 main_4.py
```
- Natija
```
Python'da vaqt: 1.116683 soniya, Natija: 9227465
C'da vaqt: 0.049001 soniya, Natija: 9227465
C kodining tezligi Python'dan 22.79 marta tezroq

```
Umid qilama sizga bu foydali buldi 😊 

Telegram address: [Engineering blog](https://t.me/musharrafme)
