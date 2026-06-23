# brain.py

import os
from openai import OpenAI

DEEPSEEK_API_KEY = "sk-1c670a82e057430c84630ae5242355d1"  # 这里设置你申请的 key 这是我充值了一块钱的账户，用完就删key
DEEPSEEK_API_URL = "https://api.deepseek.com/v1"

client = OpenAI(
    api_key = DEEPSEEK_API_KEY,
    base_url = DEEPSEEK_API_URL)

class AgentBrain:
    """Agent 的大脑，负责思考与决策"""
    
    def __init__(self, model="deepseek-v4-flash"):
        self.model = model
    
    def think(self, prompt):
        """核心思考函数：接收提示，返回模型的思考结果"""
        try:
            # 使用客户端调用 Chat Completions API（v1.x 版本写法）
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,  # 控制创造性，越低越专注
                max_tokens=500    # 控制回复长度
            )
            # 提取模型返回的文本内容（v1.x 版本属性路径变更）
            reasoning = response.choices[0].message.content
            return reasoning.strip()
        except Exception as e:
            return f"思考过程出错: {e}"

# 简单测试一下大脑是否工作
if __name__ == "__main__":
    brain = AgentBrain()
    test_prompt = "读取这个文件所在地址"
    print("测试提问：", test_prompt)
    print("大脑回复：", brain.think(test_prompt))