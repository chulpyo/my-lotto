""" My Lotto 프로젝트 설정 파일

Changes
-------
2022-03-29
    - 최초 작성

"""
import os

from typing import Any, Optional, Dict, List, Tuple, TypeVar
from urllib.parse import quote

from pydantic import (
    BaseSettings
)
from dotenv import load_dotenv

# ENV FILE 로드
FILE_DIR = os.path.abspath(os.path.dirname(__file__))
ENV_DIR = os.path.join(FILE_DIR, 'env')
ENV_FILE = os.path.join(ENV_DIR, '.env')

if not os.path.exists(ENV_DIR):
    os.mkdir(ENV_DIR)

if not os.path.exists(ENV_FILE):
    open(ENV_FILE, 'w')

load_dotenv(ENV_FILE)

# 주요 경로 상수
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            FILE_DIR
        )
    )
)

SRC_DIR = os.path.join(BASE_DIR, 'src')
APP_DIR = os.path.join(SRC_DIR, 'app')

class Settings(BaseSettings):
    """ 프로젝트 기본 세팅 저장 클래스 """
    # DB
    DB_CONNECTOR: str = ''
    DB_USER: str = ''
    DB_PWD: str = ''
    DB_HOST: str = ''
    DB_PORT: int = -1
    DB_DATABASE: str = ''
    DB_URI_TEMPLATE: str = '{connector}://{user}:{pwd}@{host}:{port}/{db}'

    def get_db_uri(self) -> str:
        """
        대상 db 이름을 입력받아 db 연결을 위한 URI 반환
        
        Returns
        -------
        : str
            대상 DB URI
    
        """

        return self.DB_URI_TEMPLATE.format(
            connector=self.DB_CONNECTOR
            , user=self.DB_USER
            , pwd=quote(self.DB_PWD)
            , host=self.DB_HOST
            , port=self.DB_PORT
            , db=self.DB_DATABASE
        )

    class Config:
        """ 기본 세팅 메타 클래스 """
        env_prefix = ''
        case_sentive = False
        # env_prefix = 'MYLT_'
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
