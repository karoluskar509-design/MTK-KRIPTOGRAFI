#!/usr/bin/env python3
"""
AES (slide-mode key expansion) + encryption (MixColumns SIMPLE).
- Manual input with defaults if user presses ENTER.
- Initial key filled ROW-MAJOR (slide style).
- Key expansion follows the slide rules described earlier.
- MixColumns SIMPLE: mul2 = (b<<1)&0xFF, mul3 = mul2 ^ b
"""

from typing import List

# --- SBOX & RCON ---
SBOX = [
0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76,
0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0,
0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15,
0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75,
0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84,
0x53,0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF,
0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8,
0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2,
0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73,
0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB,
0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79,
0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08,
0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A,
0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E,
0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF,
0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16
]
RCON = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]

# --- helpers ---
def default_input(prompt: str, default: str) -> str:
    s = input(prompt).strip()
    if s == "":
        print(f"→ otomatis memakai default: {default}")
        return default
    while len(s) != 16:
        print("ERROR: harus tepat 16 karakter.")
        s = input(prompt).strip()
        if s == "":
            print(f"→ otomatis memakai default: {default}")
            return default
    return s

def to_hex_list(text: str) -> List[str]:
    return [format(ord(c),'02X') for c in text]

def matrix_row_major_from_hex(hex_list: List[str]) -> List[List[str]]:
    mat = [[None]*4 for _ in range(4)]
    for i in range(16):
        r = i // 4
        c = i % 4
        mat[r][c] = hex_list[i]
    return mat

def print_matrix_hex_strings(mat: List[List[str]], title: str):
    print(f"\n=== {title} ===")
    for r in range(4):
        print(" ".join(mat[r][c] for c in range(4)))

def print_matrix_int(mat: List[List[int]], title: str):
    print(f"\n=== {title} ===")
    for r in range(4):
        print(" ".join(f"{mat[r][c]:02X}" for c in range(4)))

# --- key expansion (slide-mode) ---
def rot_word(word: List[int]) -> List[int]:
    return word[1:] + word[:1]

def sub_word(word: List[int]) -> List[int]:
    return [SBOX[b] for b in word]

def expand_keys_slide_mode(key_text: str) -> List[List[List[int]]]:
    hexlist = to_hex_list(key_text)
    # initial key matrix row-major
    km = matrix_row_major_from_hex(hexlist)  # strings like '55'
    # initial words W0..W3 are columns extracted top->bottom
    words: List[List[int]] = []
    for col in range(4):
        w = [int(km[row][col],16) for row in range(4)]
        words.append(w)
    # expand to 44 words
    for i in range(4,44):
        temp = words[i-1].copy()
        if i % 4 == 0:
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp[0] ^= RCON[(i//4)-1]
            temp = [t & 0xFF for t in temp]
        neww = [ (temp[j] ^ words[i-4][j]) & 0xFF for j in range(4) ]
        words.append(neww)
    # group into round keys (4 words -> 4x4 int matrix row-major for display)
    round_keys: List[List[List[int]]] = []
    for r in range(11):
        block = words[r*4:(r+1)*4]  # block[0..3] are words: columns left->right
        mat = [[0]*4 for _ in range(4)]
        for c in range(4):
            for rr in range(4):
                mat[rr][c] = block[c][rr]
        round_keys.append(mat)
    return round_keys

# --- AES primitives ---
def sub_bytes_state(state: List[List[str]]) -> List[List[str]]:
    return [[format(SBOX[int(state[r][c],16)],'02X') for c in range(4)] for r in range(4)]

def shift_rows_state(state: List[List[str]]) -> List[List[str]]:
    out = [[None]*4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            out[r][c] = state[r][(c + r) % 4]
    return out

def mul2_simple(b: int) -> int:
    return (b << 1) & 0xFF

def mul3_simple(b: int) -> int:
    return mul2_simple(b) ^ b

def mix_columns_simple(state: List[List[str]]) -> List[List[str]]:
    out = [[None]*4 for _ in range(4)]
    for c in range(4):
        a = [int(state[r][c],16) for r in range(4)]
        r0 = (mul2_simple(a[0]) ^ mul3_simple(a[1]) ^ a[2] ^ a[3]) & 0xFF
        r1 = (a[0] ^ mul2_simple(a[1]) ^ mul3_simple(a[2]) ^ a[3]) & 0xFF
        r2 = (a[0] ^ a[1] ^ mul2_simple(a[2]) ^ mul3_simple(a[3])) & 0xFF
        r3 = (mul3_simple(a[0]) ^ a[1] ^ a[2] ^ mul2_simple(a[3])) & 0xFF
        out[0][c] = format(r0,'02X')
        out[1][c] = format(r1,'02X')
        out[2][c] = format(r2,'02X')
        out[3][c] = format(r3,'02X')
    return out

def add_round_key_state(state: List[List[str]], rk: List[List[int]]) -> List[List[str]]:
    out = [[format(int(state[r][c],16) ^ rk[r][c],'02X') for c in range(4)] for r in range(4)]
    return out

# --- main ---
def main():
    print("=== AES (Slide-mode key expansion) + encryption (MixColumns SIMPLE) ===")
    pt = default_input("Masukkan PLAINTEXT (16 chars; ENTER=default PASKAMARTOHASUGI): ",
                       "PASKAMARTOHASUGI")
    ck = default_input("Masukkan CIPHERKEY (16 chars; ENTER=default UNIKASANTOTHOMAS): ",
                       "UNIKASANTOTHOMAS")

    # display ASCII/HEX
    print("\nPlaintext ASCII/HEX:")
    for i,ch in enumerate(pt):
        print(f"{i:02d} | {ch} | {ord(ch):3d} | {format(ord(ch),'02X')}")
    print("\nCipherKey ASCII/HEX:")
    for i,ch in enumerate(ck):
        print(f"{i:02d} | {ch} | {ord(ch):3d} | {format(ord(ch),'02X')}")

    # initial plaintext state (row-major hex strings)
    pt_hex = to_hex_list(pt)
    state = matrix_row_major_from_hex(pt_hex)

    # expand keys using slide-mode
    round_keys = expand_keys_slide_mode(ck)

    # print round keys K0..K10
    print_matrix_int(round_keys[0], "K0")
    for i in range(1,11):
        print_matrix_int(round_keys[i], f"K{i}")

    # Encryption
    state = add_round_key_state(state, round_keys[0])  # round 0

    for rnd in range(1,10):
        state = sub_bytes_state(state)
        state = shift_rows_state(state)
        state = mix_columns_simple(state)
        state = add_round_key_state(state, round_keys[rnd])

    # final round
    state = sub_bytes_state(state)
    state = shift_rows_state(state)
    state = add_round_key_state(state, round_keys[10])

    # produce ciphertext string row-major
    ct = "".join(state[r][c] for r in range(4) for c in range(4))
    print("\n=== Ciphertext (HEX) (row-major) ===")
    print(ct.upper())

if __name__ == "__main__":
    main()
