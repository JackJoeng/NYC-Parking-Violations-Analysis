from src.bigdata1.opcvapi import get_client, parse_args, validate_num_pages
from src.bigdata1.elasticsearch import create_and_update_index, convert_dtype
import os
import logging
from requests import get
from time import sleep

DATA_URL = "data.cityofnewyork.us"
DATA_ID = "nc67-uf89"

logging.basicConfig(filename="./logs.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    opts = parse_args()
    client = get_client(DATA_URL, os.environ['APP_TOKEN'])

    page_size = int(opts.get('page_size', 1000))
    num_pages = validate_num_pages(opts, page_size)

    i = 0
    logger.debug("Begin processing of data for "
                 f"page_size: {page_size} and num_pages: {num_pages}")
                 
    while i < num_pages:
        resp = client.get(DATA_ID, limit=page_size, offset=i*page_size)
        logger.debug(f"Processed page {i+1}, limit={page_size} and "
                     f"offset={i*page_size}")

        i += 1
        write_to_file = 'output' in opts
        if write_to_file:
            with open(opts['output'], 'a+') as fh:
                for item in resp:
                    print(str(item))
                    fh.write(f"{str(item)}\n")
        for item in resp:
            convert_dtype(item)
            es = create_and_update_index('bigdata1', 'violations')
            res = es.index(index='bigdata1', doc_type='violations', body=item, id=item['summons_number'])
            print(res['result'])

        print(f"DONE LOADING {i}, SLEEPING...")
        sleep(30)
