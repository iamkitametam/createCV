
# reformatting date

def make_correct_date_format(s):
    s = s.replace("\xa0"," ")
    s = s.upper()
    s = s.split(" ")
    s = s[0:5]

    if(s[4][0]=='2'):
        s[4] = s[4][0:4]
        s = " ".join(s)
    else:
        s = " ".join(s)
        s = s.replace("ПО НАСТОЯЩЕЕ", "н.в.")

    s = s.replace("ЯНВАРЬ ", "01.")
    s = s.replace("ФЕВРАЛЬ ", "02.")
    s = s.replace("МАРТ ", "03.")
    s = s.replace("АПРЕЛЬ ", "04.")
    s = s.replace("МАЙ ", "05.")
    s = s.replace("ИЮНЬ ", "06.")
    s = s.replace("ИЮЛЬ ", "07.")
    s = s.replace("АВГУСТ ", "08.")
    s = s.replace("СЕНТЯБРЬ ", "09.")
    s = s.replace("ОКТЯБРЬ ", "10.")
    s = s.replace("НОЯБРЬ ", "11.")
    s = s.replace("ДЕКАБРЬ ", "12.")

    s = s.replace("JANUARY ", "01.")
    s = s.replace("FEBRUARY ", "02.")
    s = s.replace("MARCH ", "03.")
    s = s.replace("APRIL ", "04.")
    s = s.replace("MAY ", "05.")
    s = s.replace("JUNE ", "06.")
    s = s.replace("JULY ", "07.")
    s = s.replace("AUGUST ", "08.")
    s = s.replace("SEPTEMBER ", "09.")
    s = s.replace("OCTOBER ", "10.")
    s = s.replace("NOVEMBER ", "11.")
    s = s.replace("DECEMBER ", "12.")

    # s = s.replace("20","")

    return s