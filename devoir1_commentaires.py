### BONJOUR, ICI JHR ###
### Mes notes et corrections sont précédées de trois dièses ###

### Oups 1 -> il fallait que ton script se termine par «.py»

### Oups 2 -> Il fallait conserver la variable publications.
### Sinon, si tu la laissais dans un autre fichier appelé «devoir1.py», il fallait l'importer avec le code suivant:

from devoir1 import publications ### Petit hack sympathique (j'ai rajouté le fichier «devoir1.py» original)

### Enfin, chapeau pour une solution très élégante au problème contenu dans ce devoir!

# on crée une première liste pour isoler les médias dans chacune des lignes
media_cru = []
for i in publications:	
	media_cru.append(i[0])

### print(media_cru)

# on crée la nouvelle liste de média propre en vérifiant que le nom du média n'est pas déjà dans la liste propre
media_propre = []
for media_sale in media_cru:
	if media_sale not in media_propre:
		media_propre.append(media_sale)

### print(media_propre)

# Initialisation de l'index
nombre_de_boucle = 0

for media in media_propre:

	# Paramètres initiaux pour chacun des elements dans media propre
	partage = 0
	reaction = 0
	commentaires = 0
	total = 0
	
	# Boucle dans chacune des lignes du document de publication
	for ligne_de_donnees in publications:
		
		# Accumulation des donnees pour chacun des elements dans media propre
		if ligne_de_donnees[0] == media:
			
			partage += ligne_de_donnees[3]
			reaction += ligne_de_donnees[4]
			commentaires += ligne_de_donnees[5]
		
		total = partage + reaction + commentaires


	message = str(nombre_de_boucle + 1) + " Les publications du média " + str(media) + " ont été partagées " + str(partage) + " fois, ont provoqué " + str(reaction) + " réactions, et ont généré " + str(commentaires) + " commentaires, pour un engagement total de " + str(total) + " en 2017."
	print(message)
	
	nombre_de_boucle += 1
