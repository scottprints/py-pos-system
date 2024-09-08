import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from models import Product

def get_recommendations(products, target_product_name, top_n=5):
    product_names = [product.name for product in products]
    product_categories = [product.category for product in products]

    # Create a count matrix
    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(product_categories)

    # Compute the cosine similarity matrix
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    # Get the index of the target product
    target_idx = product_names.index(target_product_name)

    # Get the pairwise similarity scores of all products with the target product
    sim_scores = list(enumerate(cosine_sim[target_idx]))

    # Sort the products based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the top_n most similar products
    sim_scores = sim_scores[1:top_n+1]

    # Get the product indices
    product_indices = [i[0] for i in sim_scores]

    # Return the top_n most similar products
    return [products[i] for i in product_indices]
