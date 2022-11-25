lista = [1,2,3] 
tuple = (1,2,3)
set = {1,2,3}
dictionary = {"yksi":1,"kaksi":2,"kolme":3}

print("Listan toinen objekti on",lista[1])
print("Tuplen toinen objekti on", tuple[1])
for i in set:
    if i == 2:
        print("Setin toinen objekti on", i)
print("Dictionary toinen objekti on", dictionary["kaksi"])