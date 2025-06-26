# Guide d’installation – AIAssistantStreamer (Windows)

## 👤 Crédits

![AIAssistantStreamer](https://raw.githubusercontent.com/anisayari/AIAssitantStreamer/main/assets/topic.png)

## 🧩 Prérequis

- [Installer **Python 3.11+**](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)  
  (⚠️ Cocher **“Add Python to PATH”** pendant l’installation)

## 🗂️ Télécharger le projet

- [Télécharger le ZIP du projet](https://github.com/anisayari/AIAssistantStreamer/archive/refs/heads/main.zip)
- Extraire dans `C:\Users\VOTRE_NOM\Documents\AIAssistantStreamer`  
  (le dossier peut être placé où vous le souhaitez)

## ⚙️ Installation

1. Ouvrir le dossier du projet.
2. Cliquer dans la barre d’adresse, taper `cmd`, appuyer sur **Entrée**.
3. Exécuter les commandes suivantes :

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
````

4. Ouvrir le fichier `.env` avec le Bloc-notes
   (⚠️ Ne rien modifier pour le moment, suivez d’abord les étapes suivantes)

## 🔑 Clé API OpenAI

1. Créer un compte sur : [https://platform.openai.com/](https://platform.openai.com/)
2. Aller dans : [https://platform.openai.com/settings/organization/api-keys](https://platform.openai.com/settings/organization/api-keys)
3. Cliquer sur **Create new secret key** puis copier la clé dans `.env` :

```env
OPENAI_API_KEY=sk-...
```

## 🔊 Clé API ElevenLabs

1. Créer un compte sur : [https://www.elevenlabs.io/](https://www.elevenlabs.io/)
2. Aller dans : [https://elevenlabs.io/app/settings/api-keys](https://elevenlabs.io/app/settings/api-keys)
3. Cliquer sur **Create API Key**
4. Donner un nom à la clé (ex : `Assistant IA`)
5. Activer **Text to Speech → has access**
6. Copier la clé dans `.env` :

```env
ELEVENLABS_API_KEY=sk-...
```

## 🗣️ Clé API Picovoice

1. Créer un compte sur : [https://picovoice.ai/](https://picovoice.ai/)
2. Une fois connecté, récupérer la clé API affichée
3. Copier la clé dans `.env` :

```env
ACCES_KEY_PORCUPINE=QsRwq...
```

## 🎙️ Générer un Wake Word

1. Aller sur : [https://console.picovoice.ai/](https://console.picovoice.ai/)
2. Cliquer sur **Create Wake Word**
3. Choisir la langue (ex. français)
4. Saisir le mot-clé vocal (ex. `Excuse-moi`)
5. Télécharger le fichier `.ppn` généré
6. Placer ce fichier dans `assets/`
7. Dans `.env` :

```env
KEYWORD_PATH_PORCUPINE=C:\Users\VOTRE_NOM\Documents\AIAssistantStreamer\assets\Excuse-moi_fr_windows_v3_0_0.ppn
```

8. Le fichier `porcupine_params_fr.pv` est déjà présent dans `assets/`. Ajouter aussi :

```env
MODEL_PATH_PROCUPINE=C:\Users\VOTRE_NOM\Documents\AIAssistantStreamer\assets\porcupine_params_fr.pv
```

## ▶️ Lancer l’assistant

```bat
venv\Scripts\activate
python main.py
```

L’assistant répondra vocalement après détection de votre **mot-clé personnalisé**.

## 🔉 Générer les voix d’introduction (ElevenLabs)

1. Se connecter : [https://elevenlabs.io/app/voice-library](https://elevenlabs.io/app/voice-library)
2. Choisir une voix → **Add to my voices** → puis cliquer sur **Use voice**
3. Saisir votre texte → **Generate speech**
4. Télécharger l’audio au format MP3
5. Placer le fichier dans le dossier `voix_intro/`

## 🐧 Debian 11 (Linux) – Dépendances pour PyAudio

```bash
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
```