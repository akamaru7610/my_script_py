import os
import sys
from pathlib import Path

APP_HOME = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".." ))

class MyBatchConf(object):

    target_excel = os.path.join(APP_HOME, "tmp", "60_外部インターフェイスレイアウト定義書_v0.66.xlsx")
    out_json_dir = os.path.join(APP_HOME, "out_json")

    """
      Excelのコア情報
    """
    no_chk_sheet = ['表紙', '改版履歴', '定義書一覧']
    number_col   = 1
    name_col     = 3
    digit_col    = 37
    content_row  = 8
