import csv
import os
from PIL import Image



def images_par_classes():
    cpt = 0
    with open('monstres.md', 'w') as f:
        f.write('# Ensemble des monstres des divers élèves' + '\n')
    for classe in os.listdir(('./monstres')):
            print(classe)
            if classe != '.DS_Store':
                with open('monstres.md', 'a') as f:
                    f.write(f"\n## {classe}"+"\n")
                if classe != '.DS_Store':
                    for image in os.listdir('./monstres/' + classe):
                        print(image)
                        if image != '.DS_Store':
                            if ' ' in image:
                                os.rename('./monstres/' + classe + '/' + image, './monstres/' + classe + '/' + image.replace(' ', '_'))
                            with open('monstres.md', 'a') as f:
                                #f.write("\n### "+image[0:len(image)-4] + '\n')
                                f.write(f"- [{image[0:len(image)-4]}]("+'monstres/' + classe + '/' + image + ')\n')
                                cpt += 1
    print(cpt)

def images_par_classes_2():
    cpt = 0
    with open('liens.txt', 'w') as f:
        f.write('# Ensemble des monstres des divers élèves' + '\n')
    for classe in os.listdir(('./monstres')):
            print(classe)
            if classe != '.DS_Store':
                with open('liens.txt', 'a') as f:
                    f.write(f"\n## {classe}"+"\n")
                if classe != '.DS_Store':
                    for image in os.listdir('./monstres/' + classe):
                        print(image)
                        if image != '.DS_Store':
                            if ' ' in image:
                                os.rename('./monstres/' + classe + '/' + image, './monstres/' + classe + '/' + image.replace(' ', '_'))
                            with open('liens.txt', 'a') as f:
                                chaine = "!["+image[:len(image)-4]+"](./monstres/"+classe+"/"+image+")"
                                chaine += "{"+": style='height:150px;width:150px'"+"}"+'\n'
                                print(chaine)
                                f.write(chaine)
                                cpt += 1

def images_par_classes_3():
    cpt = 0
    with open('monstres.md', 'w') as f:
        f.write('# Ensemble des monstres des divers élèves' + '\n')
    for classe in os.listdir(('./monstres')):
            print(classe)
            if classe != '.DS_Store':
                with open('monstres.md', 'a') as f:
                    f.write(f"\n## {classe}"+"\n")
                    f.write("|"*len([name for name in os.listdir("./monstres/"+classe) if os.path.isfile(os.path.join("./monstres/"+classe, name))])+"|")
                    f.write("\n")
                    f.write("|---"*len([name for name in os.listdir("./monstres/"+classe) if os.path.isfile(os.path.join("./monstres/"+classe, name))])+"|")
                    f.write("\n")
                if classe != '.DS_Store':
                    chaine = ""
                    for image in os.listdir('./monstres/' + classe):
                        if image != '.DS_Store':
                            chaine += "|"+image[:len(image)-4]
                    chaine += "|"
                    with open('monstres.md','a') as f:
                        f.write(chaine)
                        f.write("\n")
                    chaine = ""
                    for image in os.listdir('./monstres/' + classe):
                        if image != '.DS_Store':
                            chaine += "|!["+image[:len(image)-4]+"](./monstres/"+classe+"/"+image+")"
                    chaine += "|"
                    with open('monstres.md','a') as f:
                        f.write(chaine)
                        f.write("\n")

def images_par_classes_4():
    with open('./monstres.md', 'w') as f:
        f.write('# Ensemble des monstres des divers élèves' + '\n')
    for classe in os.listdir(('./monstres')):
            if classe != '.DS_Store':
                with open('./monstres.md', 'a') as f:
                    f.write(f"\n## {classe}")
                    f.write("\n")
                    f.write("\n")
                    f.write("|"*5+"|")
                    f.write("\n")
                    f.write("|---"*5+"|")
                    f.write("\n")
                    liste = [image for image in os.listdir('./monstres/' + classe) if image != '.DS_Store']

                    print(liste)
                    cpt = 0
                    for i,elt in enumerate(liste):
                        if elt == liste[-1]:
                            f.write("|"+str(elt[:len(elt)-4])+"|\n")
                        else:
                            f.write("|"+str(elt[:len(elt)-4]))
                        if (i+1)%5 == 0:
                            f.write("|\n")
                            j = 0
                            chaine = "|"
                            while j < 5:
                                chaine += "!["+liste[cpt][:len(liste[cpt])-4]+"](./monstres/"+classe+"/"+liste[cpt]+")"+"|"
                                j += 1
                                cpt += 1
                            chaine += "|"
                            f.write(chaine+"\n")
                    f.write("|")
                    while cpt < len(liste):
                        f.write("!["+liste[cpt][:len(liste[cpt])-4]+"](./monstres/"+classe+"/"+liste[cpt]+")"+"|")
                        cpt+=1
                    f.write("\n")

def redimensionner_images():
    dico = []
    with open('indexation_redimensionnee.csv','r') as f:
        lecteur = csv.reader(f, delimiter="\n")
        for ligne in lecteur:
            dico.append(ligne)
    print(dico[0])
    for classe in os.listdir(('./monstres')):
        if classe != '.DS_Store':
            for image in os.listdir('./monstres/' + classe):
                if image != '.DS_Store' and ".pdf" not in image:
                    print(dico[0] == [classe+" "+image])
                    if [classe+" "+image] not in dico:
                        print("bite")
                        img = Image.open('./monstres/'+classe+"/"+image)
                        img = img.convert("P", palette=Image.Palette.ADAPTIVE, colors=256)
                        img.save(f"./monstres/{classe}/{image}", optimize=True)
                        with open('indexation_redimensionnee.csv','a') as f:
                            f.write(classe+" "+image)
                            f.write("\n")
            

redimensionner_images()
#images_par_classes_4()
