from bs4 import BeautifulSoup

# Lecture des données
f = open("recette.html", "r")
html_content = f.read()
f.close()

soup = BeautifulSoup(html_content, "html.parser")
titre_h1 = soup.find("h1")
texte_titre = titre_h1.text

print("Titre de la page HTML:", texte_titre)

p = soup.find("p", class_="description") 
# ou
# liste_div_centre = soup.find_all("div", class_="centre")
# if liste_div_centre and len(liste_div_centre) >= 2:
#   p = liste_div_centre[1].find("p", class_="description")

div_image = soup.find("div", class_="info")
image = div_image.find("img", class_="centre info")

print("Paragraphe de description:", p.text)
print("Le src de l'image est:", image["src"])

