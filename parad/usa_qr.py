import qrcode
from pathlib import Path
import sys, os, subprocess


def generate_qr_code(
    data: str, filename: str = "qrcode.png", open_after: bool = True
) -> str:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # salva em um caminho absoluto (ex.: Desktop)
    out_path = Path(filename)
    if not out_path.suffix:
        out_path = out_path.with_suffix(".png")
    if not out_path.is_absolute():
        out_path = (
            Path.home() / "Desktop" / out_path.name
        )  # mude se preferir outra pasta

    img.save(out_path)
    print(f"QR code salvo em: {out_path}")

    if open_after:
        try:
            if sys.platform.startswith("win"):
                os.startfile(str(out_path))
            elif sys.platform == "darwin":
                subprocess.run(["open", str(out_path)], check=False)
            else:
                subprocess.run(["xdg-open", str(out_path)], check=False)
        except Exception as e:
            print(f"Não consegui abrir automaticamente: {e}")

    return str(out_path)


if __name__ == "__main__":
    text = input("Texto/URL para o QR: ").strip()
    generate_qr_code(text)
