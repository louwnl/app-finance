# Mes Comptes

App téléphone pour faire ses comptes : comprendre l'historique, puis prévoir les dépenses à venir.

- **Comptes** : tu donnes le solde de chaque compte à une date que tu connais, puis tu déclares tes opérations avant et après. Le solde est recalculé jour par jour.
- **Échéancier** : prêts (étudiants, renouvelable, conso), salaire, aide familiale, APL, charges fixes et achats PayPal en 4 fois. Leurs prélèvements sont ajoutés automatiquement, sur le passé comme sur le futur. Un mois différent se corrige en touchant la ligne.
- **Analyse** : évolution du solde, dépenses par catégorie, part des revenus partie en crédits, mois dans le rouge.
- **Prévisions** : solde prévu jusqu'à 2 ans, date d'un éventuel découvert, fins de crédits.

## Installer l'app sur ton téléphone

L'app est publiée sur GitHub Pages : https://louwnl.github.io/app-finance/

- **iPhone** : ouvre le lien dans Safari, touche le bouton Partager, puis « Sur l'écran d'accueil ».
- **Android** : ouvre le lien dans Chrome, menu ⋮, puis « Installer l'application » (ou « Ajouter à l'écran d'accueil »).

Elle s'ouvre ensuite en plein écran avec son icône et marche sans connexion.

## Tes données

Tout reste sur ton téléphone : rien n'est envoyé en ligne, même si le code est public. Pense à faire **Exporter** de temps en temps (Accueil, en bas) et à garder le fichier dans tes fichiers ou tes mails. **Importer** recharge une sauvegarde, par exemple sur un nouveau téléphone.

## Mettre en ligne (une seule fois)

Dans le dépôt GitHub : **Settings → Pages → Build and deployment**, source « Deploy from a branch », branche `main`, dossier `/ (root)`, puis **Save**.

## Fichiers

- `index.html` : toute l'app (HTML, CSS, JavaScript, sans dépendance).
- `manifest.webmanifest`, `icons/` : nom et icône sur l'écran d'accueil.
- `sw.js` : fonctionnement hors connexion. Change `VERSION` à chaque modification pour que les téléphones récupèrent la nouvelle version.
