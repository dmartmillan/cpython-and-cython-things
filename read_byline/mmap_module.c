#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <string.h>

typedef struct {
    PyObject_HEAD
    char* filename;
    int fd;
    struct stat file_stat;
    char* mapped;
    char* current;
} MMapObject;

// Forward declare the generator type object
static PyTypeObject MMapToType;

// Generator's iteration function
static PyObject* readline(MMapObject* self) {
    // Check if we've reached the end of the file
    if (self->current >= self->mapped + self->file_stat.st_size) {
        PyErr_SetNone(PyExc_StopIteration);
        return NULL;
    }

    // Look for the next newline character starting from current position
    size_t remaining = self->mapped + self->file_stat.st_size - self->current;
    char* newline = memchr(self->current, '\n', remaining);

    Py_ssize_t line_length;
    if (newline) {
        line_length = newline - self->current + 1;
    } else {
        line_length = remaining;
    }

    PyObject* result = Py_BuildValue("s#", self->current, line_length);
    // Advance current pointer by the length of the line we just returned
    self->current += line_length;
    return result;
}

// Generator initialization function
static PyObject* mmap_io(PyObject* self, PyObject* args) {

    char* filename;
    if (!PyArg_ParseTuple(args, "s", &filename))
        return NULL;

    MMapObject* obj = PyObject_New(MMapObject, &MMapToType);
    if (!obj) return NULL;


    // Open the file
    obj->filename = filename;
    obj->fd = open(obj->filename, O_RDONLY);
    if (obj->fd == -1) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    // Get file size
    if (fstat(obj->fd, &(obj->file_stat)) == -1) {
        close(obj->fd);
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    // Memory-map the file
    obj->mapped = mmap(NULL, obj->file_stat.st_size, PROT_READ, MAP_PRIVATE, obj->fd, 0);
    if (obj->mapped == MAP_FAILED) {
        close(obj->fd);
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    }

    //Update current pointer
    obj->current = obj->mapped;

    return (PyObject*)obj;
}


static PyTypeObject MMapToType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mmap_module.mmap_io",
    .tp_basicsize = sizeof(MMapObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = mmap_io,  // Set the tp_new slot
    .tp_iter = PyObject_SelfIter,
    .tp_iternext = (iternextfunc)readline,
};

// Define module methods
static PyMethodDef MMapMethods[] = {
    {"mmap_io", mmap_io, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}
};

// Define module
static struct PyModuleDef mmapmodule = {
    PyModuleDef_HEAD_INIT,
    "mmap_module",
    "Example module using CPython API",
    -1,
    MMapMethods
};

// Module initialization
PyMODINIT_FUNC PyInit_mmap_module(void) {
    if (PyType_Ready(&MMapToType) < 0) return NULL;

    PyObject* m = PyModule_Create(&mmapmodule);
    if (!m) return NULL;

    Py_INCREF(&MMapToType);
    PyModule_AddObject(m, "mmap_io", (PyObject*)&MMapToType);
    return m;
}
