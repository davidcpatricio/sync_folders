import logging
import time

from dirsync import sync

while True:
    def synchronize_folders(
            source_folder, replica_folder, log_path, time_interval=5
    ):
        logging.basicConfig(filename=log_path,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='w',
                            encoding='utf-8')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        sync(source_folder, replica_folder, 'sync', purge=True)

        time.sleep(time_interval)

    synchronize_folders(
        '.\\folder_a',
        '.\\folder_b',
        '.\\log.txt',
        10
    )
