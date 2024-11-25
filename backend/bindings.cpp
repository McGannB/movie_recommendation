#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "similarity.cpp"

namespace py = pybind11;

PYBIND11_MODULE(matrix_ops, m) {
    m.doc() = "Matrix operations module";
    m.def("cosine_similarity", &cosine_similarity, "Compute cosine similarity");
}