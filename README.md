# removeaudio
code to remove audio from MP4, AVI and MOV video files.

<p align="left">
  <img src="https://cdn.iconscout.com/icon/free/png-512/vlc-media-player-2-569258.png" width="300" height="300"/>
</p>

## 🔒 Security Notice

**⚠️ IMPORTANT: Version 2.0 includes critical security fixes**

The original `noaudio.py` has been deprecated due to **CRITICAL security vulnerabilities**:
- **Command Injection (CVSS 9.8)** - Malicious filenames could execute arbitrary commands
- **Path Traversal** - No validation of directory paths
- **Poor Error Handling** - May fail silently

**Please use `noaudio_secure.py` instead of `noaudio.py`**

---

## 📋 Requirements

### System Requirements
- Python 3.6 or higher
- ffmpeg (must be installed and in PATH)

### Installing ffmpeg

**Windows:**
```bash
choco install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**Verify Installation:**
```bash
ffmpeg -version
```

---

## 🚀 Usage

### Secure Version (Recommended)
```bash
python noaudio_secure.py
```

### Features
- ✅ Secure command execution (no injection risk)
- ✅ Path validation and sanitization
- ✅ Dependency checking
- ✅ Progress reporting
- ✅ Error handling
- ✅ User confirmation before processing

---

## Instructions:
1. Download the repo as a zip file
2. Unzip the file
3. Install ffmpeg (see requirements above)
4. Run `python noaudio_secure.py` (NOT noaudio.py)
5. Enter the directory path to the folder where your videos are stored
6. Confirm to proceed
7. Wait for processing to complete

---

## ⚠️ Security Warnings

### Original Version (noaudio.py)
The original `noaudio.py` has known security vulnerabilities and has been deprecated.

**DO NOT USE** `noaudio.py` with untrusted video files or directories.

### Safe Usage Guidelines
1. ✅ Use `noaudio_secure.py` instead
2. ✅ Only process files from trusted sources
3. ✅ Backup important files before processing
4. ✅ Review filenames for suspicious characters
5. ✅ Run in isolated environment if processing untrusted files

---

## Disclaimer:
1. This tool modifies video files. Always backup your original files before processing.
2. The original `noaudio.py` has critical security vulnerabilities and should not be used.
3. Use `noaudio_secure.py` for safe operation.
