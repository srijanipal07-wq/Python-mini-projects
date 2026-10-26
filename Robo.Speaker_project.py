import os

if __name__ == '__main__':
    print("Welcome to the Robo Speaker Project! Created by Srijan!")
    x = input("Enter what you want to speak: ")
    
    # Windows PowerShell text-to-speech command
    command = f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
    
    os.system(command)