with open('input.txt', 'r') as f:
    line = f.readline().strip()

speicher_liste = [int(x) for x in line]

idspeicherliste = []

i = 0
for x in range(0, len(speicher_liste)):
    if(x % 2 == 0):
        len_datei = speicher_liste[x]
        idspeicherliste.extend([i] * len_datei)
        i += 1
    else:
        len_freier_speicher = speicher_liste[x]
        idspeicherliste.extend(['.'] * len_freier_speicher)

max_id = i

idspeicherliste2=idspeicherliste.copy()

pos_freier_speicher = 0
pos_dateiblock = 1
while pos_freier_speicher < pos_dateiblock:
    pos_freier_speicher = idspeicherliste.index('.')
    for x in range(len(idspeicherliste) - 1, 0, -1):
        if idspeicherliste[x] != '.':
            pos_dateiblock = x
            break
    if(pos_freier_speicher >= pos_dateiblock):
        break
    idspeicherliste[pos_freier_speicher] = idspeicherliste[pos_dateiblock]
    idspeicherliste[pos_dateiblock] = '.'

checksum = 0
for x in range(0, len(idspeicherliste)):
    if idspeicherliste[x] != '.' and idspeicherliste[x] != '#':
        checksum += x * int(idspeicherliste[x])

print(f"Part 1: {checksum}")

# Part 2
idspeicherliste = idspeicherliste2.copy()

for file_id in range(max_id - 1, -1, -1): 
    pos_db = idspeicherliste.index(file_id) # Position der Datei
    len_db = idspeicherliste.count(file_id) # Länge der Datei

    best_fs_pos = None
    for pos_fs in range(0, pos_db):
        if idspeicherliste[pos_fs:pos_fs + len_db] == ['.'] * len_db:
            best_fs_pos = pos_fs
            break

    if best_fs_pos is not None:
        for i in range(len_db):
            idspeicherliste[best_fs_pos + i] = file_id
            idspeicherliste[pos_db + i] = '.'

checksum = sum(x * int(idspeicherliste[x]) for x in range(len(idspeicherliste)) if idspeicherliste[x] != '.')
print(f"Part 2: {checksum}")