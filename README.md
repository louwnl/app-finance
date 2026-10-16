# Mes Comptes

App téléphone pour faire ses comptes : comprendre l'historique, puis prévoir les dépenses à venir.

- **Comptes** : tu donnes le solde de chaque compte à une date que tu connais et son découvert autorisé, puis tu déclares tes opérations avant et après. Le solde est recalculé jour par jour.
- **Avances à se faire rembourser** : une dépense peut être cochée « À me faire rembourser » (par qui, combien). L'accueil liste ce qu'on te doit ; une fois remboursée, l'app ajoute le remboursement reçu. L'analyse ne compte que la part restée à ta charge.
- **Échéancier** : prêts (étudiants, renouvelable, conso), salaire, aide familiale, APL, charges fixes et achats PayPal en 4 fois. Leurs prélèvements sont ajoutés automatiquement, sur le passé comme sur le futur. Un mois différent se corrige en touchant la ligne.
- **Analyse** : évolution du solde, dépenses par catégorie, part des revenus partie en crédits, mois dans le rouge.
- **Prévisions** : solde prévu jusqu'à 2 ans, date d'un éventuel découvert, fins de crédits.

## Installer l'app sur Android (APK)

Sur ton téléphone, télécharge le dernier APK : https://github.com/louwnl/app-finance/releases/latest/download/mes-comptes.apk

Ouvre le fichier téléchargé. La première fois, Android demande d'autoriser l'installation depuis ton navigateur ou ton gestionnaire de fichiers : accepte, puis touche **Installer**. Ensuite, l'app vérifie elle-même s'il existe une nouvelle version : un bandeau « Mettre à jour » apparaît sur l'accueil, et le bouton « Rechercher une mise à jour » est en bas de l'accueil. La nouvelle version s'installe par-dessus et garde tes données.

Chaque modification fusionnée dans `main` compile un nouvel APK et le publie dans les Releases du dépôt (workflow `.github/workflows/android.yml`).

## Version web (iPhone ou navigateur)

Si GitHub Pages est activé (Settings → Pages, branche `main`, dossier `/ (root)`), l'app est aussi sur https://louwnl.github.io/app-finance/. Elle s'ajoute à l'écran d'accueil depuis Safari (Partager → « Sur l'écran d'accueil ») ou Chrome. Ses données sont séparées de celles de l'APK : passe par Exporter / Importer pour les transférer.

## Tes données

Tout reste sur ton téléphone : rien n'est envoyé en ligne, même si le code est public. Pense à faire **Exporter** de temps en temps (Accueil, en bas) et à garder le fichier dans tes fichiers ou tes mails. **Importer** recharge une sauvegarde, par exemple sur un nouveau téléphone.

## Fichiers

- `index.html` : toute l'app (HTML, CSS, JavaScript, sans dépendance).
- `manifest.webmanifest`, `icons/` : nom et icône sur l'écran d'accueil.
- `sw.js` : fonctionnement hors connexion de la version web. Change `VERSION` à chaque modification.
- `package.json`, `capacitor.config.json` : emballage Android avec Capacitor. Le dossier `android/` est généré pendant la compilation.
- `android-res/`, `scripts/icons.py` : icônes Android et web (`python3 scripts/icons.py` les régénère).
- Signature de l'APK : la clé vient des secrets GitHub `ANDROID_KEYSTORE_BASE64` (le fichier .jks encodé en base64) et `ANDROID_KEYSTORE_PASSWORD`. Elle doit rester la même pour que les mises à jour s'installent par-dessus sans perdre les données. Sans ces secrets, l'APK est signé avec une clé temporaire.

Compiler en local (avec Android Studio) : `npm ci && npm run web && npx cap add android && cp -r android-res/* android/app/src/main/res/ && npx cap open android`.
