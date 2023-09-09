# sd-webui-output-path-helper
这是一个针对Stable Diffusion web UI开发的一个生成图片路径控制插件，能让你生成的图片被自动放到你自定义命名的文件夹里

## 功能说明
平时我们生成的图片会统一放到指定的输出目录下，长此以往，每次做的图片都是不同的，但都被放在了一起，不好管理
该插件能对每次生成的图进行指定目录的控制，随时都能创建新的分组，让图片立即保存到新的目录或历史目录中
比如：
现在做风景的图，等下又要做汽车的图，然后又要做建筑的图，这时候我们就可以在做不同项目之前，先设定好项目名称，这样一来每次生成的图片就会被放进指定的文件夹内

## 功能记录
2023.9.9
1. 历史记录功能
2. 支持t2i
3. 支持i2i
4. 支持webUI 1.6版本

## 效果展示
1. 界面窗口
<img alt="Screenshot" src="https://github.com/design61/sd-webui-output-path-helper/blob/main/image/1.png">

2. 效果预览
<img alt="Screenshot" src="https://github.com/design61/sd-webui-output-path-helper/blob/main/image/2.png">

## 安装方法
1. 打开 `扩展` 选项卡. 
2. 打开 `从网址安装` 选项卡.
3. 在 `扩展的 git 仓库网址` 输入 `https://github.com/design61/sd-webui-output-path-helper.git`.
4. 点击 `安装` 按钮.
5. 等待安装，直到出现 `Use Installed tab to restart` 的提示.
6. 重启你的 web UI.

## Installation
1. Open `Extensions` tab.
2. Open `Install from URL` tab in the tab.
3. Enter `https://github.com/design61/sd-webui-output-path-helper.git` to `URL for extension's git repository`.
4. Press `Install` button.
5. Wait for 5 seconds, and you will see the message `Use Installed tab to restart`.
6. Go to the `Installed` tab, and then click `Apply and restart UI`.
