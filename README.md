# qingting_fm_downloader
 download qingting_fm audios  
 蜻蜓fm下载

 ## packages
 pyaria2  
 requests  
 
## 注意
下载依赖于aria2，请先安装aria2-rpc

 ## 用法
 - 先用`pip install -r requirements.txt` 安装需要的包
 - 在蜻蜓网页版抓取自己的cookie
 - 如果只下载免费内容可不用cookie
 - 打开专辑网页如  https://www.qingting.fm/channels/402683/  channels后面的这组数字就是专辑id
 - 使用`python3 qingting-fm.py`，然后输入刚才得到的专辑id，即可下载该专辑的全部内容