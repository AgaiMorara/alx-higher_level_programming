#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: PyObject list object
 */
void print_python_list_info(PyObject *p)
{
    long int size, i;
    PyListObject *list;
    PyObject *item;

    /* Get the size of the list */
    size = PyList_Size(p);
    
    /* Cast PyObject to PyListObject to access internal members */
    list = (PyListObject *)p;

    /* Print size and allocated space */
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    /* Print type of each element */
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
