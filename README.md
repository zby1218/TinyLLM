# TinyLLM

预训练一个微型语言模型，模型结构与decoder-only的大模型一致,参数大小为`38M`

训练语料库: huggingface jingyaogong/minimind_dataset/[mobvoi_seq_monkey_general_open_corpus.zip](https://huggingface.co/datasets/jingyaogong/minimind_dataset/blob/main/mobvoi_seq_monkey_general_open_corpus.zip)

已实现：

- tokenizer

- RMSRorm

- RoPE

- Group Query Attention

- KV Cache

- MOE


