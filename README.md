# pytest-learning-lab

一个用于系统学习 **Python 测试框架（pytest）** 的实践项目：按照主流招聘要求中出现的测试技术栈，从单元测试一路做到接口测试、UI 自动化、测试报告与 CI。

目标不是写很多用例，而是**把一层层测试能力真正跑通**：分层目录、fixture、参数化、标记、报告、持续集成。

---

## 目录结构

```
pytest-learning-lab/
├── pytest.ini                  # pytest 配置：testpaths / pythonpath / marker 注册
├── requirements.txt            # 核心依赖
├── conftest.py                 # 根 conftest：pytest_runtest_makereport 钩子（为 UI 失败截图服务）
├── config.py                   # 从环境变量读取配置（API_KEY）
├── api_client.py               # requests.Session 封装的接口客户端
├── app.py                      # 极简 ASGI 应用（作为被请求对象）
├── etl.py                      # 样例 ETL 数据（用于数据校验类测试）
├── locustfile.py               # 性能测试脚本（学习用）
└── tests/
    ├── conftest.py             # rows fixture
    ├── unit/                   # 单元测试（不碰网络）
    │   ├── test_demo.py          # 基础断言、tmp_path、capsys
    │   ├── test_config.py        # monkeypatch 修改环境变量
    │   ├── test_etl.py           # 数据校验：amount == price * qty
    │   ├── test_fixture2.py      # fixture 依赖链 + autouse
    │   └── test_param_fixture.py # fixture 参数化
    ├── api/                    # 接口测试
    │   ├── conftest.py           # session 级 api fixture
    │   ├── test_api.py           # 状态码、响应耗时断言
    │   ├── test_client.py        # ApiClient 封装测试
    │   └── test_mock.py          # monkeypatch 打桩
    └── ui/                     # UI 自动化
        ├── conftest.py           # Playwright / Selenium 双驱动 fixture + 失败自动截图
        ├── test_ui.py            # Playwright 驱动
        └── test_ui_selenium.py   # Selenium 驱动
```

---

## 技术栈

| 分类 | 使用 |
|---|---|
| 语言 | Python 3.11 |
| 测试框架 | pytest、pytest-cov |
| 接口测试 | requests |
| UI 自动化 | Playwright（Chromium）、Selenium |
| 报告 | allure-pytest（含失败自动截图） |
| 性能测试 | locust |
| 持续集成 | GitHub Actions |

---

## 环境准备

```bash
pip install -r requirements.txt
```

UI 测试需要额外安装浏览器驱动（**故意不放进 `requirements.txt`**，避免 CI 每次都下载浏览器）：

```bash
pip install playwright selenium
playwright install chromium
```

---

## 运行方式

项目用 **marker 把测试分层**，可以按需只跑一层：

```bash
pytest -m unit        # 只跑单元测试：不碰网络、不需要浏览器，最快
pytest -m api         # 只跑接口测试：需要外网
pytest -m ui          # 只跑 UI 测试：需要本机 Chrome + playwright
pytest                # 全部跑
```

生成测试报告：

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

生成覆盖率报告：

```bash
pytest --cov=. --cov-report=html
```

---

## 覆盖的知识点

**基础**
- 用例发现规则（`test_*.py`、`test_*` 函数）
- `assert` 断言、`pytest.raises` 异常断言
- 测试失败时的详细输出

**fixture**
- `scope`：function / module / session 不同生命周期
- `autouse=True` 自动生效的 fixture
- fixture 之间的依赖链（小 fixture 拼出大 fixture）
- `yield` fixture 做资源清理
- **参数化 fixture**（`params` + `request.param`）
- 内置 fixture：`tmp_path`、`capsys`、`monkeypatch`、`request`

**组织与配置**
- `conftest.py` 的分层与作用域（根 / tests / 各层各一份）
- `pytest.ini` 配置：`testpaths`、`pythonpath`、`addopts`
- 自定义 marker 与分组执行（unit / api / ui）

**进阶**
- `@pytest.mark.parametrize` 参数化
- pytest hook：`pytest_runtest_makereport` 拿到用例执行结果
- UI 用例失败时**自动截图**并附加到 Allure 报告
- 插件：allure-pytest、pytest-cov

**工程化**
- 依赖与配置外置（环境变量、`requirements.txt`）
- `.gitignore` 管理生成物（缓存、报告、截图）
- GitHub Actions 自动跑测试

---

## 持续集成

`.github/workflows/test.yml` 在每次 push 时自动执行：

```bash
pip install -r requirements.txt
pytest tests/unit tests/api
```

说明：**CI 只跑 unit + api，不跑 ui** —— 避免在流水线里反复下载浏览器。UI 测试在本地执行。

> ⚠️ 已知局限：`tests/api` 直接请求外网 `httpbin.org`，网络抖动时 CI 会不稳定。后续计划改成本地桩服务，让测试与外部网络解耦。

---

## 学习路线（本仓库的推进顺序）

| 步骤 | 内容 |
|---|---|
| 1 | 环境准备 + 第一个测试 |
| 2 | `assert` 与用例发现规则 |
| 3 | fixture |
| 4 | 参数化 `parametrize` |
| 5 | 标记与 `skip` / `xfail` |
| 6 | 配置文件 `pytest.ini` |
| 7 | 常用插件（覆盖率 / 报告） |
| 8 | 实战：接口测试、ETL 数据校验 |

---

## 后续计划

- [ ] 把 `tests/api` 的外网依赖改成本地桩服务，消除 CI 的不稳定
- [ ] 把 UI 层纳入 CI（或单独一条 workflow）
- [ ] 补充性能测试场景（压测脚本 + 结果报告）
- [ ] 补充 `LICENSE`

---

作者：陈军 · 系统测试工程师 / SDET
