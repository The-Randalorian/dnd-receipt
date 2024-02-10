from escpos.printer import Usb

p = Usb(0x6868, 0x0200)  #, 0, profile="TM-T88III"

while True:
    line_count = 0
    with open("text_log.txt", "at") as f:
        f.write("=" * 40 + "\n")
        while True:
            t = input(">> ")
            if len(t) <= 0:
                if line_count <= 0:
                    exit(0)
                break
            line_count += 1
            p.textln(t)
            f.write(t + "\n")
    p.cut()