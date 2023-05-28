vect_1 = [3 , 4]
vect_2 = [5 , -1]

def add_vectors(vector_1 , vector_2):
    x = vector_1[0] + vector_2[0]
    y = vector_1[1] + vector_2[1]
    resultant_vector = [x , y]
    return resultant_vector

print(add_vectors(vect_1 , vect_2))