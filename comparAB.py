import os
import tkinter as tk
from tkinter import filedialog

def print_ascii():
    input("""
                                                       .,-:;//;:=,
                                                  . :H@@@MM@M#H/.,+%;,
                                               ,/X+ +M@@M@MM%=,-%HMMM@X/,
                                             -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
                                            ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
                                          ,%MM@@MH ,@%=             .---=-=:=,.
                                          =@#@@@MX.,                -%HX$$%%%:;
                                         =-./@M@M$                   .;@MMMM@MM:
                                         X@/ -$MM/                    . +MM@@@M$
                                        ,@M@H: :@:                    . =X#@@@@-
                                        ,@@@MMX, .                    /H- ;@M@M=
                                        .H@@@@M@+,                    %MM+..%#$.
                                         /MMMM@MMH/.                  XM@MH; =;
                                          /%+%$XHH@$=              , .H@@@@MX,
                                           .=--------.           -%H.,@@@@@MX,
                                           .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
                                             =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
                                               =%@M@M#@$-.=$@MM@@@M; %M%=
                                                 ,:+$+-,/H#MMMMMMM@= =,
                                                       =++%%%%+/:-.
                                         Press enter to start comparing files.
""")

def compare_files():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_ascii()
    root = tk.Tk()
    root.withdraw()
    print("Select file A. It contains the lines you want to remove from file B.")
    file_a_path = filedialog.askopenfilename(title="Select file A")
    print("Select file B. Lines common to file A will be deleted in this file.")
    file_b_path = filedialog.askopenfilename(title="Select file B")
    
    with open(file_a_path, 'r') as file_a, open(file_b_path, 'r') as file_b:
        file_a_lines = set(file_a.readlines())
        file_b_lines = file_b.readlines()
    
    deleted_lines = 0
    with open(file_b_path, 'w') as file_b:
        for line in file_b_lines:
            if line in file_a_lines:
                deleted_lines += 1
            else:
                file_b.write(line)
    print(f"{deleted_lines} lines were deleted from file B.")

if __name__ == '__main__':
    compare_files()
