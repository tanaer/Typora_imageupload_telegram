# Typora 图片上传工具 (Cloudflare / Telegram)

[English](README.md) | [中文](README_zh.md)

为 [Typora](https://typora.io/) 开发的自定义图片上传命令，将图片上传到 Cloudflare 图床（通过 Telegram 频道）。

## 功能特性

- 支持 Windows, macOS 和 Linux。
- 上传图片到你指定的 Cloudflare/Telegram 图床。
- 自动将 Typora 中的本地图片路径替换为远程 URL。

## 使用指南

### 方法 1：使用预编译二进制文件（推荐）

无需安装 Python。

1.  **下载**：前往 [Releases](../../releases) 页面下载对应系统的可执行文件：
    - Windows: `typora-upload-win.exe`
    - macOS: `typora-upload-mac`
    - Linux: `typora-upload-linux`

2.  **配置**：
    在下载的可执行文件**同一目录**下创建一个 `config.json` 文件。
    
    *config.json 示例：*
    ```json
    {
        "api_url": "https://xxx.com/upload",
        "base_url": "https://xxx.com",
        "auth_code": "YOUR_AUTH_CODE",
        "upload_channel": "telegram"
    }
    ```

3.  **Typora 设置**：
    - 打开 Typora -> **偏好设置** -> **图像**。
    - **插入图片时**：选择“上传图片”。
    - **上传服务**：选择“自定义命令” (Custom Command)。
    - **命令**：输入下载的可执行文件的绝对路径。
      - 示例 (Windows): `C:\Users\You\Tools\typora-upload-win.exe`
      - 示例 (Mac/Linux): `/usr/local/bin/typora-upload-mac` (请先执行 `chmod +x` 赋予执行权限)

4.  **测试**：点击 Typora 中的“验证图片上传选项”进行测试。

### 方法 2：源码运行 (Python)

1.  **前置条件**：安装 Python 3.x。

2.  **安装依赖**：
    ```bash
    pip install -r typora_upload/requirements.txt
    ```

3.  **配置**：
    编辑 `typora_upload/config.json`（如有需要重命名 `config.sample.json`）填入你的配置。

4.  **Typora 设置**：
    - **命令**： 
      ```bash
      python /path/to/typora_imgupload_telegram/typora_upload/upload.py
      ```

## 配置项说明

| 键名 | 描述 | 默认值 / 示例 |
| :--- | :--- | :--- |
| `api_url` | 上传 API 接口地址 | `https://cfpic.890214.net/upload` |
| `base_url` | 返回 URL 的域名 | `https://cfpic.890214.net` |
| `auth_code` | 你的认证代码 | `imgbed_...` |
| `upload_channel` | 上传渠道策略 | `telegram` |

## 许可证

MIT
