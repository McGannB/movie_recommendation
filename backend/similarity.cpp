#include <vector>
#include <cmath>

// Function to calculate cosine similarity
double cosine_similarity(const std::vector<double>& vec1, const std::vector<double>& vec2) {
    double dot = 0.0, mag1 = 0.0, mag2 = 0.0;
    for (size_t i = 0; i < vec1.size(); ++i) {
        dot += vec1[i] * vec2[i];
        mag1 += vec1[i] * vec1[i];
        mag2 += vec2[i] * vec2[i];
    }
    return dot / (std::sqrt(mag1) * std::sqrt(mag2));
}