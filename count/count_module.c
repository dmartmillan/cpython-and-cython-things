#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Forward declaration of the generator type
typedef struct {
    PyObject_HEAD
    double count;
    double max_value;
} CountUpToObject;

// Forward declare the generator type object
static PyTypeObject CountUpToType;

// Generator's iteration function
static PyObject* count_up_to_next(CountUpToObject* self) {
    if (self->count > self->max_value) {
        PyErr_SetNone(PyExc_StopIteration);
        return NULL;
    }
    return Py_BuildValue("d", self->count++);
}

// Generator initialization function
static PyObject* count_up_to(PyObject* self, PyObject* args) {
    double max_value;
    if (!PyArg_ParseTuple(args, "d", &max_value))
        return NULL;

    CountUpToObject* obj = PyObject_New(CountUpToObject, &CountUpToType);
    if (!obj) return NULL;

    obj->count = 1;
    obj->max_value = max_value;
    return (PyObject*)obj;
}

// Define the generator type
static PyTypeObject CountUpToType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "count_module.CountUpTo",
    .tp_basicsize = sizeof(CountUpToObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_iter = PyObject_SelfIter,
    .tp_iternext = (iternextfunc)count_up_to_next,
};

// Define module methods
static PyMethodDef CountMethods[] = {
    {"count_up_to", count_up_to, METH_VARARGS, "Generate numbers up to max_value"},
    {NULL, NULL, 0, NULL}
};

// Define module
static struct PyModuleDef countmodule = {
    PyModuleDef_HEAD_INIT,
    "count_module",
    "Example module using CPython API",
    -1,
    CountMethods
};

// Module initialization
PyMODINIT_FUNC PyInit_count_module(void) {
    if (PyType_Ready(&CountUpToType) < 0) return NULL;

    PyObject* m = PyModule_Create(&countmodule);
    if (!m) return NULL;

    Py_INCREF(&CountUpToType);
    PyModule_AddObject(m, "CountUpTo", (PyObject*)&CountUpToType);
    return m;
}
