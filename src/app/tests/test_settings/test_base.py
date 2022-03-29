""" src/app/settings/base.py 테스트 파일

시나리오
--------
test_settings_db_uri_generate
    1. Settings에 저장된 데이터를 바탕으로 원하는 형식의 db uri 생성
    2. 변수를 오버라이딩하여 계정을 root에서 root1로 변경하여 db uri 생성

"""

from settings import base

def test_settings_db_uri_generate() -> None:
    # 시나리오 1
    result = base.settings.get_db_uri()
    assert result == 'mysql+pymysql://root:qwer1234@chulpyo.me:21081/SPOAPI'
    base.settings.DB_USER = 'root1'
    result = base.settings.get_db_uri()
    assert result == 'mysql+pymysql://root1:qwer1234@chulpyo.me:21081/SPOAPI'

