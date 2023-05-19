# PLH-Practica4
A Github repo to handle code and information for a practical work training word embeddings.

Contains python files for two classes, data and models each to handle corpus of text and different models
trained for word embeddings, respectively.

A sample jupyter notebook for usage is provided. However, NO notebook apart from this one should be pushed
into the repo because notebooks are to be developed apart from the repo. This repo IS ONLY to handle the classes which will be imported into the notebooks.

## INFORMATION ABOUT WORD2VEC

Recommended links:
https://towardsdatascience.com/word2vec-skip-gram-model-part-1-intuition-78614e4d6e0b

http://mccormickml.com/2017/01/11/word2vec-tutorial-part-2-negative-sampling/

Word2Vec method will be used for a skip-gram method. A Word2Vec method can be seen in the following analyisis of the large baseline model provided:

1. **Function Definition**: The code defines a function named `build_and_compile_model` that takes several input arguments: `input_length`, `hidden_size`, `dictionary_size`, and `embedding_size`. These arguments determine the architecture and hyperparameters of the model.

2. **Input Layers**: The function begins by creating two input layers, `input_1` and `input_2`, using `tf.keras.Input`. These layers will be used to provide input to the model. Each input has a shape of `(input_length,)`, indicating a sequence of integers.

3. **Layers Definition**: The code proceeds to define the layers used in the model:

   - `Embedding Layer`: The `embedding` layer converts the input integers into dense vectors of fixed size. It maps each integer to a dense representation. The `Embedding` layer takes the `dictionary_size` (the number of unique words or tokens) and `embedding_size` (the dimensionality of the embedding vectors) as arguments. The `input_length` parameter specifies the length of input sequences.

   - `GlobalAveragePooling1D Layer`: The `pooling` layer performs global average pooling over the sequence dimension. It takes the average value for each feature across the entire sequence, resulting in a fixed-length output vector.

   - `Concatenate Layer`: The `concatenate` layer concatenates the output vectors from the previous pooling layers. It combines the representations from `input_1` and `input_2`.

   - `Dense Layers`: The `hidden` layer is a fully connected layer with `hidden_size` neurons and ReLU activation. It processes the concatenated input representation. The `output` layer is another fully connected layer with a single neuron and no activation function.

4. **Layer Connections**: The code connects the layers to define the flow of data through the model:

   - The input sequences `input_1` and `input_2` are passed through the `embedding` layer to obtain embedded representations `_embedded_1` and `_embedded_2`.

   - The embedded representations are then passed through the `pooling` layers, `_pooled_1` and `_pooled_2`, respectively. The `mask` argument ensures that any padding tokens (represented by 0) are ignored during pooling.

   - The pooled representations are concatenated using the `concatenate` layer, resulting in `_concatenated`.

   - The concatenated output is then passed through the `hidden` layer to obtain `_hidden_output`.

   - Finally, the `_hidden_output` is passed through the `output` layer to produce `_output`.

5. **Model Definition**: The function assembles the layers into a `tf.keras.Model` object by specifying the input and output tensors. The resulting model is assigned to the variable `model`.

6. **Model Compilation**: The model is compiled with a specific loss function (`mean_absolute_error`) and an optimizer (`Adam`) using the `model.compile` method.

7. **Return**: The function returns the compiled model.

For further understanding of word2vec please check the pdf provided. 