import concurrent.futures
import mmap

BATCH_SIZE = 2621440

def process_chunk(chunk):
    return chunk.decode('utf-8').replace("0", "o")

def mmap_io_batch_parallel(filename, batch_size=BATCH_SIZE):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            file_size = mmap_obj.size()
            offsets = range(0, file_size, batch_size)
            # Use a ThreadPoolExecutor to process chunks concurrently.
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                # executor.map preserves the order of the inputs.
                results = executor.map(lambda offset: process_chunk(mmap_obj[offset:offset + batch_size]), offsets)
                yield results