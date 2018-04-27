# simple-web-spider
A simple web spider for study

简单爬虫架构：
爬虫调度端->爬虫->获取有价值数据
爬虫包括：（URL管理器、网页下载器、网页解析器）
爬虫调度器负责在URL管理器、网页下载器、网页解析器之间交换数据
URL管理器负责管理待抓取的URL集合和已抓取的URL集合，以防止重复抓取和循环抓取
网页下载器负责下载URL对应的网页并转换为一个字符串
网页解析器负责解析下载的网页，并将其中解析出的URL补充到URL管理器中

开发步骤：
1.确定目标
2.分析目标(url格式、数据格式、网页编码)
2.1.入口页：https://baike.baidu.com/item/Python/407313
2.2.URL格式：
2.2.1.词条页面URL：/item/(词条名)
2.3.数据格式：
2.3.1.标题：<dd class="lemmaWgt-lemmaTitle-title"><h1>***</h1></dd>
2.3.2.简介：<div class="lemma-summary" label-module="lemmaSummary">***</div>
2.4。页面编码：UTF-8