# Guide d’installation – AIAssistantStreamer (Windows)

AIAssistantStreamer est un assistant vocal que vous pouvez faire tourner en local sur votre propre PC.

Il vous écoute lorsque vous prononcez un mot-clé (comme "Ok Google"), comprend ce que vous dites, génère une réponse originale grâce à l’intelligence artificielle, puis vous répond avec une voix réaliste.

Vous pouvez également personnaliser des messages d’introduction audio.

<img src="https://raw.githubusercontent.com/anisayari/AIAssitantStreamer/main/assets/topic.png" alt="AIAssistantStreamer" width="800"/>

Un projet proposé par l'ingénieur en intelligence artificielle et créateur de contenu Anis AYARI (Defend Intelligence).

## 🧩 Prérequis

* [Installer **Python 3.11+**](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)
  (⚠️ Cocher **“Add Python to PATH”** pendant l’installation)

## 🗂️ Télécharger le projet

* [Télécharger le ZIP du projet](https://github.com/Yorik56/AIAssitantStreamer/archive/refs/heads/main.zip)
* Extraire dans `C:\Users\VOTRE_NOM\Documents\AIAssistantStreamer`
  (le dossier peut être placé où vous le souhaitez)

## ⚙️ Installation

1. Ouvrir le dossier du projet.
2. Cliquer dans la barre d’adresse du dossier, taper `cmd`, puis appuyer sur **Entrée** pour ouvrir une invite de commandes.
3. Copier les lignes ci-dessous et les coller dans l'invite de commandes. Elles seront exécutées une par une :

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

4. Ouvrir le fichier `.env` avec le Bloc-notes
   (⚠️ Ne rien modifier pour le moment, suivez d’abord les étapes suivantes)

## 🔑 Clé API OpenAI

1. Créer un compte sur : [https://platform.openai.com/](https://platform.openai.com/)
2. Aller sur : [https://platform.openai.com/settings/organization/api-keys](https://platform.openai.com/settings/organization/api-keys)
3. Cliquer sur **Create new secret key** puis copier la clé dans `.env` :

```env
OPENAI_API_KEY=sk-...
```

## 🔊 Clé API ElevenLabs

1. Créer un compte sur : [https://www.elevenlabs.io/](https://www.elevenlabs.io/)
2. Aller sur : [https://elevenlabs.io/app/settings/api-keys](https://elevenlabs.io/app/settings/api-keys)
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

Une wake word est un mot ou une phrase spécifique que l'utilisateur prononce pour activer un assistant vocal, comme "Hey Siri" ou "OK Google".

1. Aller sur : [https://console.picovoice.ai/](https://console.picovoice.ai/)
2. Cliquer sur **Create Wake Word**
3. Choisir la langue (ex. français)
4. Saisir le mot-clé vocal (ex. `Excuse-moi`)
5. Télécharger le fichier `.ppn` généré
6. Placer ce fichier dans le dossier `assets` à la racine du projet
7. Dans `.env` :

```env
KEYWORD_PATH_PORCUPINE=C:\Users\VOTRE_NOM\Documents\AIAssistantStreamer\assets\Excuse-moi_fr_windows_v3_0_0.ppn
```

8. Le fichier `porcupine_params_fr.pv` est déjà présent dans `assets`. Ajouter aussi :

```env
MODEL_PATH_PROCUPINE=C:\Users\VOTRE_NOM\Documents\AIAssistantStreamer\assets\porcupine_params_fr.pv
```

L’assistant répondra vocalement après détection de votre **Wake Word**.

## 🔉 Choisir la voix de votre assistant IA (ElevenLabs)

Par défaut, une voix est déjà configurée dans ce projet, mais vous pouvez si vous le souhaitez en choisir une autre en suivant les étapes suivantes :

1. Se connecter : [https://elevenlabs.io/app/voice-library](https://elevenlabs.io/app/voice-library)
2. Choisir une voix, cliquer sur (...) (More actions)
3. Cliquer sur **Copy voice ID** puis coller cet identifiant dans le `.env`

```env
ELEVENLAB_VOICE_ID=...
```

## 🔉 Générer la voix d’introduction (ElevenLabs)

Les voix d’introduction sont des messages audio courts utilisés pour accueillir ou signaler l’activation d’un assistant vocal.
Par exemple : "Bonjour, comment puis-je vous aider ?"

Par défaut, une voix d'introduction est déjà configurée dans ce projet, mais vous pouvez si vous le souhaitez en ajouter une autre en suivant les étapes suivantes :

1. Se connecter : [https://elevenlabs.io/app/voice-library](https://elevenlabs.io/app/voice-library)
2. Choisir une voix, cliquer sur (+) (Add to my voices), puis cliquer sur T (Use voice)
3. Saisir votre texte, cliquer sur **Generate speech**
4. Télécharger l’audio au format MP3
5. Placer le fichier dans le dossier `voix_intro/`

## ▶️ Lancer l’assistant

```bat
venv\Scripts\activate
python main.py
```

## 🎤 Activer et arrêter l’écoute

* L’assistant reste **en veille** en continu.
* Il s’active dès que vous prononcez le **mot-clé défini** (wake word).
* Pour arrêter l’écoute, **dites simplement “merci”** à la fin d’une interaction.

> Vous pouvez également quitter le programme à tout moment avec `Ctrl+C`.

---

## Annexes

### 🐧 Debian 11 (Linux) – Dépendances pour PyAudio

```bash
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
```
