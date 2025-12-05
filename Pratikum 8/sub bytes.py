#!/usr/bin/env python3
"""
AES-128 — slide-mode key expansion + full 10-round encryption (AES MixColumns standard).
- Initial key is arranged ROW-MAJOR (to match slide).
- Key expansion follows the slide rule:
    W0..W3 = columns extracted from the row-major initial matrix (top->bottom).
    for i>=4:
      temp = W[i-1]
      if i%4==0:
        temp = RotWord(temp); temp = SubWord(temp); temp[0] ^= RCON[i//4]
      W[i] = W[i-4] XOR temp
- Encryption:
    Round0: AddRoundKey(K0)
    Rounds1..9: SubBytes -> ShiftRows -> MixColumns (AES standard) -> AddRoundKey(Ki)
    Round10: SubBytes -> ShiftRows -> AddRoundKey(K10)
- Input defaults: press ENTER to use defaults from your task.
"""
from typing import List

# --- SBOX (flat 256) ---
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

RCON = [0x00,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]

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

def to_hex_bytes(text: str) -> List[int]:
    return [ord(c) for c in text]

def print_mat_hex(mat: List[List[int]], title: str):
    print(f"\n{title}:")
    for r in mat:
        print(" ".join(f"{x:02X}" for x in r))

# --- key expansion slide-mode (initial key row-major) ---
def rot_word(w: List[int]) -> List[int]:
    return w[1:]+w[:1]

def sub_word(w: List[int]) -> List[int]:
    return [SBOX[b] for b in w]

def expand_keys_slide(key_text: str) -> List[List[List[int]]]:
    # initial key filled ROW-MAJOR from key_text
    hexs = [format(ord(c),'02X') for c in key_text]
    # build row-major matrix strings then extract columns as words
    km = [[None]*4 for _ in range(4)]
    for i in range(16):
        r = i // 4
        c = i % 4
        km[r][c] = hexs[i]
    # initial words W0..W3 are columns top->bottom (ints)
    words: List[List[int]] = []
    for c in range(4):
        words.append([int(km[r][c],16) for r in range(4)])
    # expand to 44 words
    for i in range(4,44):
        temp = words[i-1].copy()
        if i % 4 == 0:
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp[0] ^= RCON[i//4]
            temp = [t & 0xFF for t in temp]
        neww = [ (temp[j] ^ words[i-4][j]) & 0xFF for j in range(4) ]
        words.append(neww)
    # group into round keys (each 4 words -> 4x4 row-major matrix)
    round_keys: List[List[List[int]]] = []
    for r in range(0,44,4):
        block = words[r:r+4]  # 4 words = columns left->right
        mat = [[0]*4 for _ in range(4)]
        for c in range(4):
            for row in range(4):
                mat[row][c] = block[c][row]
        round_keys.append(mat)
    return round_keys

# --- AES primitives (standard MixColumns) ---
def sub_bytes_state(state: List[List[int]]) -> List[List[int]]:
    return [[ SBOX[state[r][c]] for c in range(4)] for r in range(4)]

def shift_rows_state(state: List[List[int]]) -> List[List[int]]:
    out = [[0]*4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            out[r][c] = state[r][(c + r) % 4]
    return out

def xtime(a: int) -> int:
    return ((a << 1) ^ 0x1B) & 0xFF if (a & 0x80) else (a << 1) & 0xFF

def mix_single_column(col: List[int]) -> List[int]:
    a0,a1,a2,a3 = col
    # r0 = 2*a0 ^ 3*a1 ^ a2 ^ a3
    r0 = (xtime(a0) ^ (xtime(a1) ^ a1) ^ a2 ^ a3) & 0xFF
    r1 = (xtime(a1) ^ (xtime(a2) ^ a2) ^ a3 ^ a0) & 0xFF
    r2 = (xtime(a2) ^ (xtime(a3) ^ a3) ^ a0 ^ a1) & 0xFF
    r3 = (xtime(a3) ^ (xtime(a0) ^ a0) ^ a1 ^ a2) & 0xFF
    return [r0,r1,r2,r3]

def mix_columns_state(state: List[List[int]]) -> List[List[int]]:
    # operate on columns
    cols = [ [state[r][c] for r in range(4)] for c in range(4) ]
    mixed_cols = [ mix_single_column(col) for col in cols ]
    # convert back to row-major
    out = [[0]*4 for _ in range(4)]
    for c in range(4):
        for r in range(4):
            out[r][c] = mixed_cols[c][r]
    return out

def add_round_key_state(state: List[List[int]], rk: List[List[int]]) -> List[List[int]]:
    out = [[ (state[r][c] ^ rk[r][c]) & 0xFF for c in range(4)] for r in range(4)]
    return out

# --- main encryption flow ---
def encrypt_full(plaintext: str, cipherkey: str):
    # expand keys
    round_keys = expand_keys_slide(cipherkey)
    print_mat_hex(round_keys[0], "K0 (slide-mode)")
    for i in range(1,11):
        print_mat_hex(round_keys[i], f"K{i}")

    # build initial state: row-major bytes
    pt_bytes = [ord(c) for c in plaintext]
    state = [[0]*4 for _ in range(4)]
    for i in range(16):
        r = i // 4
        c = i % 4
        state[r][c] = pt_bytes[i]

    print_mat_hex(state, "Initial State (row-major, plaintext)")

    # Round 0: AddRoundKey
    state = add_round_key_state(state, round_keys[0])
    print_mat_hex(state, "After AddRoundKey (Round 0)")

    # Rounds 1..9
    for rnd in range(1,10):
        state = sub_bytes_state(state)
        state = shift_rows_state(state)
        state = mix_columns_state(state)
        state = add_round_key_state(state, round_keys[rnd])
        print_mat_hex(state, f"After Round {rnd}")

    # Round 10 (final)
    state = sub_bytes_state(state)
    state = shift_rows_state(state)
    state = add_round_key_state(state, round_keys[10])
    print_mat_hex(state, "After Round 10 (Ciphertext)")

    return state

if __name__ == "__main__":
    pt = default_input("Masukkan PLAINTEXT (16 chars; ENTER=default PASKAMARTOHASUGI): ",
                       "PASKAMARTOHASUGI")
    ck = default_input("Masukkan CIPHERKEY (16 chars; ENTER=default UNIKASANTOTHOMAS): ",
                       "UNIKASANTOTHOMAS")

    encrypt_full(pt, ck)
