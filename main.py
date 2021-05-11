from multiprocessing import Process, Pool
from process import get_folders
from process import get_drives
from service import add_folders
import functools
import operator


result_list = []


def get_all_folders():
    def log_result(result):
        # This is called whenever foo_pool(i) returns a result.
        # result_list is modified only by the main process, not the pool workers.
        result_list.append(result)

    pool = Pool()
    multiple_results = [pool.apply_async(func=get_folders, args=(drive,)) for drive
                        in get_drives()]

    pool.close()
    pool.join()

    return functools.reduce(operator.iconcat, map(lambda result: result.get(), multiple_results), [])


if __name__ == '__main__':
    folders = get_all_folders()

    add_folders(folders)

    folder_image_metada()


