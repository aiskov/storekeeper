import os
from hashlib import sha224


def search_duplicates(target, options=None):
    digests = dict()

    for root, dirs, files in os.walk(target):
        for item in files:
            path = '%s/%s' % (root, item)
            hash_digest = _create_digest(path)

            if hash_digest not in digests:
                digests[hash_digest] = set()

            digests[hash_digest].add(path)

            if 'verbose' in options and options.verbose and len(digests[hash_digest]) > 1:
                print 'Duplicates found by hash: %s' % hash_digest
                for file_path in digests[hash_digest]:
                    print '    %s' % file_path

    return [value for key, value in digests.iteritems() if len(value) > 1]


def _create_digest(target, buffer_size=50000000):
    hash_sum = sha224()

    with open(target) as f:
        while True:
            data = f.read(buffer_size)

            if not data:
                break

            hash_sum.update(data)

    return '[%s]->%s' % (os.path.getsize(target), hash_sum.hexdigest())

