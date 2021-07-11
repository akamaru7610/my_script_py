import os
import sys
from pathlib import Path

APP_HOME = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".." ))
sys.path.append(APP_HOME)
PROG_NAME = os.path.splitext(os.path.basename(__file__))[0]

from lib.my_logger import MyLogger
# from conf.my_batch_conf import MyBatchConf

MY_LOGGER = MyLogger.get_my_logger(APP_HOME, PROG_NAME)

def cmd(target_file, idfs):
    """
      引数の識別子単位にファイルを分割します。
    """
    try:
        MY_LOGGER.info("start")

        with open(target_file, mode='r') as f:
            all_lines = f.readlines()

        MY_LOGGER.info(idfs)
        for idf in idfs:
            MY_LOGGER.info("idf:{}".format(idf))

            idf_lines = get_target_idf_lines(all_lines, idf)
            out_path = target_file + "_{}.dat".format(idf)
            MY_LOGGER.info("out_path:{}".format(out_path))
            out_idf_file(out_path, idf_lines)

    except Exception as e:
        MY_LOGGER.info("Failure!! file:{}".format(target_file))
        MY_LOGGER.exception(e)
        sys.exit(1)
    else:
        MY_LOGGER.info("Success!! file:{}".format(target_file))
        MY_LOGGER.info("end")

def get_target_idf_lines(all_lines, idf):
    """
     識別子の行をリストで取得します。
    """
    return [line for line in all_lines if line.startswith(idf)]

def out_idf_file(out_path, data):
    """
     リストをファイル出力します。
    """
    with open(out_path, 'w') as file:
        file.writelines(data)

if __name__ == "__main__":
    """
      ＜実行方法＞
      python .\bin\split_dat_idf.py '.\tmp\S12I00.dat.20210322095842' 'A,B,D'
    """
    args = sys.argv
    cmd(args[1], sys.argv[2].split(','))
