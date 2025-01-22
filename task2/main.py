import hashlib
import os


def compute_hash(path):
    hash_func = hashlib.new('sha3_256')
    with open(path, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)

    return hash_func.hexdigest()


def main():
    s = []
    for path in os.listdir('./task2'):
        s.append(str(compute_hash(f"./task2/{path}").lower()))
    s.sort(reverse=True)
    st = "abror2142@gmail.com" + "".join(s)
    h = hashlib.sha3_256(st.encode('utf-8')).hexdigest()
    print(h)

main()