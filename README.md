# 爬1000个网站
## Tools
 -  工具类
    - compute.py 根据字符集和每行最大字数计算合适的画布大小和字体宽高度
## lol_heroskin.py  
- 内容：英雄联盟英雄皮肤批量下载(普通版/多线程版)
## CaiGou 
 -  内容：[中国供应商网站爬取](https://www.china.cn/buy/purchase/1.html)
 -  涉及知识点：
    - css内嵌字体集处理，该网站采用base64加密内嵌方式
    - PIL绘图
    - 调用百度AIOcr识别图片，转换文字(自行网上搜索用法)
 -  涉及文件：
    - caigou.py 爬虫代码文件
    - Tools/compute.py 工具类
    
## TouTiao
 -  内容：头条解密及热榜爬取
 -  jinritoutiao.py 热榜爬取代码
 -  as_cp.js/touTiaoSign.js 解密js
 -  toutiao_decode.py 执行js文件代码
 -  toutiaonews.py 新闻爬取代码(由于头条缓存机制，每次获取数据变化不大，建议定时爬取每日更新内容，待补充)
