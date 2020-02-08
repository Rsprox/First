input_list = ["Т356ОК56", "Т357ОК", "A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12", "Т359ОК59", "У0019ОК1", "Х9999ОХ"]
ckeck_chars = set('АВЕКМНОРСТУХ')   #Используются русские буквы
result = []
for x in input_list:
    if len(x) == 8:
        if (x[0] in ckeck_chars) and x[1].isdigit() and x[2].isdigit() and x[3].isdigit() and (x[4] in ckeck_chars) and (x[5] in ckeck_chars) and x[6].isdigit() and x[7].isdigit():
            result.append(x)
    elif len(x) == 9:
        if (x[0] in ckeck_chars) and x[1].isdigit() and x[2].isdigit() and x[3].isdigit() and (x[4] in ckeck_chars) and (x[5] in ckeck_chars) and x[6].isdigit() and x[7].isdigit() and x[8].isdigit():
            result.append(x)
print(*result)