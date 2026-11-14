#1
def buyurtma_hisobla(*args, **kwargs):
    chegirma_foizi = kwargs.get("chegirma_foizi", 0)
    yetkazib_narxi = kwargs.get("yetkazib_berish_narxi", 0)
    soliq_foizi = kwargs.get("soliq_foizi", 0)
    bepul_limit = kwargs.get("bepul_yetkazib_berish_limiti", 0)

    umumiy_narx = sum(args)
    chegirma_summasi = umumiy_narx * chegirma_foizi / 100
    chegirmadan_keyin = umumiy_narx - chegirma_summasi
    soliq_summasi = chegirmadan_keyin * soliq_foizi / 100

    if chegirmadan_keyin >= bepul_limit:
        yetkazib = 0
    else:
        yetkazib = yetkazib_narxi

    jami = chegirmadan_keyin + soliq_summasi + yetkazib

    print(f"Mahsulot umumiy narxi: {umumiy_narx:.2f}")
    print(f"Chegirma: ({chegirma_foizi}%): -{chegirma_summasi:.2f}")
    print(f"Chegirmadan keyingi summa: {chegirmadan_keyin:.2f}")
    print(f"soliq ({soliq_foizi}%): +{soliq_summasi:.2f}")
    print(f"Yetkazib_berish: {yetkazib:.2f}")
    print(f"Umumiy to'lov: {jami:.2f}")

buyurtma_hisobla(
    100, 200, 300,
    chegirma_foizi = 10,
    yetkazib_berish_narxi = 30,
    soliq_foizi = 12,
    bepul_yetkazib_berish_liliti = 500,
)

#2
def xodim_samaradorligi(*args, **kwargs):
    reja = kwargs.get("reja", 0)
    tolov = kwargs.get("ish_tolovi", 0)
    bonus_foizi = kwargs.get("bonus_foizi", 0)
    jarima_foizi = kwargs.get("jarima_foizi", 0)

    eng_yuqori_foiz = 0
    eng_samarali_xodim = 0

    for i in range(len(args)):
        ish_soni = args[i]
        foiz = ish_soni * 100 / reja
        ish_haqi = ish_soni * tolov
        bonus = 0
        jarima = 0

        if foiz >= 100:
            oshgan_ishlar = ish_soni - reja
            bonus = oshgan_ishlar * tolov * bonus_foizi / 100
        elif foiz < 70:
            jarima = ish_haqi * jarima_foizi / 100

        daromad = ish_haqi + bonus - jarima

        print(f"{i + 1}-xodim: reja bajarilishi {foiz:.2f}%")
        print(f"  Ish haqi: {ish_haqi:.2f}")
        print(f"  Bonus: +{bonus:.2f}")
        print(f"  Jarima: -{jarima:.2f}")
        print(f"  Daromad: {daromad:.2f}")

        if foiz > eng_yuqori_foiz:
            eng_yuqori_foiz = foiz
            eng_samarali_xodim = i + 1

    print(f"Eng samarali xodim: {eng_samarali_xodim}-xodim ({eng_yuqori_foiz:.2f}%)")


xodim_samaradorligi(
    120, 95, 60, 150,
    reja=100,
    ish_tolovi=50000,
    bonus_foizi=20,
    jarima_foizi=10,
)

#3
def tranzaksiya_tahlili(*args, **kwargs):
    balans = kwargs.get("boshlangich_balans", 0)
    komissiya_foizi = kwargs.get("komissiya_foizi", 0)
    minimal_balans = kwargs.get("minimal_balans", 0)

    muvaffaqiyatli = 0
    rad_etilgan = 0
    jami_komissiya = 0

    print(f"Boshlang'ich balans: {balans:.2f}")

    for i in range(len(args)):
        summa = args[i]

        if summa >= 0:
            balans += summa
            muvaffaqiyatli += 1
            print(f"{i + 1}-tranzaksiya: +{summa:.2f} (pul tushdi). Balans: {balans:.2f}")
        else:
            yechilgan = abs(summa)
            komissiya = yechilgan * komissiya_foizi / 100
            jami_yechiladi = yechilgan + komissiya

            if jami_yechiladi <= balans:
                balans -= jami_yechiladi
                jami_komissiya += komissiya
                muvaffaqiyatli += 1
                print(f"{i + 1}-tranzaksiya: -{yechilgan:.2f} (komissiya {komissiya:.2f}). Balans: {balans:.2f}")
            else:
                rad_etilgan += 1
                print(f"{i + 1}-tranzaksiya: -{yechilgan:.2f} RAD ETILDI (mablag' yetarli emas). Balans: {balans:.2f}")

    print(f"Muvaffaqiyatli tranzaksiyalar: {muvaffaqiyatli} ta")
    print(f"Rad etilgan operatsiyalar: {rad_etilgan} ta")
    print(f"Jami komissiya: {jami_komissiya:.2f}")
    print(f"Yakuniy balans: {balans:.2f}")

    if balans < minimal_balans:
        print(f"Ogohlantirish: balans minimal chegaradan ({minimal_balans:.2f}) past!")


tranzaksiya_tahlili(
    500, -300, -2000, -400, 100, -50,
    boshlangich_balans=1000,
    komissiya_foizi=2,
    minimal_balans=1000,
)





