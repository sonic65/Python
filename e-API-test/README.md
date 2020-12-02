# Python Pytest 接口自动化

通过读取Excel行列，将字段拼装成请求体。
判断响应字段，对比Excel中的期待结果，再将最终结果写入Excel。

通过Allure生产测试报告


# 执行参数
pytest

# 生成报告
allure generate report/result -o report/allure_html --clean

# 打开报告
allure open report/allure_html