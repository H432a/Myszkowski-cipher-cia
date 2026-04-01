import time
import matplotlib.pyplot as plt

def get_key_order(key):
    sorted_unique = sorted(list(set(key)))
    order_map = {ch: i for i, ch in enumerate(sorted_unique)}
    return [order_map[ch] for ch in key]


def encrypt_myszkowski(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()

    cols = len(key)
    rows = (len(plaintext) + cols - 1) // cols

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx < len(plaintext):
                matrix[r][c] = plaintext[idx]
                idx += 1
            else:
                matrix[r][c] = 'X'

    key_order = get_key_order(key)
    ciphertext = ""

    for order in sorted(set(key_order)):
        cols_same = [i for i in range(cols) if key_order[i] == order]
        for r in range(rows):
            for c in cols_same:
                ciphertext += matrix[r][c]

    return ciphertext, matrix


def decrypt_myszkowski(ciphertext, key):
    key = key.upper()
    cols = len(key)
    rows = (len(ciphertext) + cols - 1) // cols

    key_order = get_key_order(key)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    idx = 0
    for order in sorted(set(key_order)):
        cols_same = [i for i in range(cols) if key_order[i] == order]
        for r in range(rows):
            for c in cols_same:
                if idx < len(ciphertext):
                    matrix[r][c] = ciphertext[idx]
                    idx += 1

    plaintext = ""
    for r in range(rows):
        for c in range(cols):
            plaintext += matrix[r][c]

    return plaintext.rstrip('X'), matrix


# dice-based hash function

def dice_hash(text):
    x, y = 0, 0
    path_sum = 0
    MOD = 10**9 + 7

    for i, ch in enumerate(text):
        dice = (ord(ch) % 6) + 1

        if dice == 1:
            dx, dy = 0, 1
        elif dice == 2:
            dx, dy = 0, -1
        elif dice == 3:
            dx, dy = 1, 0
        elif dice == 4:
            dx, dy = -1, 0
        elif dice == 5:
            dx, dy = 1, 1
        else:
            dx, dy = -1, -1

        x += dx
        y += dy

        path_sum += (x*x + y*y + i)
        path_sum %= MOD

    final_hash = (x * 31 + y * 37 + path_sum) % MOD
    return final_hash, x, y


# simple hash function for comparison

def simple_hash(text):
    h = 0
    for ch in text:
        h += ord(ch)
    return h


# random walk visualization

def plot_random_walk(text):
    x, y = 0, 0
    xs = [0]
    ys = [0]

    for ch in text:
        dice = (ord(ch) % 6) + 1

        if dice == 1:
            dx, dy = 0, 1
        elif dice == 2:
            dx, dy = 0, -1
        elif dice == 3:
            dx, dy = 1, 0
        elif dice == 4:
            dx, dy = -1, 0
        elif dice == 5:
            dx, dy = 1, 1
        else:
            dx, dy = -1, -1

        x += dx
        y += dy

        xs.append(x)
        ys.append(y)

    plt.figure()
    plt.plot(xs, ys, marker='o')
    plt.title("Dice Random Walk Path")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()


# analysis function  

def analyze(plaintext, key):
    print("\n========== ANALYSIS ==========")

    start = time.time()
    cipher, enc_matrix = encrypt_myszkowski(plaintext, key)
    enc_time = time.time() - start

    start = time.time()
    decrypted, dec_matrix = decrypt_myszkowski(cipher, key)
    dec_time = time.time() - start

    hash_val, x, y = dice_hash(cipher)
    simple = simple_hash(cipher)

    print("\nMatrix Shape:", len(enc_matrix), "x", len(enc_matrix[0]))

    print("\nEncryption Matrix:")
    for row in enc_matrix:
        print(row)

    print("\nDecryption Matrix:")
    for row in dec_matrix:
        print(row)

    print("\n========== RESULTS ==========")
    print(f"{'Plaintext':<15}: {plaintext}")
    print(f"{'Key':<15}: {key}")
    print(f"{'Ciphertext':<15}: {cipher}")
    print(f"{'Dice Hash':<15}: {hash_val}")
    print(f"{'Simple Hash':<15}: {simple}")
    print(f"{'Final Position':<15}: ({x}, {y})")
    print(f"{'Decrypted':<15}: {decrypted}")

    print("\n========== PERFORMANCE ==========")
    print(f"{'Encryption Time':<20}: {enc_time:.6f} sec")
    print(f"{'Decryption Time':<20}: {dec_time:.6f} sec")

    print("\n========== OBSERVATIONS ==========")
    print("1. Duplicate key characters create grouped column reads.")
    print("2. Dice mapping introduces non-linear transformation.")
    print("3. Small input changes significantly affect final hash.")
    print("4. Dice hash >> Simple hash in randomness.")

    # Visualization
    plot_random_walk(cipher)


# menu-driven program

def main():
    while True:
        print("\n========= MENU =========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Full Analysis (BEST OPTION)")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            pt = input("Enter plaintext: ")
            key = input("Enter key: ")

            cipher, matrix = encrypt_myszkowski(pt, key)

            print("\nMatrix:")
            for row in matrix:
                print(row)

            print("\nCiphertext:", cipher)

        elif choice == '2':
            ct = input("Enter ciphertext: ")
            key = input("Enter key: ")

            pt, matrix = decrypt_myszkowski(ct, key)

            print("\nMatrix:")
            for row in matrix:
                print(row)

            print("\nDecrypted Text:", pt)

        elif choice == '3':
            pt = input("Enter plaintext: ")
            key = input("Enter key: ")
            analyze(pt, key)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()