import os
import sys
from pathlib import Path
import json
import unicodedata

APP_HOME = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".." ))
sys.path.append(APP_HOME)
PROG_NAME = os.path.splitext(os.path.basename(__file__))[0]

from lib.my_logger import MyLogger
# from conf.my_batch_conf import MyBatchConf

MY_LOGGER = MyLogger.get_my_logger(APP_HOME, PROG_NAME)

def cmd(target_file, settting_json):
    """
    """
    try:
        MY_LOGGER.info("start")

        with open(target_file, mode='r', encoding='sjis') as f:
            target_line = f.readlines()[0]

        with open(settting_json, 'r', encoding='utf-8') as json_open:
            settting_items = json.load(json_open)

        chk_item = int(settting_items['sum_digit'])
        is_def_ok = chk_def(target_line, chk_item)

        out_ret_json(target_file+".json", target_line, chk_item, is_def_ok)

    except Exception as e:
        MY_LOGGER.info("Failure!! file:{}".format(target_file))
        MY_LOGGER.exception(e)
        sys.exit(1)
    else:
        MY_LOGGER.info("Success!! file:{}".format(target_file))
        MY_LOGGER.info("end")

def chk_def(target_line, chk_item):
    # Todo: ファイル形式でチェックを変えたい
    return get_east_asian_width_count(target_line) == chk_item

def out_ret_json(file_path, target_line, chk_item, is_def_ok):
    data = dict()
    data['line']     = target_line
    data['line_len'] = get_east_asian_width_count(target_line)
    data['chk_item'] = chk_item
    data['chk']      = is_def_ok
    with open(file_path, mode='wt', encoding='sjis') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

def is_dat():
    return

def is_csv():
    return

if __name__ == "__main__":
    # Todo: clickを導入したい
    args = sys.argv
    cmd(args[1], args[2])
