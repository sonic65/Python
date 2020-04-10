#导入xml的包
import xml.dom.minidom
#打开xml文件
xml_file=xml.dom.minidom.parse('.\data\myxml.xml')

#获得文档元素对象
print("以下为文档根元素的信息")
root=xml_file.documentElement
print(root.nodeName)
print(root.nodeType)

print("获取任意标签名")
tags=root.getElementsByTagName("city")
print(tags[4].tagName)
tags=root.getElementsByTagName("town")
print(tags[2].tagName)
tags=root.getElementsByTagName("love")
print(tags[0].tagName)


print("获取标签的属性值")
#获得一组city的标签
citys=root.getElementsByTagName("city")
#获取第4个城市的name、weather属性值
city_name=citys[3].getAttribute("name")
city_weather=citys[3].getAttribute("weather")
print(city_name,city_weather)


print("获取第标签之间的数据")
towns=root.getElementsByTagName("town")
towm_name=towns[9].firstChild.data
print(towm_name)