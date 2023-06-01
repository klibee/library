# modules
# ================================================
import random


# function
# =======================================
def product(self):

    # catalog
    items = catalog()
    item  = random.choice(items)

    # bye
    return {
         "title": item[0],
         "price": item[1],
      "category": item[2],
         "stock": random.randint(1, 999),
    }


# function
# =======================================
def catalog():

    items = []

    # televisores
    items.append(["Samsung QLED 4K Q80A", "$1,299", "televisores"])
    items.append(["LG OLED CX Series", "$1,899", "televisores"])
    items.append(["Sony X950H 4K Ultra HD", "$1,599", "televisores"])
    items.append(["TCL 6-Series 4K QLED", "$799", "televisores"])
    items.append(["Samsung Crystal UHD 4K TU8000", "$699", "televisores"])
    items.append(["LG NanoCell 85 Series", "$1,199", "televisores"])
    items.append(["Sony A8H OLED 4K Ultra HD", "$2,299", "televisores"])
    items.append(["Vizio OLED 4K UHD", "$1,799", "televisores"])
    items.append(["Samsung Frame QLED 4K LS03A", "$1,499", "televisores"])
    items.append(["LG OLED C1 Series", "$2,099", "televisores"])
    items.append(["Sony X800H 4K Ultra HD", "$899", "televisores"])
    items.append(["TCL 5-Series 4K QLED", "$599", "televisores"])
    items.append(["Samsung QLED Q70T Series", "$1,099", "televisores"])
    items.append(["LG NanoCell 90 Series", "$1,399", "televisores"])
    items.append(["Sony X900H 4K Ultra HD", "$1,299", "televisores"])
    items.append(["Vizio M-Series Quantum 4K", "$799", "televisores"])
    items.append(["Samsung Crystal UHD 4K TU7000", "$549", "televisores"])
    items.append(["LG OLED BX Series", "$1,799", "televisores"])
    items.append(["Sony X950G 4K Ultra HD", "$1,399", "televisores"])
    items.append(["TCL 4-Series 4K UHD", "$399", "televisores"])


    # tablets
    items.append(["Apple iPad Pro (2021)", "$999", "tablets"])
    items.append(["Samsung Galaxy Tab S7+", "$849", "tablets"])
    items.append(["Microsoft Surface Pro 7", "$899", "tablets"])
    items.append(["Lenovo Tab P11 Pro", "$499", "tablets"])
    items.append(["Huawei MatePad Pro", "$599", "tablets"])
    items.append(["Amazon Fire HD 10", "$149", "tablets"])
    items.append(["Google Pixel Slate", "$799", "tablets"])
    items.append(["Samsung Galaxy Tab S6 Lite", "$299", "tablets"])
    items.append(["Apple iPad Air (2020)", "$599", "tablets"])
    items.append(["Lenovo Yoga Tab 13", "$599", "tablets"])
    items.append(["Huawei MediaPad M5 Lite", "$279", "tablets"])
    items.append(["Amazon Fire HD 8 Plus", "$109", "tablets"])
    items.append(["Microsoft Surface Go 2", "$399", "tablets"])
    items.append(["Samsung Galaxy Tab A7", "$229", "tablets"])
    items.append(["Apple iPad Mini (2021)", "$399", "tablets"])
    items.append(["Lenovo Tab M10 Plus", "$179", "tablets"])
    items.append(["Huawei MatePad 11", "$349", "tablets"])
    items.append(["Google Nexus 9", "$399", "tablets"])
    items.append(["Amazon Fire HD 7", "$49", "tablets"])
    items.append(["Samsung Galaxy Tab S5e", "$399", "tablets"])


    # teléfonos
    items.append(["iPhone 13 Pro", "$999", "teléfonos"])
    items.append(["Samsung Galaxy S21 Ultra", "$1,199", "teléfonos"])
    items.append(["Google Pixel 6 Pro", "$899", "teléfonos"])
    items.append(["OnePlus 9 Pro", "$1,069", "teléfonos"])
    items.append(["Xiaomi Mi 11 Ultra", "$1,199", "teléfonos"])
    items.append(["Huawei P40 Pro", "$999", "teléfonos"])
    items.append(["Sony Xperia 1 III", "$1,299", "teléfonos"])
    items.append(["LG Wing 5G", "$999", "teléfonos"])
    items.append(["Motorola Edge+", "$999", "teléfonos"])
    items.append(["Samsung Galaxy Note 20 Ultra", "$1,299", "teléfonos"])
    items.append(["iPhone 13", "$799", "teléfonos"])
    items.append(["Google Pixel 6", "$699", "teléfonos"])
    items.append(["OnePlus 9", "$729", "teléfonos"])
    items.append(["Xiaomi Mi 11", "$799", "teléfonos"])
    items.append(["Huawei Mate 40 Pro", "$999", "teléfonos"])
    items.append(["Sony Xperia 5 III", "$1,099", "teléfonos"])
    items.append(["LG Velvet 5G", "$699", "teléfonos"])
    items.append(["Motorola Edge", "$699", "teléfonos"])
    items.append(["Samsung Galaxy S21", "$799", "teléfonos"])
    items.append(["iPhone SE (2020)", "$399", "teléfonos"])


    # notebooks
    items.append(["Apple MacBook Pro (2021)", "$1,299", "notebooks"])
    items.append(["Dell XPS 13", "$1,199", "notebooks"])
    items.append(["HP Spectre x360", "$1,099", "notebooks"])
    items.append(["Lenovo ThinkPad X1 Carbon", "$1,499", "notebooks"])
    items.append(["Asus ZenBook 14", "$999", "notebooks"])
    items.append(["Microsoft Surface Laptop 4", "$1,299", "notebooks"])
    items.append(["Acer Swift 5", "$899", "notebooks"])
    items.append(["MSI GS66 Stealth", "$1,999", "notebooks"])
    items.append(["Razer Blade 15", "$1,799", "notebooks"])
    items.append(["Apple iMac (2021)", "$1,299", "notebooks"])
    items.append(["Dell Alienware m15 R4", "$2,399", "notebooks"])
    items.append(["HP Envy x360", "$899", "notebooks"])
    items.append(["Lenovo Yoga C940", "$1,199", "notebooks"])
    items.append(["Asus ROG Zephyrus G14", "$1,499", "notebooks"])
    items.append(["Microsoft Surface Book 3", "$1,599", "notebooks"])
    items.append(["Acer Predator Helios 300", "$1,299", "notebooks"])
    items.append(["MSI Prestige 14", "$1,299", "notebooks"])
    items.append(["Razer Blade Pro 17", "$2,499", "notebooks"])
    items.append(["Apple Mac Mini (2021)", "$699", "notebooks"])
    items.append(["Dell Inspiron 15 7000", "$999", "notebooks"])


    # monitores
    items.append(["Dell Ultrasharp U2719D", "$399", "monitores"])
    items.append(["LG 27UK850-W", "$449", "monitores"])
    items.append(["ASUS ROG Swift PG279Q", "$699", "monitores"])
    items.append(["Samsung Odyssey G7", "$799", "monitores"])
    items.append(["Acer Predator X27", "$1,799", "monitores"])
    items.append(["BenQ PD2700U", "$499", "monitores"])
    items.append(["ViewSonic VP3268-4K", "$899", "monitores"])
    items.append(["HP Z27", "$499", "monitores"])
    items.append(["AOC CQ32G1", "$349", "monitores"])
    items.append(["MSI Optix MAG271CQR", "$399", "monitores"])
    items.append(["Philips 276E8VJSB", "$329", "monitores"])
    items.append(["LG 34UC80-B", "$549", "monitores"])
    items.append(["Dell S3221QS", "$499", "monitores"])
    items.append(["ASUS TUF Gaming VG27AQ", "$499", "monitores"])
    items.append(["Samsung UR59C", "$399", "monitores"])
    items.append(["Acer Nitro XV273K", "$799", "monitores"])
    items.append(["BenQ EX2780Q", "$599", "monitores"])
    items.append(["ViewSonic XG2402", "$249", "monitores"])
    items.append(["HP VH240a", "$159", "monitores"])
    items.append(["AOC 24G2", "$199", "monitores"])


    # impresoras
    items.append(["Epson EcoTank ET-2720", "$199", "impresoras"])
    items.append(["Canon PIXMA TR4520", "$79", "impresoras"])
    items.append(["HP OfficeJet Pro 9015", "$229", "impresoras"])
    items.append(["Brother HL-L2380DW", "$189", "impresoras"])
    items.append(["Epson WorkForce WF-7720", "$299", "impresoras"])
    items.append(["Canon imageCLASS MF743Cdw", "$399", "impresoras"])
    items.append(["HP LaserJet Pro M281fdw", "$329", "impresoras"])
    items.append(["Brother MFC-L2750DW", "$249", "impresoras"])
    items.append(["Epson SureColor P800", "$1,195", "impresoras"])
    items.append(["Canon PIXMA PRO-100", "$379", "impresoras"])
    items.append(["HP ENVY Photo 7155", "$149", "impresoras"])
    items.append(["Brother HL-L6200DW", "$249", "impresoras"])
    items.append(["Epson Expression Photo XP-970", "$249", "impresoras"])
    items.append(["Canon imagePROGRAF PRO-1000", "$1,299", "impresoras"])
    items.append(["HP LaserJet Pro M404dn", "$299", "impresoras"])
    items.append(["Brother DCP-L2540DW", "$169", "impresoras"])
    items.append(["Epson WorkForce Pro WF-3720", "$149", "impresoras"])
    items.append(["Canon PIXMA iP8720", "$249", "impresoras"])
    items.append(["HP DeskJet 3755", "$69", "impresoras"])
    items.append(["Brother MFC-J995DW", "$199", "impresoras"])


    # consolas
    items.append(["PlayStation 5", "$499", "consolas"])
    items.append(["Xbox Series X", "$499", "consolas"])
    items.append(["Nintendo Switch", "$299", "consolas"])
    items.append(["PlayStation 4 Pro", "$399", "consolas"])
    items.append(["Xbox One X", "$499", "consolas"])
    items.append(["Nintendo Switch Lite", "$199", "consolas"])
    items.append(["PlayStation 4 Slim", "$299", "consolas"])
    items.append(["Xbox One S", "$299", "consolas"])
    items.append(["Nintendo 3DS XL", "$199", "consolas"])
    items.append(["PlayStation Classic", "$59", "consolas"])
    items.append(["Xbox Series S", "$299", "consolas"])
    items.append(["Nintendo Wii U", "$299", "consolas"])
    items.append(["PlayStation Vita", "$199", "consolas"])
    items.append(["Xbox 360 E", "$199", "consolas"])
    items.append(["Nintendo 2DS", "$79", "consolas"])
    items.append(["Atari Flashback 8", "$49", "consolas"])
    items.append(["Sega Genesis Mini", "$79", "consolas"])
    items.append(["Super Nintendo Classic Edition", "$79", "consolas"])
    items.append(["Neo Geo Mini", "$109", "consolas"])
    items.append(["TurboGrafx-16 Mini", "$99", "consolas"])


    # drones
    items.append(["DJI Phantom 4 Pro", "$1,499", "drones"])
    items.append(["Parrot Anafi", "$699", "drones"])
    items.append(["Autel Evo II", "$1,495", "drones"])
    items.append(["DJI Mavic 2 Pro", "$1,599", "drones"])
    items.append(["Holy Stone HS720", "$299", "drones"])
    items.append(["Yuneec Typhoon H Pro", "$1,299", "drones"])
    items.append(["DJI Mini 2", "$449", "drones"])
    items.append(["Autel Evo Lite", "$899", "drones"])
    items.append(["Parrot Bebop 2", "$399", "drones"])
    items.append(["DJI Mavic Air 2", "$799", "drones"])
    items.append(["Holy Stone HS110D", "$129", "drones"])
    items.append(["Yuneec Mantis Q", "$499", "drones"])
    items.append(["DJI Phantom 3 Standard", "$499", "drones"])
    items.append(["Autel X-Star Premium", "$799", "drones"])
    items.append(["Parrot Disco FPV", "$699", "drones"])
    items.append(["DJI Spark", "$499", "drones"])
    items.append(["Holy Stone HS100", "$229", "drones"])
    items.append(["Yuneec Breeze", "$179", "drones"])
    items.append(["Blade Chroma Camera Drone", "$699", "drones"])
    items.append(["DJI Inspire 2", "$2,999", "drones"])


    # cámaras
    items.append(["Canon EOS R6", "$2,499", "cámaras"])
    items.append(["Sony Alpha a7 III", "$1,999", "cámaras"])
    items.append(["Nikon Z6 II", "$1,999", "cámaras"])
    items.append(["Fujifilm X-T4", "$1,699", "cámaras"])
    items.append(["Panasonic Lumix GH5", "$1,399", "cámaras"])
    items.append(["Olympus OM-D E-M1 Mark III", "$1,799", "cámaras"])
    items.append(["Leica Q2", "$4,995", "cámaras"])
    items.append(["Sony Cyber-shot RX100 VII", "$1,299", "cámaras"])
    items.append(["Canon EOS 5D Mark IV", "$2,799", "cámaras"])
    items.append(["Nikon D850", "$2,999", "cámaras"])
    items.append(["Fujifilm X-Pro3", "$1,799", "cámaras"])
    items.append(["Panasonic Lumix S1", "$2,499", "cámaras"])
    items.append(["Olympus PEN-F", "$1,099", "cámaras"])
    items.append(["Sony Alpha a6600", "$1,399", "cámaras"])
    items.append(["Canon EOS M6 Mark II", "$1,099", "cámaras"])
    items.append(["Nikon Z7 II", "$2,999", "cámaras"])
    items.append(["Fujifilm X100V", "$1,399", "cámaras"])
    items.append(["Panasonic Lumix LX100 II", "$999", "cámaras"])
    items.append(["Olympus Tough TG-6", "$449", "cámaras"])
    items.append(["Sony Alpha a6400", "$999", "cámaras"])

    # bye
    return items


