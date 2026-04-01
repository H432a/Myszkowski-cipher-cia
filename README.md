# Myszkowski-cipher-cia
#  Myszkowski Cipher with Dice Random Walk Hash

This project implements:
- Myszkowski Transposition Cipher (Encryption & Decryption)
- A custom Dice Random Walk Hash Function
- End-to-end pipeline: Encrypt → Hash → Decrypt

---

## Theory

### Myszkowski Cipher
Myszkowski Cipher is a columnar transposition cipher where:
- The plaintext is written row-wise into a matrix
- Columns are read based on alphabetical order of key characters
- Duplicate key characters are handled by reading columns together

This makes it different from standard columnar transposition.

---

### Dice Random Walk Hash

This project introduces a custom hash function based on a deterministic random walk.

#### Working:
1. Each character is converted into a dice value:
   dice = (ord(character) % 6) + 1 
2. Each dice value represents a movement:

| Dice | Movement |
|------|---------|
| 1 | Up (0, +1) |
| 2 | Down (0, -1) |
| 3 | Right (+1, 0) |
| 4 | Left (-1, 0) |
| 5 | Diagonal ↗ (+1, +1) |
| 6 | Diagonal ↙ (-1, -1) |

3. A 2D walk is simulated:
- Track position (x, y)
- Accumulate path complexity

4. Final hash is computed using:
- Final position
- Path sum

---

##  How to Run

1. Install matplotlib (if not installed):
```bash
pip install matplotlib
