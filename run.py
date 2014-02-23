#!/usr/bin/env python3
from queue import Queue
from threading import Thread

def get(url, **kwargs):
    from get import get as _get
    return _get(url, cachedir = '/ebs/volume', **kwargs)

catalogs = [
    'http://data.iledefrance.fr',
    'http://opendata.paris.fr.opendatasoft.com',
    'http://tourisme04.opendatasoft.com',
    'http://tourisme62.opendatasoft.com',
    'http://grandnancy.opendatasoft.com',
    'http://bistrotdepays.opendatasoft.com',
    'http://scisf.opendatasoft.com',
    'http://pod.opendatasoft.com',
    'http://dataratp.opendatasoft.com',
    'http://public.opendatasoft.com',
]

def datasets(catalog):
    # Search an OpenDataSoft portal, and add things.
    # I chose OpenDataSoft because they care a lot about metadata.
    return json.loads(get(catalog + '/api/datasets/1.0/search?rows=1000000', load = True))

def worker(queue):
    while not queue.empty():
        url = queue.get()
        get(url, load = False)

def main(threads = 50, catalogs = catalogs):
    queue = Queue()
    for catalog in catalogs[:1]:
        for dataset in datasets(catalog):
            queue.put(portal + '/something/here/' + dataset['datasetid'])
    for i in range(threads):
        Thread(target = worker, args = (queue,)).start()

if __name__ == '__main__':
    main()
