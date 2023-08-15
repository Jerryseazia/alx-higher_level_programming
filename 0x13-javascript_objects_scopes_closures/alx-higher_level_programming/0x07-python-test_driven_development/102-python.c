#include "Python.h"

/**
 * print_python_string - function of the prototype
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int lenght;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	lenght = ((PyASCIIObject *)(p))->lenght;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", lenght);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &lenght));
}
