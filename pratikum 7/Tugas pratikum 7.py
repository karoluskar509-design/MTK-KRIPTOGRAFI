import sys
import textwrap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# =============================================
#  DES TABLES
# =============================================

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# 8 S-Box (standard)
SBOX = [
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
    ],
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
    ],
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
    ],
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
    ],
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
    ],
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
    ],
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
    ],
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11],
    ]
]


# =============================================
#   DES Helper Functions
# =============================================

def str_to_bin(text):
    return ''.join(format(ord(i), '08b') for i in text)

def permute(block, table):
    return ''.join(block[i-1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))

def sbox_sub(block48):
    output = ""
    for i in range(8):
        part = block48[i*6:(i+1)*6]
        row = int(part[0] + part[5], 2)
        col = int(part[1:5], 2)
        output += format(SBOX[i][row][col], '04b')
    return output


def generate_subkeys(key8):
    """
    returns: subkeys(list of 16 48-bit), keybin(64-bit), log(str)
    key8 is padded to 8 chars
    """
    log = ""
    # Ensure key is exactly 8 chars (pad with spaces if needed)
    key8 = key8.ljust(8)[:8]
    key_bin = str_to_bin(key8)
    log += f"Key (padded 8 chars): '{key8}'\n"
    log += f"Key Binary (64-bit):\n{key_bin}\n\n"

    # PC-1
    key56 = permute(key_bin, PC1)
    log += f"PC-1 output (56-bit):\n{key56}\n\n"

    C = key56[:28]
    D = key56[28:]
    log += f"C0 = {C}\nD0 = {D}\n\n"

    rotations = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    subkeys = []

    for i, r in enumerate(rotations):
        C = left_shift(C, r)
        D = left_shift(D, r)
        log += f"Round {i+1} Left shift by {r}:\n"
        log += f"C{i+1} = {C}\n"
        log += f"D{i+1} = {D}\n"
        combined = C + D
        # PC-2 to form subkey
        sub = permute(combined, PC2)
        log += f"K{i+1:02} (after PC-2) = {sub}\n\n"
        subkeys.append(sub)

    return subkeys, key_bin, log


def des_encrypt(pt, key):
    """
    returns: cipher_bin, cipher_hex, subkeys, keybin, log
    """
    log = ""

    # Pad plaintext with spaces to be multiple of 8 bytes
    original_len = len(pt)
    while len(pt) % 8 != 0:
        pt += " "

    pt_bin = str_to_bin(pt)
    log += f"Plaintext (original): '{pt[:original_len]}'\n"
    log += f"Plaintext Binary (after padding to {len(pt)} bytes):\n{pt_bin}\n\n"

    blocks = textwrap.wrap(pt_bin, 64)

    subkeys, keybin, keylog = generate_subkeys(key)
    log += keylog

    cipher_bin = ""

    for block_index, block in enumerate(blocks):
        log += f"\n===== BLOCK {block_index+1} =====\n"
        log += f"64-bit block (before IP):\n{block}\n\n"

        block_ip = permute(block, IP)
        log += f"After Initial Permutation (IP):\n{block_ip}\n\n"

        L, R = block_ip[:32], block_ip[32:]
        log += f"L0 = {L}\nR0 = {R}\n\n"

        for i in range(16):
            log += f"---- ROUND {i+1} ----\n"
            exp_r = permute(R, E)
            log += f"E(R{i}): {exp_r}\n"

            x = xor(exp_r, subkeys[i])
            log += f"XOR with K{i+1:02}: {x}\n"

            s = sbox_sub(x)
            log += f"S-Box output (32-bit): {s}\n"

            p = permute(s, P)
            log += f"P-box output (32-bit): {p}\n"

            newR = xor(L, p)
            log += f"L{i} = {L}\nR{i} = {R}\nNew R (R{i+1}) = L{i} XOR P = {newR}\n\n"

            L, R = R, newR

        # After 16 rounds combine R and L (note the swap)
        preoutput = R + L
        log += f"Before final permutation (R16 + L16):\n{preoutput}\n\n"

        final = permute(preoutput, FP)
        log += f"Final Permutation (IP^-1) result:\n{final}\n\n"

        cipher_bin += final

    # Convert cipher_bin to hex safely
    if cipher_bin.strip("0") == "":
        cipher_hex = "0"
    else:
        cipher_hex = hex(int(cipher_bin, 2))[2:].upper()

    log += f"=== FINAL CIPHERTEXT ===\nBinary:\n{cipher_bin}\nHexadecimal:\n{cipher_hex}\n"

    return cipher_bin, cipher_hex, subkeys, keybin, log


# ==========================================================
#   GUI CLASS – PYQT5
# ==========================================================

class DESGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DES Encryption – PyQt5 Modern GUI")
        self.resize(1000, 750)

        # Gradient background
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, 900)
        gradient.setColorAt(0.0, QColor("#6C63FF"))
        gradient.setColorAt(1.0, QColor("#2C2F83"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

        main = QWidget()
        layout = QVBoxLayout(main)

        # TITLE
        title = QLabel("DES Encryption – PyQt5 GUI")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: white;")
        layout.addWidget(title)

        # INPUT CARD
        card = QWidget()
        card.setStyleSheet("""
            background: white;
            border-radius: 15px;
            padding: 20px;
        """)
        form = QFormLayout(card)

        self.input_plain = QLineEdit()
        self.input_plain.setStyleSheet("padding: 8px; font-size: 14px;")

        self.input_key = QLineEdit()
        self.input_key.setStyleSheet("padding: 8px; font-size: 14px;")

        form.addRow("Plaintext:", self.input_plain)
        form.addRow("Key (max 8 chars):", self.input_key)

        layout.addWidget(card)

        # BUTTON
        btn = QPushButton("Encrypt DES")
        btn.setFixedHeight(45)
        btn.setStyleSheet("""
            QPushButton {
                background-color: #00E5FF;
                color: black;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00B2CC;
            }
        """)
        btn.clicked.connect(self.do_encrypt)
        layout.addWidget(btn)

        # OUTPUT BOX
        self.output = QTextEdit()
        self.output.setStyleSheet("""
            background-color: #0A0B33;
            color: #00FFEA;
            font-family: Consolas;
            font-size: 13px;
            padding: 10px;
            border-radius: 10px;
        """)
        # monospace font and read-only for convenience
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setCentralWidget(main)

    def do_encrypt(self):
        pt = self.input_plain.text()
        key = self.input_key.text()

        if len(key) == 0 or len(key) > 8:
            QMessageBox.critical(self, "Error", "Key harus 1–8 karakter!")
            return

        cbin, chex, subkeys, keybin, log = des_encrypt(pt, key)

        # The des_encrypt already created a detailed log in correct order,
        # but we'll prefix a small header for clarity.
        text = "=== DES ENCRYPTION RESULT (detailed steps) ===\n\n"
        text += log

        self.output.setPlainText(text)


# ==========================================================
# RUN APP
# ==========================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DESGUI()
    window.show()
    sys.exit(app.exec_())
