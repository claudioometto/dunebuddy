import argparse
from alerts import storm_alert
from vision import screen_capture
from voice import speaker

def main(debug=False):
    if debug:
        print("[DEBUG] Iniciando Dunebuddy em modo debug...")

    img = screen_capture.capture_screen()
    if debug:
        print("[DEBUG] Captura de tela realizada.")

    if storm_alert.detect_storm(img):
        if debug:
            print("[DEBUG] Tempestade detectada.")
        speaker.say("Tempestade à vista. Hora de recuar.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--modo-debug", action="store_true", help="Ativa o modo debug no terminal")
    args = parser.parse_args()
    main(debug=args.modo_debug)
