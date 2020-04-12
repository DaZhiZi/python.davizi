from models import Model
from utils import formatted_time

# 继承自 Model 的 Todo 类
class Todo(Model):
    def __init__(self, form):
        self.id = form.get('id', None)
        self.title = form.get('title', '')
        self.user_id = int(form.get('user_id', -1))
        # 还应该增加 时间 等数据
        self.created_time = form.get('created_time', formatted_time())
        self.update_time = form.get('update_time', self.created_time)
