import re
input_list = ["Т356ОК56", "Т357ОК", "A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12", "Т359ОК59", "У0019ОК1", "Х9999ОХ"]
result = [x for x in input_list if re.fullmatch(r'[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', x)]    #Используются русские бувы
print(*result)
