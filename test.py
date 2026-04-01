from cia import encrypt_myszkowski, decrypt_myszkowski, dice_hash

def test_round_trip():
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    cipher, _ = encrypt_myszkowski(plaintext, key)
    hash_val, x, y = dice_hash(cipher)
    decrypted, _ = decrypt_myszkowski(cipher, key)

    print("\n===== TEST RESULT =====")
    print("Plaintext :", plaintext)
    print("Key       :", key)
    print("Cipher    :", cipher)
    print("Hash      :", hash_val)
    print("Final Pos :", (x, y))
    print("Decrypted :", decrypted)

    if plaintext.replace(" ", "").upper() == decrypted:
        print("\n Round-trip successful :)")
    else:
        print("\n Error in implementation :(")


if __name__ == "__main__":
    test_round_trip()