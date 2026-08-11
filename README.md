# removeaudio

Live demo: https://hongyime.github.io/removeaudio/

![Project screenshot](./screenshot.png)

> Strip audio tracks from video files (MP4, AVI, MOV) using ffmpeg — secure version

## What it does
Batch-processes all video files in a directory and produces muted copies prefixed with `noaudio_`. Uses `ffmpeg` with stream-copy mode (no re-encoding — very fast). The secure version (`noaudio_secure.py`) uses subprocess list args to prevent command injection.

## Features
- Supports `.mp4`, `.avi`, `.mov` files (case-insensitive)
- No re-encoding — copies streams directly (`-c copy -an`), preserving quality
- Skips already-processed files (those starting with `noaudio_`)
- Skips files where output already exists
- Validates directory and ffmpeg availability before processing
- Prints per-file status + final summary

## Requirements
```
Python 3.x
ffmpeg installed and in PATH
```

## Usage
```bash
python noaudio_secure.py
# Enter directory path when prompted
```

> **Note**: The legacy `noaudio.py` has critical security vulnerabilities (command injection, CVSS 9.8) and exits with a warning. Always use `noaudio_secure.py`.

## Installation (ffmpeg)
- Windows: `choco install ffmpeg`
- macOS: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`

## License

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
