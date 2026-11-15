"""
这一部分用来定义自定义异常类
"""


class InterruptAgentFlow(Exception):
    """这个异常表示代理流程被中断"""

    def __init__(self, *messages: dict) -> None:
        self.messages = messages
        super().__init__()


class Submitted(InterruptAgentFlow):
    """这个异常表示任务完成，需要提交任务"""


class LimitsExceeded(InterruptAgentFlow):
    """这个异常表示步数或成本超出预算"""


class TimeExceeded(LimitsExceeded):
    """这个异常表示墙上时间超出预算"""


class UserInterruption(InterruptAgentFlow):
    """这个异常表示用户中断"""


class FormatError(InterruptAgentFlow):
    """这个异常表示LM输出格式错误"""
