# Python 学习路线（专为前端开发者设计）

> 作为一名前端开发者，你已经掌握了 JavaScript、TypeScript 和 Node.js，这会让学习 Python 更加容易。本课程将帮助你快速掌握 Python，并通过对比 JavaScript 和 Python 的异同来加深理解。

## 📊 当前学习进度

**总体进度**：14% (3/21 课完成)
**当前阶段**：第一阶段 - 基础语法 (43% 完成)
**最后更新**：2026-05-01

### ✅ 已完成的课程
- 第1课：变量与数据类型 ⭐⭐⭐⭐⭐
- 第2课：数据结构 ⭐⭐⭐⭐⭐
- 第3课：控制流 ⭐⭐⭐⭐ (进行中)

### 🎯 正在学习
- 第3课：控制流（完善练习）
- 准备进入第4课：函数

---

## 课程大纲

### 第一阶段：基础语法（1-2周）

#### 1. 变量与数据类型 ✅
- [x] Python 变量声明（无需 `let/const`）
- [x] 基本数据类型：int, float, str, bool
- [x] None vs JavaScript 的 null/undefined
- [x] 类型转换：`int()`, `str()`, `float()`
- [x] **对比 JS**：动态类型 vs 静态类型检查的差异

#### 2. 数据结构 ✅
- [x] List（类似 JS 数组）
- [x] Tuple（不可变列表）
- [x] Set（类似 JS Set）
- [x] Dictionary（类似 JS Object/Map）
- [x] 列表推导式（JS 暂无直接对应）
- [x] **实践**：用 Python 重写一个 JS 数组操作函数

#### 3. 控制流 🔄
- [x] if/else 语句（注意缩进和 `:`）
- [x] for 循环（遍历列表、字典）
- [x] while 循环
- [x] match/case 语句（Python 3.10+，类似 JS switch）*已了解概念*
- [x] **对比 JS**：代码块用缩进而非花括号

#### 4. 函数
- [ ] 函数定义：`def function_name(params):`
- [ ] 参数类型提示（类似 TypeScript）
- [ ] 默认参数
- [ ] *args 和 **kwargs
- [ ] Lambda 函数
- [ ] **对比 JS**：函数式编程差异

### 第二阶段：面向对象编程（1-2周）

#### 5. 类与对象
- [ ] 类定义和 `__init__` 构造函数
- [ ] `self` 参数（类似 JS 的 `this`）
- [ ] 类属性和实例属性
- [ ] 私有属性（`_variable` 命名约定）
- [ ] **对比 JS**：Python 的类系统 vs ES6 Class

#### 6. 继承与多态
- [ ] 类继承
- [ ] 方法重写
- [ ] 多重继承（Python 特有）
- [ ] 抽象基类（ABC）
- [ ] **实践**：设计一个简单的类继承结构

#### 7. 特殊方法（魔术方法）
- [ ] `__str__` 和 `__repr__`
- [ ] `__eq__`, `__lt__` 等比较方法
- [ ] `__call__`（可调用对象）
- [ ] **对比 JS**：Symbol 和 Proxy

### 第三阶段：进阶特性（2-3周）

#### 8. 异常处理
- [ ] try/except/finally
- [ ] 自定义异常
- [ ] 上下文管理器（`with` 语句）
- [ ] **对比 JS**：try/catch/finally

#### 9. 文件操作与模块
- [ ] 文件读写（`open()`, `with`）
- [ ] JSON 处理（`json` 模块）
- [ ] 导入模块（`import`）
- [ ] 创建自定义模块
- [ ] `__name__ == "__main__"`
- [ ] **对比 JS**：ES Modules vs Python imports

#### 10. 装饰器
- [ ] 函数装饰器
- [ ] 类装饰器
- [ ] 常用内置装饰器（@property, @staticmethod）
- [ ] **对比 JS**：装饰器模式 vs 高阶函数

#### 11. 生成器与迭代器
- [ ] 生成器函数（`yield`）
- [ ] 生成器表达式
- [ ] 迭代器协议
- [ ] **对比 JS**：Generator 函数

### 第四阶段：异步编程（1-2周）

#### 12. 异步基础
- [ ] asyncio 基础
- [ ] async/await 语法
- [ ] 事件循环
- [ ] 并发与并行
- [ ] **对比 JS**：Promise, async/await 在两种语言中的异同

#### 13. 实战项目
- [ ] 异步 HTTP 请求（aiohttp）
- [ ] 并发任务处理
- [ ] **实践**：用 Python 重写一个 Node.js 异步脚本

### 第五阶段：生态系统与工具（2-3周）

#### 14. 包管理
- [ ] pip 使用
- [ ] virtualenv/venv 虚拟环境
- [ ] requirements.txt
- [ ] Poetry（现代依赖管理）
- [ ] **对比 JS**：npm/yarn/pnpm vs pip/Poetry

