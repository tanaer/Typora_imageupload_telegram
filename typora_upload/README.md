# Typora 图片上传脚本 (Cloudflare Image Bed)

这是一个为 Typora 编写的自定义图片上传脚本，用于将图片上传到 `https://cfpic.890214.net`。

## 安装与配置

1.  **安装 Python 依赖**
    
    确保已安装 Python 3。在当前目录下运行：
    ```bash
    pip install -r requirements.txt
    ```

2.  **配置 Auth Code**

    打开 `config.json` 文件，填入你的上传认证码 (`authCode`)：
    ```json
    {
        "api_url": "https://cfpic.890214.net/upload",
        "base_url": "https://cfpic.890214.net",
        "auth_code": "这里填入你的认证码", 
        "upload_channel": "telegram"
    }
    ```

## 在 Typora 中设置

1.  打开 Typora -> **偏好设置** -> **图像**。
2.  **插入图片时** 选择 "上传图片"。
3.  **上传服务** 选择 "Custom Command" (自定义命令)。
4.  **命令** 中填入：
    ```bash
    python "c:\Users\Administrator\Documents\trae_projects\typora_imgupload_telegram\typora_upload\upload.py"
    ```
    *(请确保使用 `upload.py` 的绝对路径，如果 python 不在系统环境变量中，也请使用 python 的绝对路径)*

5.  点击 "验证图片上传选项" 进行测试。

## 注意事项

*   脚本会将上传成功的图片 URL 输出到标准输出。
*   如果上传失败，Typora 会显示错误信息。
*   默认使用 `telegram` 渠道，可在 `config.json` 中修改。
