import qrcode

links = []
with open('index.html', 'r') as file:
    for ligne in file:
        if "maquette" in ligne:
            links.append("https://chasse-aux-ren-arts.ovh/"+ligne.strip().split('"')[1][2:])

for link in links:
    print(link)
    img = qrcode.make(link)
    img.save("qrcodes/"+link.split('/')[3][9:]+".png")

