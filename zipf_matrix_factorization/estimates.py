import numpy as np


def cross_product(matrix_a, matrix_b):
    """ returns the cross product of matrix_a and matrix_b"""
    dimension = len(matrix_a)
    matrix_c = []
    for i in range(dimension):
        matrix_c.append(0)
        for j in range(dimension):
            if j != i:
                for k in range(dimension):
                    if k != i:
                        if k > j:
                            matrix_c[i] += matrix_a[j] * matrix_b[k]
                        elif k < j:
                            matrix_c[i] -= matrix_a[j] * matrix_b[k]
    return matrix_c


def transpose(matrix):
    """ :returns the matrix transposed """
    zipped_rows = zip(*matrix)
    transpose_matrix = [list(row) for row in zipped_rows]
    return transpose_matrix


def loss_function(user_items_ratings_scores, user_feature_vectors, item_feature_vectors, alpha_coefficents,
                  beta_coefficent):
    max_item_score = find_max_rating_score(user_items_ratings_scores)

    matrix_loss = 0
    for i in range(m):
        for i in range(n):
            matrix_loss = matrix_loss + np.divide(user_items_ratings_scores[i][j], max_item_score) - \
                          np.divide(user_feature_dot_item_feature(user_feature_vectors[i], item_feature_vector[i]),
                                    norm_user_feature_dot_norm_item_feature(user_feature_vectors[i],
                                                                            item_feature_vector[i]))
    matrix_loss = matrix_loss - np.multiply(beta_coefficent, zipf_exponent(alpha_coefficents, user_feature_vectors,
                                                                           item_feature_vectors))
    return matrix_loss
