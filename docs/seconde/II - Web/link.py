import os

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
    print(cpt)
images_par_classes_2()
