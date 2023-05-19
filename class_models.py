import tensorflow as tf

class Models:
    """
    =====================================================================================================
    Class Models - Contains methods and attributes to work with the different Models to be used.
    =====================================================================================================

    • ATTRIBUTES
    ------------
        ⮕ models // An internal dictionary model_name - model where each trained model is stored.
    ------------

    • METHODS
    ------------
      ~ MODIFIERS ~
        ⮕ add_model // Adds a model to the internal dictionary by providing the model and its name.
        ⮕ train_model // Trains a stored model based on its name given a data object.
        ⮕ get_common_words // Applies the skipgram method for a word.
        ⮕ build_and_compile_large_baseline // Computes the large baseline.
        ⮕ build_and_compile_short_baseline // Computes the short baseline.
    ------------
    """
    def __init__(self):
        'Setting up models dictionary to store various models.'
        self._models = {}

        'Setting up the baseline...'
        base_model = self.build_and_compile_large_baseline() # Computed with default values...
        self.add_model(base_model,'large_baseline')
        base_model = self.build_and_compile_short_baseline() # Computed with default values...
        self.add_model(base_model,'short_baseline')

    def __str__(self):
        'Representation method to see all models'
        res = ''
        for pair in self._datasets.items():
            key, value = pair[0], pair[1]
            res.join(f'Model Name: {key}, Number of rows: {value.summary()}\n') # Might be Wrong!
        return res

    def add_model(self,model,model_name):
        self._models[model_name] = model
    
    def train_model(self,data: Data,model_name: str):
        'Pre: data parameter is an instance of class Data'
        'Post: Model trained on this data'
        return(not_implemented)
    
    def get_common_words(word: str, model_name: str):
        'Function to apply the skipgram method'
        return(not_implemented)

    
    def build_and_compile_large_baseline(
            self,input_length: int = 10, hidden_size: int = 64, dictionary_size: int = 1000, embedding_size: int = 16,
    ) -> tf.keras.Model:
        input_1, input_2 = tf.keras.Input((input_length, ), dtype=tf.int32, ), tf.keras.Input((input_length, ), dtype=tf.int32, )
        # Define Layers
        embedding = tf.keras.layers.Embedding(
            dictionary_size, embedding_size, input_length=input_length, mask_zero=True, )
        pooling = tf.keras.layers.GlobalAveragePooling1D() # Colapsa els valors del vector en un de sol
        concatenate = tf.keras.layers.Concatenate(axis=-1, )
        hidden = tf.keras.layers.Dense(hidden_size, activation='relu')
        output = tf.keras.layers.Dense(1)
        # Pass through the layers
        _input_mask_1, _input_mask_2 = tf.not_equal(input_1, 0), tf.not_equal(input_2, 0)
        _embedded_1, _embedded_2 = embedding(input_1, ), embedding(input_2, )
        _pooled_1, _pooled_2 = pooling(_embedded_1, mask=_input_mask_1), pooling(_embedded_2, mask=_input_mask_2)
        _concatenated = concatenate((_pooled_1, _pooled_2, ))
        _hidden_output = hidden(_concatenated)
        _output = output(_hidden_output)
        # Define the model
        model = tf.keras.Model(inputs=(input_1, input_2, ), outputs=_output, )
        model.compile(loss='mean_absolute_error',
                    optimizer=tf.keras.optimizers.Adam(0.001))
        return model