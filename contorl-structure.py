manob_ape = 15
anek_ape = 20
somchai_ape = 25
somsri_ape = 30
somsak_ape = 35
somying_ape = 20
i_am_handsome = True
fruits = ["orenge", "apple", "banana"]

# > มากกว่า
print(somsak_ape > somying_ape)
# < น้อยกว่า
print(manob_ape < somsri_ape)
# == เท่ากับ
print(anek_ape == somying_ape)
# >= มากกว่าหรือเท่ากับ
print (somsak_ape > somsri_ape)
# <= น้อยกว่าหรือเท่ากับ
print(manob_ape < anek_ape)
# != ไม่เท่ากับ
print(i_am_handsome)
# "orenge" in fruits
print("orenge" in fruits)

print("orenge" in fruits and i_am_handsome)
print("orenge" in fruits or i_am_handsome)

age = 18
if(age>=18):
    print("you can access thiswebsite")
else:
    print("you can't access thiswebsite")