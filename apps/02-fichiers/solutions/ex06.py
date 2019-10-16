"""
Solution to Exercice 06
"""
# Author: Kaan Eraslan
# License: see, LICENSE

import os
from urllib import request


if __name__ == "__main__":
    impath = os.path.join("assets", "trolltunga.jpg")
    imurl = "http://www.w3schools.com/css/trolltunga.jpg"
    reponse = request.urlopen(imurl)
    data = reponse.read()
    with open(impath, "wb") as fd:
        fd.write(data)
    #
    print("Done!")
