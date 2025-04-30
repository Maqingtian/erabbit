project_name/
│
├── tests/                     # 测试用例目录
│   ├── __init__.py
│   ├── test_login.py           # 登录接口测试
│   ├── test_goods.py           # 查看商品接口测试
│   ├── test_cart.py            # 加入购物车接口测试
│   ├── test_order.py           # 订单相关接口测试
│   └── test_address.py         # 添加地址接口测试
│
├── pages/                      # Page Object 模式页面对象目录
│   ├── __init__.py
│   ├── login_page.py           # 登录接口页面对象
│   ├── goods_page.py           # 查看商品接口页面对象
│   ├── cart_page.py            # 加入购物车接口页面对象
│   ├── order_page.py           # 订单相关接口页面对象
│   └── address_page.py         # 添加地址接口页面对象
│
├── utils/                      # 工具类目录
│   ├── __init__.py
│   ├── requests_util.py        # 封装 Requests 请求工具类
│   └── common_util.py          # 其他通用工具类
│
├── data/                       # 测试数据目录
│   ├── login_data.json         # 登录接口测试数据
│   ├── goods_data.json         # 查看商品接口测试数据
│   ├── cart_data.json          # 加入购物车接口测试数据
│   ├── order_data.json         # 订单相关接口测试数据
│   └── address_data.json       # 添加地址接口测试数据
│
├── conftest.py                 # Pytest 配置文件
├── pytest.ini                  # Pytest 配置文件
└── README.md