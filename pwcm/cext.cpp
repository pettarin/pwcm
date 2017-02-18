#include <Python.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cfunc.h"

// wrapper around _dosomething
static PyObject *dosomething(PyObject *self, PyObject *args) {
    return Py_BuildValue("i", _dosomething());
}

static PyMethodDef cext_methods[] = {
    {
        "dosomething",
        dosomething,
        METH_VARARGS,
        "Do something: returns a different int for each different version of the function"
    },
    {
        NULL,
        NULL,
        0,
        NULL
    }
};

// Python 2 and 3
#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "cext",         /* m_name */
    "cext",         /* m_doc */
    -1,             /* m_size */
    cext_methods,   /* m_methods */
    NULL,           /* m_reload */
    NULL,           /* m_traverse */
    NULL,           /* m_clear */
    NULL,           /* m_free */
};
#endif

static PyObject *moduleinit(void) {
    PyObject *m;

#if PY_MAJOR_VERSION >= 3
    m = PyModule_Create(&moduledef);
#else
    m = Py_InitModule("cext", cext_methods);
#endif

    return m;
}

#if PY_MAJOR_VERSION >= 3
PyMODINIT_FUNC PyInit_cext(void) {
    return moduleinit();
}
#else
PyMODINIT_FUNC initcext(void) {
    moduleinit();
}
#endif
