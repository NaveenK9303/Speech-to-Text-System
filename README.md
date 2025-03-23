# Speech-to-Text System Using Python

## 📌 Project Overview
This project implements a **Speech-to-Text system** using **Google's Speech Recognition API**. It allows users to convert spoken words into text, either from a **microphone** or from an **audio file**.

## 🚀 Features
- **Real-time Speech Recognition** using a microphone.
- **Transcription from Audio Files** (`.wav` format).
- **Google Speech-to-Text API** for accurate recognition.
- **Handles background noise and errors gracefully.**
- **Supports both online and offline speech recognition.**

## ⚙️ Installation
### **1️⃣ Install Required Libraries**
Ensure you have Python installed, then run:
```bash
pip install SpeechRecognition pyaudio pydub
```

### **2️⃣ Manually Install PyAudio (If Needed)**
#### **For Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```
#### **For Linux/macOS:**
```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

## 📜 Usage
### **Run the script:**
```bash
python speech_to_text.py
```
### **Choose an option:**
- `1` → Convert speech from **microphone** to text.
- `2` → Convert speech from an **audio file** (WAV format required).

### **Example Inputs & Outputs**
#### **🎤 Microphone Input:**
```
🎤 Speak now...
📝 Recognized Speech: Hello, how are you?
```
#### **🎵 Audio File Input:**
```
🎵 Processing audio file: sample.wav
📝 Recognized Text from File: Welcome to the AI internship program.
```

## 📂 File Structure
```
📁 speech-to-text/
├── speech_to_text.py  # Main Python script
├── README.md  # Project documentation
├── sample.wav  # Example audio file
```

## 🔥 Future Improvements
- [ ] Support for **multiple languages**.
- [ ] Implement **offline transcription** using Wav2Vec.
- [ ] Build a **Graphical User Interface (GUI)**.
- [ ] Enable **real-time translation** from speech.

## 🤝 Contributing
Pull requests are welcome! If you'd like to contribute, please open an issue first to discuss proposed changes.

## 📜 License
This project is licensed under the MIT License.

---
👨‍💻 Developed by **[Your Name]**

