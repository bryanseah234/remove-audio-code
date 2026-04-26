#!/usr/bin/env python3
"""
Secure video audio removal tool
Fixes: Command injection, path traversal, error handling
"""
import subprocess
import os
import sys
from pathlib import Path

POSSIBLE_EXTENSIONS = ["avi", "mp4", "mov"]

def validate_directory(directory_path):
    """Validate and sanitize directory path"""
    try:
        # Convert to absolute path and resolve symlinks
        path = Path(directory_path).resolve()
        
        # Check if directory exists
        if not path.exists():
            print(f"❌ Error: Directory does not exist: {path}")
            return None
        
        # Check if it's actually a directory
        if not path.is_dir():
            print(f"❌ Error: Path is not a directory: {path}")
            return None
        
        # Check read permissions
        if not os.access(path, os.R_OK):
            print(f"❌ Error: No read permission for directory: {path}")
            return None
        
        return path
    except Exception as e:
        print(f"❌ Error validating directory: {e}")
        return None

def check_ffmpeg():
    """Check if ffmpeg is installed and accessible"""
    try:
        result = subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return True
        else:
            print("❌ Error: ffmpeg is installed but not working correctly")
            return False
    except FileNotFoundError:
        print("❌ Error: ffmpeg is not installed or not in PATH")
        print("Please install ffmpeg:")
        print("  Windows: choco install ffmpeg")
        print("  macOS: brew install ffmpeg")
        print("  Linux: sudo apt-get install ffmpeg")
        return False
    except Exception as e:
        print(f"❌ Error checking ffmpeg: {e}")
        return False

def remove_audio_from_video(input_path, output_path):
    """
    Remove audio from video file using ffmpeg
    Uses secure subprocess call with list arguments
    """
    try:
        # Build command as list (prevents command injection)
        command = [
            "ffmpeg",
            "-i", str(input_path),
            "-c", "copy",
            "-an",
            str(output_path),
            "-y"  # Overwrite output file if exists
        ]
        
        # Execute with shell=False (secure)
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode == 0:
            return True, "Success"
        else:
            return False, f"ffmpeg error: {result.stderr}"
    
    except subprocess.TimeoutExpired:
        return False, "Timeout: Video processing took too long"
    except Exception as e:
        return False, f"Error: {str(e)}"

def process_directory(directory):
    """Process all video files in directory"""
    processed = 0
    failed = 0
    skipped = 0
    
    print(f"🔍 Searching for video files in: {directory}")
    print(f"📹 Looking for extensions: {', '.join(POSSIBLE_EXTENSIONS)}")
    print()
    
    # Walk through directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Check if file has valid extension
            if '.' not in filename:
                continue
            
            ext = filename.rsplit('.', 1)[-1].lower()
            if ext not in POSSIBLE_EXTENSIONS:
                continue
            
            # Skip files that already have "noaudio_" prefix
            if filename.startswith("noaudio_"):
                skipped += 1
                continue
            
            # Build paths
            input_path = Path(root) / filename
            output_filename = f"noaudio_{filename}"
            output_path = Path(root) / output_filename
            
            # Check if output file already exists
            if output_path.exists():
                print(f"⏭️  Skipping (output exists): {filename}")
                skipped += 1
                continue
            
            print(f"🎬 Processing: {filename}")
            
            # Remove audio
            success, message = remove_audio_from_video(input_path, output_path)
            
            if success:
                print(f"✅ Success: {output_filename}")
                processed += 1
            else:
                print(f"❌ Failed: {filename} - {message}")
                failed += 1
            
            print()
    
    # Summary
    print("=" * 60)
    print("📊 PROCESSING SUMMARY")
    print("=" * 60)
    print(f"✅ Processed successfully: {processed}")
    print(f"❌ Failed: {failed}")
    print(f"⏭️  Skipped: {skipped}")
    print(f"📁 Total files: {processed + failed + skipped}")
    print()

def main():
    """Main execution flow"""
    print("=" * 60)
    print("🎬 VIDEO AUDIO REMOVAL TOOL")
    print("=" * 60)
    print()
    
    # Check ffmpeg
    print("🔧 Checking dependencies...")
    if not check_ffmpeg():
        sys.exit(1)
    print("✅ ffmpeg is installed and working")
    print()
    
    # Get directory from user
    directory_input = input("📁 Enter directory path containing video files: ").strip()
    
    # Validate directory
    directory = validate_directory(directory_input)
    if directory is None:
        sys.exit(1)
    
    print(f"✅ Directory validated: {directory}")
    print()
    
    # Confirm before processing
    response = input("⚠️  This will create new files with 'noaudio_' prefix. Continue? (yes/no): ")
    if response.lower() != "yes":
        print("❌ Operation cancelled by user")
        sys.exit(0)
    
    print()
    
    # Process directory
    try:
        process_directory(directory)
        print("✅ Done!")
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
