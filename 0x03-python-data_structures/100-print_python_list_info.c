#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic infor about Python
 *
 * @p: Python list object
 *
 * Returns: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p);
	int i;

	PyObject **ob_item;
	PyListObject *pp;

	pp = (PyListObject *) p;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", pp->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(pp->ob_item[i])->tp_name);
	}
}
