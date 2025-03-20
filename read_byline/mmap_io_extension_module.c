#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

static PyObject* mmap_io(PyObject* self, PyObject* args) {
    const char* filename;
    int fd;
    struct stat file_stat;
    char* mapped;
    PyObject* result = NULL;

    if (!PyArg_ParseTuple(args, "s", &filename)) {
        return NULL;
    }

    // Open the file
    fd = open(filename, O_RDONLY);
    if (fd == -1) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    // Get file size
    if (fstat(fd, &file_stat) == -1) {
        close(fd);
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    // Memory-map the file
    mapped = mmap(NULL, file_stat.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
    if (mapped == MAP_FAILED) {
        close(fd);
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    // Find the first newline character
    char* newline = memchr(mapped, '\n', file_stat.st_size);
    Py_ssize_t line_length = (newline != NULL) ? (newline - mapped + 1) : file_stat.st_size;

    // Create a Python string
    result = Py_BuildValue("s#", mapped, line_length);

    // Cleanup
    munmap(mapped, file_stat.st_size);
    close(fd);

    return result;
}

// Method definition table
static PyMethodDef MmapMethods[] = {
    {"mmap_io_extension", mmap_io, METH_VARARGS, "Read the first line of a file using mmap."},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef mmapmodule = {
    PyModuleDef_HEAD_INIT,
    "mmap_io_extension_module",
    NULL,
    -1,
    MmapMethods
};

// Module initialization function
PyMODINIT_FUNC PyInit_mmap_io_extension_module(void) {
    return PyModule_Create(&mmapmodule);
}