# PRD: removeaudio

## Overview
A Python CLI tool that strips audio from video files using ffmpeg. Designed for users who need silent video copies (e.g., for privacy, meme content, or video editing workflows). Processes an entire directory recursively and produces `noaudio_` prefixed output files without re-encoding.

## Goals
- Accept a directory path and process all `.mp4`, `.avi`, `.mov` files within it
- Use ffmpeg stream-copy mode (`-c copy -an`) to strip audio without quality loss
- Skip already-processed files to support re-runs
- Validate input path and ffmpeg availability before processing
- Print per-file status and a final summary

## Non-Goals
- Audio extraction (saving audio only)
- Video format conversion
- Re-encoding with different codecs
- GUI
- Cloud storage integration

## User Stories
- As a content creator, I want to strip audio from 20 clips at once so I can overlay custom music later.
- As a developer, I want a secure alternative to shell-string ffmpeg calls that doesn't allow command injection.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: `subprocess` (stdlib), `os` (stdlib), `sys` (stdlib), `pathlib` (stdlib)
- **External tool**: `ffmpeg` (must be installed separately)

## Architecture
```
removeaudio/
├── noaudio_secure.py    # current production script
├── noaudio.py           # deprecated — exits with security warning
├── noaudio.py.VULNERABLE # original vulnerable version (reference only)
└── requirements.txt
```

**Functions in `noaudio_secure.py`:**
- `validate_directory(path)` → resolved `Path` or `None`
- `check_ffmpeg()` → bool
- `remove_audio_from_video(input_path, output_path)` → `(bool, message)`
- `process_directory(directory)` → prints results
- `main()` → CLI entry point

## Features (detailed)

### Directory Validation
- Resolves symlinks via `Path.resolve()`
- Checks existence, is-directory, read permissions
- Returns `None` on any failure with clear error message

### ffmpeg Check
- Runs `ffmpeg -version` via subprocess with 5s timeout
- Prints install instructions for Windows/macOS/Linux if not found

### Audio Removal
- Command: `["ffmpeg", "-i", input, "-c", "copy", "-an", output, "-y"]`
- `shell=False` — prevents command injection
- 5-minute timeout per file
- Returns success bool + error message string

### File Discovery
- `os.walk()` recursive traversal
- Filters by extension (case-insensitive via `.lower()`)
- Skips files starting with `noaudio_` prefix
- Skips files where output already exists

### Summary Output
```
✅ Processed successfully: N
❌ Failed: N
⏭️  Skipped: N
```

## Data / Config
- No config file — settings are constants in script:
  - `POSSIBLE_EXTENSIONS = ["avi", "mp4", "mov"]`
- Output filename: `noaudio_{original_filename}`

## Deployment / Run
```bash
pip install  # no pip deps
python noaudio_secure.py
# → Enter directory path when prompted
# → Confirm before processing
```

## Constraints & Notes
- **ffmpeg required**: not included — must be installed by user
- **Stream copy**: output is identical quality to input; very fast
- **Timeout**: 300 seconds per file — may need increase for very large files
- **Vulnerable legacy**: `noaudio.py` used `os.system()` with unsanitized input (command injection, CVSS 9.8) — preserved for reference only, now exits immediately
