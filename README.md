# Typora Image Uploader (Cloudflare / Telegram)

[English](README.md) | [中文](README_zh.md)

A custom image upload command for [Typora](https://typora.io/), uploading images to a Cloudflare Image Bed (via Telegram channel).

## Features

- Supports Windows, macOS, and Linux.
- Uploads images to your specified Cloudflare/Telegram image host.
- Automatically replaces local image paths with remote URLs in Typora.

## Usage

### Method 1: Using Pre-built Binary (Recommended)

No Python installation required.

1.  **Download**: Go to the [Releases](../../releases) page and download the executable for your OS:
    - Windows: `typora-upload-win.exe`
    - macOS: `typora-upload-mac`
    - Linux: `typora-upload-linux`

2.  **Configuration**:
    Create a `config.json` file in the **same directory** as the downloaded executable.
    
    *Example `config.json`:*
    ```json
    {
        "api_url": "https://cfpic.890214.net/upload",
        "base_url": "https://cfpic.890214.net",
        "auth_code": "YOUR_AUTH_CODE",
        "upload_channel": "telegram"
    }
    ```

3.  **Typora Settings**:
    - Open Typora -> **Preferences** -> **Image**.
    - **When Insert**: Choose "Upload Image".
    - **Image Upload Setting**: Choose "Custom Command".
    - **Command**: Enter the absolute path to your downloaded executable.
      - Example (Windows): `C:\Users\You\Tools\typora-upload-win.exe`
      - Example (Mac/Linux): `/usr/local/bin/typora-upload-mac` (Make sure to `chmod +x` it first)

4.  **Test**: Click "Test Uploader" in Typora to verify.

### Method 2: Running from Source (Python)

1.  **Prerequisites**: Install Python 3.x.

2.  **Install Dependencies**:
    ```bash
    pip install -r typora_upload/requirements.txt
    ```

3.  **Configuration**:
    Edit `typora_upload/config.json` (rename `config.sample.json` if needed) with your settings.

4.  **Typora Settings**:
    - **Command**: 
      ```bash
      python /path/to/typora_imgupload_telegram/typora_upload/upload.py
      ```

## Configuration Reference

| Key | Description | Default / Example |
| :--- | :--- | :--- |
| `api_url` | The upload API endpoint | `https://cfpic.890214.net/upload` |
| `base_url` | The domain for the returned URL | `https://cfpic.890214.net` |
| `auth_code` | Your authentication code | `imgbed_...` |
| `upload_channel` | Upload channel strategy | `telegram` |

## License

MIT
