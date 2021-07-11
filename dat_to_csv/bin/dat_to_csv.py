import os
import sys
from pathlib import Path
import json
import csv

APP_HOME = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".." ))
sys.path.append(APP_HOME)
PROG_NAME = os.path.splitext(os.path.basename(__file__))[0]

from lib.my_logger import MyLogger
# from conf.my_batch_conf import MyBatchConf

MY_LOGGER = MyLogger.get_my_logger(APP_HOME, PROG_NAME)

def cmd(target_file, settting_json):
    """
      引数の固定長ファイルをCSV形式に変換します。
    """
    try:
        MY_LOGGER.info("start")

        with open(target_file, mode='r') as f:
            target_file_lines = f.readlines()

        with open(settting_json, 'r', encoding='utf-8') as json_open:
            settting_items = json.load(json_open)

        out_file_arrs = get_out_content_arr(target_file_lines, settting_items)
        out_csv(target_file+'.csv', out_file_arrs)

    except Exception as e:
        MY_LOGGER.info("Failure!! file:{}".format(target_file))
        MY_LOGGER.exception(e)
        sys.exit(1)
    else:
        MY_LOGGER.info("Success!! file:{}".format(target_file))
        MY_LOGGER.info("end")

def get_out_content_arr(target_file_lines, settting_items):
    """
     出力情報をを配列で取得します。
    """
    ret = []
    is_set_name = False
    for l in target_file_lines:
        f_arr = []
        start = end = 0
        for key in settting_items:
            if key == 'name':
                if not is_set_name:
                    name_col = settting_items[key]
                    name_col.append("ngtxt")
                    ret.append(name_col)
                    is_set_name = True
                continue

            end += settting_items[key]
            txt = truncate(l[start:end], settting_items[key])
            f_arr.append(txt)
            start = end

        # 行末の不要項目をセット(通常はないはず)
        f_arr.append(l[start:-1])

        ret.append(f_arr)
    return ret

def out_csv(file_path, data):
    """
     配列をCSV形式で出力します。
    """
    with open(file_path, 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(data)

def truncate(str, num_bytes, encoding='utf-8'):
    """
     指定したバイト数分だけ文字列を切り出します。
    """
    while len(str.encode(encoding)) > num_bytes:
        str = str[:-1]
    return str

if __name__ == "__main__":
    args = sys.argv
    cmd(args[1], args[2])
