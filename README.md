# C dan Python-ga

![image](https://github.com/user-attachments/assets/d05f9c22-b8e2-4a8e-af88-0e74170cbfdd)

### Commonds
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
- Bu buyruqdan mustaqil bajariladigan dasturdan ko'ra, umumiy kutubxona yaratmoqchi bo'lganingizda foydalaniladi. Umumiy kutubxonalar turli dasturlar tomonidan ishlatilishi mumkin bo'lgan qayta ishlatiladigan kod yaratishda foydalidir, bu esa takrorlanishni kamaytiradi va yangilanishlarni osonlashtirad