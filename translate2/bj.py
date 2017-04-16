# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 23:36:52 2017

@author: kht
"""

seq2seq.model_with_buckets(
                    self.encoder_inputs, self.decoder_inputs, targets,
                    self.target_weights, buckets,
                    lambda x, y: seq2seq_f(x, y, False),
                    softmax_loss_function=softmax_loss_function)
                    
                    
#model_with_buckets：606
#embedding_attention_seq2seq：131
#embedding_attention_seq2seq：370
#embedding_attention_decoder：299     
#attention_decoder：121