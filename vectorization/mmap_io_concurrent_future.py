import mmap
from concurrent.futures import ProcessPoolExecutor, as_completed

CHUNK_SIZE = 1024 * 10000

def process_chunk(chunk_bytes):
    """Decode and process a full chunk of text."""
    return chunk_bytes.decode('utf-8').replace("0", "o")

def mmap_chunks(filename, chunk_size):
    with open(filename, mode="rb") as file_obj:
        with mmap.mmap(file_obj.fileno(), 0, access=mmap.ACCESS_READ) as mm:
            start = 0
            end = len(mm)

            while start < end:
                next_chunk_end = min(start + chunk_size, end)
                yield mm[start:next_chunk_end]
                start = next_chunk_end

def mmap_io_concurrent(filename):
    with ProcessPoolExecutor() as executor:
        for chunk in mmap_chunks(filename, CHUNK_SIZE):
            yield executor.submit(process_chunk, chunk)