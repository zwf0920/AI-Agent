# tools.py
import datetime
import os

class AgentTools:
    """Agent 可以使用的工具集合"""
    #读取文件工具
    @staticmethod
    def read_text(file_name):
        """读取文件工具"""
        with open(file_name, 'r') as f:
            content = f.read()
        return f"[文件内容] 是：{content}"
    
    #读取目录工具
    @staticmethod
    def read_catalog(catalog_name):
        """读取目录工具"""
        file_names = os.listdir(catalog_name)
        return f"[{catalog_name}下内容] 是：{file_names}"
    
    #找出工具 能找出所有关键词在文件中出现的位置
    @staticmethod
    def query(file_name,keyword):
        """找出工具"""
        positions=[]
        total_offset = 0
        with open(file_name, 'r') as f:
            content = f.read()
        start = 0  # 起始位置
        while True:
            start = content.find(keyword, start)  # 查找关键字的起始位置
            if start == -1:  # 如果找不到，结束循环
                break
            positions.append(start + total_offset)  # 记录位置，包括之前的换行符等影响
            start += len(keyword)  # 移动起始位置，以便继续查找下一个实例
            total_offset += content.count('\n', 0, start)  # 更新总偏移量，考虑换行符的影响
        return f"[{keyword}位置] 是：{positions}"
    
    @staticmethod
    def search_web(query):
        """模拟网络搜索工具（此处为模拟）"""
        mock_results = {
            "旅行目的地推荐": "巴黎、东京、马尔代夫、云南丽江...",
            "北京天气": "明天晴，气温 15-25°C，微风。",
            "Python 教程": "推荐菜鸟教程等网站。"
        }
        for key, value in mock_results.items():
            if key in query:
                return f"[网络搜索] 关于 '{query}' 的结果：{value}"
        return f"[网络搜索] 未找到 '{query}' 的明确信息。"
    
    @staticmethod
    def make_schedule(steps):
        """制定日程计划工具"""
        schedule = "生成的日程计划：\n"
        for i, step in enumerate(steps, 1):
            schedule += f"{i}. {step}\n"
        return schedule
    
    @staticmethod
    def get_current_time():
        """获取当前时间工具"""
        now = datetime.datetime.now()
        return f"[系统时间] 现在是：{now.strftime('%Y-%m-%d %H:%M:%S')}"
    
    @staticmethod
    def calculate(expression):
        """简单计算器工具（安全版本，修复兼容性问题）"""
        try:
            # 1. 严格过滤非法字符（仅允许数字、基础运算符、括号、空格）
            allowed_chars = set("0123456789+-*/(). ")
            if not all(c in allowed_chars for c in expression):
                return "[计算器] 表达式包含非法字符，拒绝计算。"
            
            # 2. 简化安全校验：移除易出错的 ast.walk 逻辑，改用基础语法检查
            # 先替换空格，避免空表达式
            clean_expr = expression.strip().replace(" ", "")
            if not clean_expr:
                return "[计算器] 表达式不能为空。"
            
            # 3. 安全执行计算（限制内置函数，仅保留基础运算）
            # 自定义安全的全局环境，仅允许基础数学运算
            safe_globals = {
                '__builtins__': {},
                'pow': pow,
                'abs': abs
            }
            # 使用 eval 但严格限制环境，且已过滤非法字符，大幅降低风险
            result = eval(clean_expr, safe_globals)
            return f"[计算器] {expression} = {result}"
        
        except ZeroDivisionError:
            return "[计算器] 错误：除数不能为零。"
        except SyntaxError:
            return "[计算器] 表达式语法错误（如括号不匹配、运算符错误）。"
        except Exception as e:
            return f"[计算器] 计算错误: {str(e)}"

# 测试工具
if __name__ == "__main__":
   # print(AgentTools.read_text("test.py"))
   # print(AgentTools.query("test.py","es"))
   print(AgentTools.read_catalog("test1"))
   # print(AgentTools.get_current_time())
   # print(AgentTools.calculate("3 + 5 * 2"))       # 正常计算
   # print(AgentTools.calculate("10 / 0"))          # 除零错误
   # print(AgentTools.calculate("__import__('os').system('ls')"))  # 非法字符过滤