 AI Voice Chatbot & YouTube Assistant

A smart, hands-free Python voice assistant that acts as a conversational AI chatbot and a voice-controlled media manager. Powered by Google Speech Recognition, ChatGPT (via `g4f`), and system-level automation tools, this assistant can chat with you naturally, play videos on YouTube, pause/mute media, or forcefully close the browser window on command.



##  Features

*  Conversational AI Mode:** Talk naturally with an intelligent AI chatbot that responds to your questions with concise, spoken answers.
*  Smart Music Playback:** Say *"Play [Song Name]"* to instantly launch your default browser and start streaming the video on YouTube.
*  Media Controls:** Control your playback by speaking commands like *"Pause"*, *"Resume"*, *"Mute"*, or *"Unmute"*.
*  OS-Level Window Closing:** Say *"Close"* or *"Close window"*, and the assistant will bypass lag or security barriers to forcefully shut your browser instantly.



##  Prerequisites & System Requirements

This project is cross-platform and works on **Windows** and **macOS**. 

### 1. External System Tools (For Microphone Access)
* **macOS Users:** Ensure your Terminal/VS Code has permission to access the Microphone under *System Settings > Privacy & Security > Microphone*.
* **Linux Users:** May need to install `portaudio` before installing dependencies:
    ```bash
    sudo apt-get install portaudio19-dev
    ```



## Installation & Setup

1. **Clone or create your project directory:**
   ```bash
   mkdir ai-voice-assistant
   cd ai-voice-assistant
