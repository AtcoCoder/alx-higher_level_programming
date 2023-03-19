#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p)
{
	PyBytesObject *pp = (PyBytesObject *) p;
	printf("%s", PyBytes_AsString(p));
}
