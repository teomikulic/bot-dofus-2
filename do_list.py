from os import listdir

RACINE = "."
IMAGE_OFFSET = 5


def check_elements():
    result = list()
    for file in listdir(RACINE+"/img/ress/"):
        result.append(RACINE + "/img/ress/" + file)
    return result