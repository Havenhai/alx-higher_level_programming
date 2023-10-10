#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int sizehaven, allochaven, i;
	PyObject *obj;

	sizehaven = Py_SIZE(p);
	allochaven = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sizehaven);
	printf("[*] Allocated = %d\n", allochaven);

	for (i = 0; i < sizehaven; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
