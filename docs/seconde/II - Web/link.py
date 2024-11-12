import os

def images_par_classes():
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
images_par_classes()
