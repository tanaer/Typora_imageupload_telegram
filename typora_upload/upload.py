import sys
import os
import json
import requests

def load_config():
    """Load configuration from config.json in the same directory."""
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
        
    config_path = os.path.join(application_path, 'config.json')
    
    if not os.path.exists(config_path):
        return None # Return None to let caller handle or fail gracefully
        
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def upload_image(file_path, config):
    """Upload a single image and return the remote URL."""
    api_url = config.get('api_url')
    auth_code = config.get('auth_code')
    upload_channel = config.get('upload_channel', 'telegram')
    base_url = config.get('base_url', '')

    if not api_url:
        return "Error: api_url not configured"

    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            params = {
                'uploadChannel': upload_channel
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Authorization': auth_code
            }
            
            # API expects multipart/form-data
            response = requests.post(api_url, files=files, params=params, headers=headers)
            
            if response.status_code != 200:
                return f"Error: Status {response.status_code}, Response: {response.text}"
                
            response.raise_for_status()
            
            # Parse response
            # Expected format: [{"src": "/file/..."}]
            data = response.json()
            
            if isinstance(data, list) and len(data) > 0 and 'src' in data[0]:
                src = data[0]['src']
                # If src is relative, prepend base_url
                if not src.startswith('http'):
                    full_url = f"{base_url.rstrip('/')}{src}"
                else:
                    full_url = src
                return full_url
            else:
                return f"Error: Unexpected response format: {data}"

    except Exception as e:
        return f"Error uploading {os.path.basename(file_path)}: {str(e)}"

def main():
    # Typora passes image paths as command line arguments
    image_paths = sys.argv[1:]
    
    if not image_paths:
        print("Error: No image paths provided.")
        return

    config = load_config()
    if config is None:
        print("Error: config.json not found.")
        print("Please ensure config.json is in the same directory as the script/executable.")
        return
    
    # Print header (optional but good for debugging)
    print("Upload Success:")
    
    for image_path in image_paths:
        if os.path.exists(image_path):
            url = upload_image(image_path, config)
            print(url)
        else:
            print(f"Error: File not found: {image_path}")

if __name__ == "__main__":
    main()
