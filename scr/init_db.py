"""Initial database setup script"""

import sys
from pathlib import Path

# Add project root path to sys.path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


# pylint: disable=wrong-import-position
import app.models as load_models
from app.config import settings
from app.database.database import Base, engine

# 설정 로드
_ = settings

# 모든 모델들을 import하여 SQLAlchemy가 테이블을 인식할 수 있도록 함
_ = load_models

# 모든 모델들을 import하여 테이블 생성
print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")