#### 15. 常用库与框架
- [ ] Web 开发：FastAPI/Flask（对比 Express/Koa）
- [ ] 数据处理：Pandas（类似 JS 的数据操作库）
- [ ] 测试：pytest（对比 Jest/Vitest）
- [ ] 代码格式化：Black（对比 Prettier）
- [ ] 类型检查：mypy（对比 TypeScript）

#### 16. 最佳实践
- [ ] PEP 8 代码风格
- [ ] Type Hints 类型提示
- [ ] 文档字符串（Docstrings）
- [ ] 单元测试
- [ ] 日志记录（logging 模块）

### 第六阶段：实战项目（2-4周）

#### 17. 项目一：Web API
- [ ] 使用 FastAPI 构建 REST API
- [ ] 数据库集成（SQLite/PostgreSQL）
- [ ] 认证与授权
- [ ] API 文档自动生成
- [ ] **对比 JS**：FastAPI vs Express/Nest.js

#### 18. 项目二：数据处理脚本
- [ ] 数据抓取（requests, BeautifulSoup）
- [ ] 数据清洗与分析（Pandas）
- [ ] 可视化（Matplotlib/Plotly）
- [ ] **对比 JS**：Python 在数据处理领域的优势

#### 19. 项目三：自动化工具
- [ ] 文件系统操作
- [ ] 定时任务（schedule/cron）
- [ ] 邮件发送
- [ ] **对比 JS**：Python 在自动化领域的应用

### 第七阶段：高级主题（按需学习）

#### 20. 性能优化
- [ ] 性能分析工具
- [ ] 内存管理
- [ ] Cython/Numba（性能提升）

#### 21. 部署与运维
- [ ] Docker 容器化
- [ ] 云服务部署（AWS/GCP/Azure）
- [ ] CI/CD 流程

## 学习资源

### 官方文档
- [Python 官方文档](https://docs.python.org/zh-cn/3/)
- [Python Style Guide (PEP 8)](https://peps.python.org/pep-0008/)

### 推荐书籍
- 《Python Crash Course》（Python 快速上手）
- 《Fluent Python》（流畅的 Python）
- 《Effective Python》（编写高质量 Python 代码）

### 在线平台
- [LeetCode Python 题解](https://leetcode.cn/)
- [Real Python](https://realpython.com/)
- [Python Morsels](https://www.pythonmorsels.com/)

### 视频教程
- [Python 官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/)
- [廖雪峰 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

## 学习建议

1. **每天至少编码 1 小时**：保持连续性比长时间突击更有效
2. **对比学习**：将 Python 代码与对应的 JavaScript 代码对比，理解差异
3. **实践为主**：每学完一个概念，立即编写代码实践
4. **阅读源码**：阅读优秀的 Python 开源项目源码
5. **参与社区**：加入 Python 相关的 Discord/Slack 群组或论坛

## 快速参考卡

### Python vs JavaScript 常用语法对比

```python
# Python
def greet(name: str) -> str:
    return f"Hello, {name}!"

class Person:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hi, I'm {self.name}"

# 列表推导式
squares = [x**2 for x in range(10)]

# 字典
person = {"name": "Alice", "age": 30}
```

```javascript
// JavaScript
function greet(name) {
    return `Hello, ${name}!`;
}

class Person {
    constructor(name) {
        this.name = name;
    }

    greet() {
        return `Hi, I'm ${this.name}`;
    }
}

// 数组方法
const squares = Array.from({length: 10}, (_, i) => i ** 2);

// 对象
const person = {name: "Alice", age: 30};
```

## 进度追踪

使用下面的清单追踪你的学习进度：

- [🔄] 第一阶段：基础语法（43% 完成 - 3/7 课）
  - ✅ 第1课：变量与数据类型
  - ✅ 第2课：数据结构
  - 🔄 第3课：控制流（进行中）
  - ⏳ 第4课：函数
  - ⏳ 第5课：异常处理
  - ⏳ 第6课：文件操作与模块
  - ⏳ 第7课：装饰器与生成器
- [ ] 第二阶段：面向对象编程
- [ ] 第三阶段：进阶特性
- [ ] 第四阶段：异步编程
- [ ] 第五阶段：生态系统与工具
- [ ] 第六阶段：实战项目
- [ ] 第七阶段：高级主题

**学习统计**：
- 已完成课时：3/21 (14%)
- 代码练习：15+ 个
- 代码行数：371+ 行
- 学习时长：约2-3小时

---

**最后更新时间**：2026-05-01

**学习动态**：
- 📅 开始日期：2026-05-01
- 💻 已提交代码：3个练习文件
- 📝 学习进度记录：详见 `学习进度.md`
- 🎯 下一步目标：完善第3课练习，开始第4课

**预计完成时间**：根据个人投入时间，大约需要 2-3 个月完成全部课程

祝你学习愉快！🐍
