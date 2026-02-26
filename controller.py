import mido
import pyautogui
import sys
import ctypes

# MIDI設定
MIDI_PORT_NAME = 'iRig KEYS 25 0'

# ノート番号の範囲設定
REJECT_RANGE = range(0, 60)   # C4 未満
APPROVE_RANGE = range(60, 128) # C4 以上

def hide_console():
    """コンソールウィンドウを非表示にする"""
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    hWnd = kernel32.GetConsoleWindow()
    if hWnd:
        user32.ShowWindow(hWnd, 0) # 0 = SW_HIDE

def start_controller():
    # ウィンドウを非表示にする
    hide_console()
    
    try:
        with mido.open_input(MIDI_PORT_NAME) as inport:
            for msg in inport:
                if msg.type == 'note_on' and msg.velocity > 0:
                    if msg.note in APPROVE_RANGE:
                        pyautogui.hotkey('alt', 'enter')
                    elif msg.note in REJECT_RANGE:
                        pyautogui.press('esc')
    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    start_controller()
