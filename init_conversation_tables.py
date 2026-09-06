"""
初始化对话历史和Pending Action相关的数据库表
"""
import sys
from pathlib import Path

# 确保能找到 app 模块
sys.path.append(str(Path(__file__).resolve().parent))

from app.db.session import SessionLocal, engine
from app.db.base import Base
from app.models.conversation import ConversationMessage, PendingAction


def create_tables():
    """创建缺失的数据库表"""
    Base.metadata.create_all(bind=engine, tables=[
        ConversationMessage.__table__,
        PendingAction.__table__,
    ])
    print("Successfully created/verified conversation tables.")


if __name__ == "__main__":
    create_tables()
