import hashlib

# récupération du fichier 1 à comparer

file1 = input("Enter the input file name: ")
sha256_hash = hashlib.sha256()
with open(file1, "rb") as f:
    # boucle qui récupère l'ensemble des bytes du fichier
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)
    print(sha256_hash.hexdigest())

# récupération du fichier 2 à comparer

file2 = input("Enter the input file name: ")
sha256_hash2 = hashlib.sha256()
with open(file2, "rb") as f:

    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash2.update(byte_block)
    print(sha256_hash2.hexdigest())

# comparaison des 2 hash avec message d'information

if sha256_hash.hexdigest() == sha256_hash2.hexdigest():
    print(" The hashes are the same ! ")
else:
    print("The hashes are not the same !")

