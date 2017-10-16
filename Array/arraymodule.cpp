#include <Python.h>
#include "Array.h"

static PyObject* array_wrapper(PyObject* self, PyObject* args) {
    // Declaring the input and return types;
    PyObject* input;
    PyObject* ret;
    
    // Check that what was passed in is an object (and only one argument!)
    if (!PyArg_ParseTuple(args, "O", &input)) {
        return NULL;
    }

    // Get an iterator over the list.
    PyObject *iter = PyObject_GetIter(input);
    if (!iter) {
      // It's not iterable.
      return NULL;
    }

    Py_ssize_t len = PyList_Size(input);
    
    long* arr = new long[len];

    int i = 0;
    // Run through the array
    while (true) {
        PyObject *next = PyIter_Next(iter);
        if (!next || i >= len) {
          // nothing left in the iterator or out of space in array
          break;
        }
      
        if (!PyLong_Check(next)) {
          // error, we were expecting an integer
        }
        
        // Add the number to the array
        long num = PyLong_AsLong(next);
        arr[i] = num;
        i++;
    }

    arr = copy_list(arr, len);

    ret = PyList_New(len);
    if (!ret) { 
        // Couldn't allocate memory for the list
        return NULL;
    }

    for (int i = 0; i < len; i++) {
        // Convert the number to a Python number
        PyObject* num = PyLong_FromLong(arr[i]);
        // Add it to the list
        PyList_SET_ITEM(ret, i, num);
    }
    delete[] arr;
    return ret;
}

// Add the copylist to the symbol table
static PyMethodDef CopyListMethods[] = {
    { "copy_list", array_wrapper, METH_VARARGS, "Sorts a list of integers." },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef copy_list_mod =
{
    PyModuleDef_HEAD_INIT,
    "copylist", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    CopyListMethods,
};

// Initialize it
PyMODINIT_FUNC PyInit_copylist(void)
{
    return PyModule_Create(&copy_list_mod);
}